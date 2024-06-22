from flask import Blueprint, render_template, request, url_for, redirect

bp = Blueprint("orderitem", __name__, url_prefix="/orderitem")


@bp.route("/")
def get_orderitems():
    return render_template("orderitem/orderitem_list.html")
