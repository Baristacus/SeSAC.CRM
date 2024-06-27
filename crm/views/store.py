from flask import Blueprint, render_template, request
from sqlalchemy import func

from crm.models import User, Order, Store, Item, OrderItem

bp = Blueprint("store", __name__, url_prefix="/store")


@bp.route("/")
def get_stores():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)

    store_list = Store.query.paginate(page=page, per_page=per_page)
    store_total = Store.query.count()

    return render_template(
        "store/store_list.jinja2",
        title="전체 상점 목록",
        store_list=store_list,
        store_total=store_total,
    )


@bp.route("/<id>")
def get_store(id):
    store = Store.query.get(id)

    # ! 월간 매출액 가져오기
    # ? 1. Order 테이블과 OrderItem 테이블을 조인하여 Item 테이블의 UnitPrice를 가져온다.
    # ? 2. 이를 Order 테이블의 OrderAt 컬럼을 기준으로 월간 매출액과 주문수 리스트를 가져온다.

    sales = (
        Order.query.join(OrderItem, Order.Id == OrderItem.OrderId)
        .join(Item, OrderItem.ItemId == Item.Id)
        .add_columns(
            func.strftime("%Y년 %m월", Order.OrderAt).label("Month"),
            func.sum(Item.UnitPrice).label("MonthlySales"),
            func.count(OrderItem.Id).label("OrderCount"),
        )
        .filter(Order.StoreId == id)
        .group_by("Month")
        .order_by(Order.OrderAt.desc())
        .all()
    )

    total_sales = sum([sale.MonthlySales for sale in sales])

    # ! 단골 고객 가져오기

    vip_users = (
        User.query.join(Order, User.Id == Order.UserId)
        .add_columns(User.Name, func.count(Order.Id).label("OrderCount"))
        .filter(Order.StoreId == id)
        .group_by(User.Id)
        .order_by(func.count(Order.Id).desc())
        .limit(5)
        .all()
    )

    print(vip_users)

    return render_template(
        "store/store_detail.jinja2",
        title="상점 상세 정보",
        store=store,
        sales=sales,
        total_sales=total_sales,
        vip_users=vip_users,
    )
