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

    # 월간 매출액 가져오기

    # 단골 고객 가져오기

    return render_template(
        "store/store_detail.jinja2",
        title="상점 상세 정보",
        store=store,
    )
