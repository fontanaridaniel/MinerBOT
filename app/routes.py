from app import app
from flask import render_template


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/charts")
def charts():
    return render_template("charts.html")


@app.route("/earnings")
def earnings():
    return render_template("earnings.html")