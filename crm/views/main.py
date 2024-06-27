from flask import Blueprint, render_template
from crm.models import User, Order, Store, Item, OrderItem

bp = Blueprint("main", __name__, url_prefix="/")


@bp.route("/")
def index():

    user_count = User.query.count()
    order_count = Order.query.count()
    store_count = Store.query.count()
    item_count = Item.query.count()
    orderitem_count = OrderItem.query.count()

    return render_template(
        "main/index.jinja2",
        user_count=user_count,
        store_count=store_count,
        item_count=item_count,
        order_count=order_count,
        orderitem_count=orderitem_count,
    )
