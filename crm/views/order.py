from flask import Blueprint, render_template, request
from sqlalchemy import func
from crm.models import User, Order, Store, Item, OrderItem

bp = Blueprint("order", __name__, url_prefix="/order")


@bp.route("/")
def get_orders():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)

    order_list = Order.query.paginate(page=page, per_page=per_page)
    order_total = Order.query.count()

    # orders.UserId -> User.Name
    # orders.StoreId -> Store.Name

    return render_template(
        "order/order_list.html",
        title="전체 주문 목록",
        order_list=order_list,
        order_total=order_total,
    )
