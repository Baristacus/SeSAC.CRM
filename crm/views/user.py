from flask import Blueprint, render_template, request, url_for, redirect

bp = Blueprint("user", __name__, url_prefix="/user")

from crm.models import User, Order, OrderItem, Item


@bp.route("/")
def get_users():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)

    name = request.args.get("name")
    gender = request.args.get("gender")
    age = request.args.get("age")

    user_list = User.query.paginate(page=page, per_page=per_page)
    user_total = User.query.count()

    if name:
        user_list = User.query.filter(User.Name.like(f"%{name}%")).paginate(
            page=page, per_page=per_page
        )
    if gender:
        user_list = User.query.filter(User.Gender == gender).paginate(
            page=page, per_page=per_page
        )
    if age:
        user_list = User.query.filter(User.Age == age).paginate(
            page=page, per_page=per_page
        )

    return render_template(
        "user/user_list.html",
        title="전체 회원 목록",
        user_list=user_list,
        user_total=user_total,
    )


@bp.route("/<id>")
def get_user(id):
    user = User.query.get(id)
    order_list = (
        Order.query.filter(Order.UserId == id).order_by(Order.OrderAt.desc()).all()
    )

    return render_template(
        "user/user_detail.html",
        title=f"{user.Name}님의 회원 정보",
        user=user,
        order_list=order_list,
    )
