import os
import json
import jinja2
import datetime
import flask
from flask import Flask, session, send_from_directory, Response, render_template, request, redirect
from flask_login.login_manager import LoginManager,redirect
from flask_login.utils import login_required, login_user, logout_user
# from gevent.pywsgi import WSGIServer


from server.model.usermodel import User
from server.services.mail_conf import *
# get_clients, get_cats, get_mail_comf, save_mail_conf, block_mail_conf, get_mail, otp_send_process


from server.services import logger
from server.constants import *


app = Flask(__name__)
app.secret_key = SEC_KEY
app.SESSION_COOKIE_SECURE = True


if IS_DEVELOPMENT:
    app.config["debug"] = True
else:
    app.config["debug"] = False


loginmanager = LoginManager()
loginmanager.init_app(app)
loginmanager.login_view = "/infolist/login/"

ROOT_PATH = os.path.join(os.path.split(__file__)[0],"..")
CSS_PATH = os.path.join(ROOT_PATH, "static", "css")
JS_PATH = os.path.join(ROOT_PATH, "static", "js")
IMAGES_PATH = os.path.join(ROOT_PATH, "static", "images")
FONT_PATH = os.path.join(ROOT_PATH, "static", "font")
DOCS_PATH = os.path.join(ROOT_PATH, "templates", "docs")


unauthtemplates = ["/login/login.html"]


TEMPLATE_PATH = [("/", "login/login.html"),
                 ("/infolist/login", "/login/login.html"),
                 ("/infolist/index", "/home/index.html"),
                 ("/infolist/mail-conf", "/mail-configuration-client/mail-configuration-client.html"),
                 ("/infolist/regenrate-password", "/regenrate-password/regenrate-password.html" ),
                 ("/infolist/logout", "/login/login.html")]


template_loader = jinja2.FileSystemLoader(os.path.join(ROOT_PATH, "templates"))
app.jinja_loader = template_loader

STATIC_PATH = [("/css/<path:filename>", CSS_PATH),
               ("/js/<path:filename>", JS_PATH),
               ("/images/<path:filename>", IMAGES_PATH),
               ("/font/<path:filename>", FONT_PATH),
               ("/docs/<path:filename>", DOCS_PATH)]



def staticTemplate(pathname, filename):
    return send_from_directory(pathname, filename)

def render_my_template(pathname):
    output = render_template(pathname)
    return output

@login_required
def auth_render_template(pathname):
    output = render_template(pathname)
    return output

# @loginmanager.login_user
# def auth_render_template(pathname):
#     output = render_template(pathname)
#     return output


@loginmanager.user_loader
def load_user(user_id):
    return User(user_id)

def do_login():
    if request.form.get("username")==USER_NAME and request.form.get('password')==PWD:
        user = User(USER_NAME)
        logout_user()
        return redirect("/infolist/index.html")
    return redirect("/infolist/login")


def do_logout():
    logout_user()
    return redirect("/infolist/login")





def get_client_list():
    rdata = get_clients()
    resp  = Response(json.dumps(rdata), status=200, mimetype="application/json")
    return resp


def get_category_list():
    rdata =get_cats()
    resp = Response(json.dumps(rdata), status=200, mimetype="application/json")
    return resp

def mail_list():
    rdata = get_mail()
    resp = Response(json.dumps(rdata), status=200, mimetype="application/json")
    return resp

def get_mail_list():
    rdata = get_mail_comf(request.data.decode('utf-8'))
    resp = Response(json.dumps(rdata), status=200, mimetype="application/json")
    return resp

def save_mail_confige():
    rdata = get_mail_comf(request.data.decode('utf-8'))
    resp = Response(json.dumps(rdata), status=200, mimetype="application/json")
    return resp

def block_mail_confige():
    rdata = get_mail_comf(request.data.decode('utf-8'))
    resp = Response(json.dumps(rdata), status=200, mimetype="application/json")
    return resp

def get_otp():
    rdata = otp_send_process(request.data.decode('utf-8'))
    resp = Response(json.dumps(rdata), status=200, mimetype="application/json")
    return resp



@app.before_request
def make_session_permanent():
    now = datetime.datetime.now()
    last_active = session.get("last_active")
    if last_active:
        delte = now - last_active
        if delte.seconds > SCUT:
            session['last_active'] = now
            logout_user()
        session['last_active'] = now


def runserver(port):
    for path in STATIC_PATH:
        app.add_url_rule(
            path[0], view_func = staticTemplate, methods = ['GET'],
            defaults = {'pathname':path[1]})
    for idx, path in enumerate(TEMPLATE_PATH):
        if (path[1] not in unauthtemplates):
            app.add_url_rule(path[0], view_func = auth_render_template, methods = ['GET'],
            defaults = {'pathname': path[1]})
        else:
            app.add_url_rule(path[0], view_func=render_my_template, methods=['GET'],
            defaults={'pathname': path[1]})
    api_urls_and_handlers = [("/", 'POST', do_login),
                 ("/infolist/get_clients", 'GET', get_client_list),
                 ("/infolist/get_cats", 'GET', get_category_list),
                 # ("infolist/get_mail_conf",'POST', get_mail_comf),
                 # ("infolist/save_mail_conf", 'POST', save_mail_conf),
                 # ("infolist/block_mail_conf", 'POST', block_mail_conf),
                 ("/infolist/get_mail_data", 'POST', get_mail_list),
                 ("/infolist/get_otp_data", 'GET', get_otp),
                 ("/infolist/api/logout",'GET', do_logout)]
    for u in api_urls_and_handlers:
        app.add_url_rule(u[0], view_func = u[2], methods=[u[1]])

    settings = { "threaded": True,"debug": True, "use_reloader": False}
    logger.info('server started at %s ' % port)
    logger.debug('server started at %s ' % port)
    logger.error('server started at %s ' % port)
    print('server started at %s ' % port)

    app.run(host="0.0.0.0", port = port ,**settings)
