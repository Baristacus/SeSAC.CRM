from flask import Blueprint, render_template, request, url_for, redirect

bp = Blueprint("item", __name__, url_prefix="/item")


@bp.route("/")
def get_items():
    return render_template("item/item_list.html")
