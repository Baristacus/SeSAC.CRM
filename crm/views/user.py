from flask import Blueprint, render_template, request, url_for, redirect

bp = Blueprint("user", __name__, url_prefix="/user")

from crm.models import User, Order


@bp.route("/")
def get_users():
    page = request.args.get("page", 1, type=int)
    user_list = User.query.paginate(page=page, per_page=10)
    return render_template("user/user_list.html", user_list=user_list)
