from flask import Blueprint, render_template


home_view = Blueprint("home_view", __name__)

@home_view.route("/")
def display_home_page():
    return render_template("index.html", num=10)
