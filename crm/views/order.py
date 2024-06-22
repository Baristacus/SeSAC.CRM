from flask import Blueprint, render_template, request, url_for, redirect

bp = Blueprint("order", __name__, url_prefix="/order")


@bp.route("/")
def get_orders():
    return render_template("order/order_list.html")
