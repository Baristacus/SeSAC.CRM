from flask import Blueprint, render_template, request, redirect, url_for, flash
from sqlalchemy import func
from crm.models import User, Order, Store, Item, OrderItem

bp = Blueprint("order", __name__, url_prefix="/order")


@bp.route("/")
def get_orders():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)

    if page < 1 or per_page * (page - 1) > Order.query.count():
        flash("페이지 번호가 잘못되었습니다. 첫 페이지로 이동합니다.", "danger")
        page = 1

    order_list = Order.query.order_by(Order.OrderAt.desc()).paginate(
        page=page, per_page=per_page
    )
    order_total = Order.query.count()

    # ? 이게 왜 되는거지? ㅡ..ㅡ; 스스로에게 값을 추가?
    for order in order_list.items:
        user = User.query.get(order.UserId)
        store = Store.query.get(order.StoreId)
        order.UserName = user.Name
        order.StoreName = store.Name
        order.StoreType = store.Type

    return render_template(
        "order/order_list.jinja2",
        title="전체 주문 목록",
        order_list=order_list,
        order_total=order_total,
    )


@bp.route("/<id>")
def get_order(id):
    try:
        order = Order.query.get(id)

        if not order:
            flash("해당 주문이 존재하지 않습니다.", "danger")
            return redirect(url_for("order.get_orders"))

        # ! 해당 id에 대한 주문 상세 정보 가져오기
        order_detail = (
            Order.query.join(OrderItem, Order.Id == OrderItem.OrderId)
            .join(Item, OrderItem.ItemId == Item.Id)
            .add_columns(Item.Id, Item.Name, Item.UnitPrice)
            .filter(Order.Id == id)
            .all()
        )

        store = Store.query.get(order.StoreId)
        user = User.query.get(order.UserId)

        total_price = sum([item.UnitPrice for item in order_detail])

        print(total_price)

        return render_template(
            "order/order_detail.jinja2",
            title="주문 상세 정보",
            order=order,
            order_detail=order_detail,
            store=store,
            user=user,
            total_price=total_price,
        )
    except:
        flash("해당 주문이 존재하지 않습니다.", "danger")
        return redirect(url_for("order.get_orders"))
