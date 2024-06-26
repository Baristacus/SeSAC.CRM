from flask import Blueprint, render_template, request
from sqlalchemy import func
from crm.models import User, Order, Store, Item, OrderItem

bp = Blueprint("user", __name__, url_prefix="/user")


@bp.route("/")
def get_users():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)

    name = request.args.get("name")
    gender = request.args.get("gender")
    age = request.args.get("age")

    user_list = User.query.paginate(page=page, per_page=per_page)
    user_total = User.query.count()

    if name:
        user_list = User.query.filter(User.Name.like(f"%{name}%")).paginate(
            page=page, per_page=per_page
        )
    if gender:
        user_list = User.query.filter(User.Gender == gender).paginate(
            page=page, per_page=per_page
        )
    if age:
        user_list = User.query.filter(User.Age == age).paginate(
            page=page, per_page=per_page
        )

    return render_template(
        "user/user_list.jinja2",
        title="전체 회원 목록",
        user_list=user_list,
        user_total=user_total,
        name=name,
        gender=gender,
        age=age,
    )


@bp.route("/<id>")
def get_user(id):
    user = User.query.get(id)

    # 주문 내역

    order_list = (
        Store.query.join(Order, Store.Id == Order.StoreId)
        .add_columns(Store.Name, Store.Type, Order.OrderAt)
        .filter(Order.UserId == id)
        .order_by(Order.OrderAt.desc())
        .all()
    )

    store_top5 = (
        Store.query.join(Order, Store.Id == Order.StoreId)
        .add_columns(Store.Name, Store.Type)
        .filter(Order.UserId == id)
        .group_by(Store.Id)
        .order_by(func.count().desc())
        .limit(5)
    )

    visited_count = (
        Order.query.filter(Order.UserId == id)
        .add_columns(Order.StoreId, func.count())
        .group_by(Order.StoreId)
        .order_by(func.count().desc())
        .all()
    )

    # 자주 방문한 매장 TOP5

    store_top5_visit = (
        Store.query.join(Order, Store.Id == Order.StoreId)
        .filter(Order.UserId == id)
        .add_columns(
            Store.Name, Store.Type, func.count(Order.StoreId).label("visit_count")
        )
        .group_by(Store.Id)
        .order_by(func.count(Order.StoreId).desc())
        .limit(5)
        .all()
    )

    # 자주 주문한 상품 TOP5

    item_top5 = (
        Item.query.join(OrderItem, Item.Id == OrderItem.ItemId)
        .join(Order, Order.Id == OrderItem.OrderId)
        .filter(Order.UserId == id)
        .add_columns(
            Item.Name, Item.Type, func.count(OrderItem.ItemId).label("order_count")
        )
        .group_by(Item.Id)
        .order_by(func.count(OrderItem.ItemId).desc())
        .limit(5)
        .all()
    )

    return render_template(
        "user/user_detail.jinja2",
        title=f"{user.Name}님의 회원 정보",
        user=user,
        order_list=order_list,
        store_top5=store_top5_visit,
        item_top5=item_top5,
    )
