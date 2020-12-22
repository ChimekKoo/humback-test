from flask import Flask, render_template, request, redirect, url_for
from validators import url as validurl

from webgui.get_app import getapp
from app.main import __version__

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index_endpoint():
    return render_template("index.html", version=__version__, getapp_status="", testapp_status="")


@app.route("/get-app", methods=["GET"])
def get_app_endpoint():
    return render_template("get-app.html", version=__version__, status="")


@app.route("/test-app", methods=["GET"])
def test_app_endpoint():
    return render_template("test-app.html", version=__version__, status="")


@app.route("/get-app-action", methods=["GET", "POST"])
def get_app_action_endpoint():
    if request.method == "POST":
        req = request.form

        getapp_status = '<span class="status-positive">App downloaded successfuly.</span>'

        while True:
            try:
                req["name"]
            except NameError:
                getapp_status = '<span class="status-negative">&ldquo;App name&ldquo; field cannot be empty.</span>'
                break

            try:
                req["url"]
            except NameError:
                getapp_status = '<span class="status-negative">&ldquo;Humbackfile URL&ldquo; field cannot be empty.</span>'
                break

            if not validurl(req["url"]):
                getapp_status = '<span class="status-negative">&ldquo;Humbackfile URL&ldquo; field must contain a valid url.</span>'
                break

            getapp(req["name"], req["url"])
            break

        return render_template(
            "index.html",
            version=__version__,
            getapp_status=getapp_status,
            testapp_status=''
        )
    else:
        redirect(url_for(get_app_endpoint()))
