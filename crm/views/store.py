from flask import Blueprint, render_template, request, url_for, redirect

bp = Blueprint("store", __name__, url_prefix="/store")


@bp.route("/")
def get_stores():
    return render_template("store/store_list.html")
