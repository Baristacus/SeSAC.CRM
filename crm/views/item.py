from flask import Blueprint, render_template, request
from sqlalchemy import func
from crm.models import User, Order, Store, Item, OrderItem

bp = Blueprint("item", __name__, url_prefix="/item")


@bp.route("/")
def get_items():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)

    item_list = Item.query.paginate(page=page, per_page=per_page)
    item_total = Item.query.count()

    return render_template(
        "item/item_list.jinja2",
        title="전체 상품 목록",
        item_list=item_list,
        item_total=item_total,
    )


@bp.route("/<id>")
def get_item(id):
    item = Item.query.get(id)

    # 월간 매출액 가져오기

    # 월간 매출액 그래프

    return render_template(
        "item/item_detail.jinja2",
        title="상품 상세 정보",
        item=item,
    )
