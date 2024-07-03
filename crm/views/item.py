from flask import Blueprint, render_template, request, redirect, url_for, flash
from sqlalchemy import func
from crm.models import User, Order, Store, Item, OrderItem

bp = Blueprint("item", __name__, url_prefix="/item")


@bp.route("/")
def get_items():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)

    if page < 1 or per_page * (page - 1) > Item.query.count():
        flash("페이지 번호가 잘못되었습니다. 첫 페이지로 이동합니다.", "danger")
        page = 1

    item_list = Item.query.paginate(page=page, per_page=per_page)
    item_total = Item.query.count()

    name = request.args.get("name")

    if name:
        item_list = Item.query.filter(Item.Name.like(f"%{name}%")).paginate(
            page=page, per_page=per_page
        )
        item_total = Item.query.filter(Item.Name.like(f"%{name}%")).count()

        if item_total == 0:
            flash("해당 이름의 상품이 존재하지 않습니다.", "danger")
            return redirect(url_for("item.get_items"))

    return render_template(
        "item/item_list.jinja2",
        title="전체 상품 목록",
        item_list=item_list,
        item_total=item_total,
        name=name,
    )


@bp.route("/<id>")
def get_item(id):
    try:
        item = Item.query.get(id)

        if not item:
            flash("해당 상품이 존재하지 않습니다.", "danger")
            return redirect(url_for("item.get_items"))

        # ! 월간 매출액 가져오기
        # ? 1. Order 테이블과 OrderItem 테이블을 조인하여 Item 테이블의 UnitPrice를 가져온다.
        # ? 2. Order 테이블의 OrderAt 컬럼을 기준으로 월간 매출액과 주문수 리스트를 가져온다.

        sales = (
            Order.query.join(OrderItem, Order.Id == OrderItem.OrderId)
            .join(Item, OrderItem.ItemId == Item.Id)
            .add_columns(
                func.strftime("%Y년 %m월", Order.OrderAt).label("Month"),
                func.sum(Item.UnitPrice).label("MonthlySales"),
                func.count(OrderItem.Id).label("OrderCount"),
            )
            .filter(OrderItem.ItemId == id)
            .group_by("Month")
            .order_by(Order.OrderAt.desc())
            .all()
        )

        # 월간 매출액 그래프
        chart_month = []
        for sale in sales:
            chart_month.append(sale.Month)

        chart_sales = []
        for sale in sales:
            chart_sales.append(sale.MonthlySales)

        chart_sales_count = []
        for sale in sales:
            chart_sales_count.append(sale.OrderCount)

        return render_template(
            "item/item_detail.jinja2",
            title="상품 상세 정보",
            item=item,
            sales=sales,
            chart_month=chart_month,
            chart_sales=chart_sales,
            chart_sales_count=chart_sales_count,
        )
    except:
        flash("상품 정보를 가져오는 중 오류가 발생했습니다.", "danger")
        return redirect(url_for("item.get_items"))
