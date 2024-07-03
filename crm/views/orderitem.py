from flask import Blueprint, render_template, request, url_for, flash
from sqlalchemy import func
from crm.models import User, Order, Store, Item, OrderItem

bp = Blueprint("orderitem", __name__, url_prefix="/orderitem")


@bp.route("/")
def get_orderitems():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)

    if page < 1 or per_page * (page - 1) > OrderItem.query.count():
        flash("페이지 번호가 잘못되었습니다. 첫 페이지로 이동합니다.", "danger")
        page = 1

    orderitem_list = OrderItem.query.paginate(page=page, per_page=per_page)
    orderitem_total = OrderItem.query.count()

    return render_template(
        "orderitem/orderitem_list.jinja2",
        title="전체 주문 내역",
        orderitem_list=orderitem_list,
        orderitem_total=orderitem_total,
    )
