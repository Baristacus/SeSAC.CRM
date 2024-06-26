from flask import Blueprint, render_template, request
from sqlalchemy import func
from crm.models import User, Order, Store, Item, OrderItem

bp = Blueprint("order", __name__, url_prefix="/order")


@bp.route("/")
def get_orders():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)

    order_list = Order.query.order_by(Order.OrderAt.desc()).paginate(
        page=page, per_page=per_page
    )
    order_total = Order.query.count()

    # 이게 왜 되는거지? ㅡ..ㅡ; 스스로에게 값을 추가?
    for order in order_list.items:
        user = User.query.get(order.UserId)
        store = Store.query.get(order.StoreId)
        order.UserName = user.Name
        order.StoreName = store.Name
        order.StoreType = store.Type

    return render_template(
        "order/order_list.html",
        title="전체 주문 목록",
        order_list=order_list,
        order_total=order_total,
    )


@bp.route("/<id>")
def get_order(id):
    order = Order.query.get(id)

    return render_template(
        "order/order_detail.html",
        title="주문 상세 정보",
        order=order,
    )
