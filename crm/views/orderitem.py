from flask import Blueprint, render_template, request, url_for
from sqlalchemy import func
from crm.models import User, Order, Store, Item, OrderItem

bp = Blueprint("orderitem", __name__, url_prefix="/orderitem")


@bp.route("/")
def get_orderitems():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)

    orderitem_list = OrderItem.query.paginate(page=page, per_page=per_page)
    orderitem_total = OrderItem.query.count()

    return render_template(
        "orderitem/orderitem_list.html",
        title="주문 상세 내역",
        orderitem_list=orderitem_list,
        orderitem_total=orderitem_total,
    )
