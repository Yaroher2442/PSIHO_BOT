from flask.views import MethodView
from flask import Response, request, jsonify, send_from_directory, \
    make_response, render_template, redirect, g
import uuid
import copy
from database.DB_interface import ApiDB
from admin.helpers import *


class BaseView(MethodView):
    def __init__(self):
        self.db = ApiDB()
        self.store = store

    def set_notices(self, type, message):
        self.store.__getattr__("notices").append(Notice(type, message))

    def render_with_notices(self, template):
        curent_notifys = copy.copy(self.store.__getattr__("notices"))
        self.store.__getattr__("notices").clear()
        return render_template(template, notifys=curent_notifys)

    def check_token(self, request):
        req_token = request.cookies.get('auth_token')
        if req_token:
            return self.db.auth.verify_token(req_token)
        else:
            return False


class Register(BaseView):
    def __init__(self):
        BaseView.__init__(self)

    def get(self):
        return render_template('register.html')

    def post(self):
        if self.db.auth.registry_user(request.form.get('name'), request.form.get('email'),
                                      request.form.get('password')):
            return redirect('/')
        else:
            return render_template('register.html')


class Login(BaseView):
    def __init__(self):
        BaseView.__init__(self)

    def get(self):
        return self.render_with_notices('login.html')

    def post(self):
        token = self.db.auth.login_user(request.form.get('email'), request.form.get('password'))
        if token:
            res = make_response(redirect('/index'))
            res.set_cookie('auth_token', token, max_age=60 * 60 * 24)
            return res
        else:
            self.set_notices(Notice.danger, 'User not found')
            return redirect('/login')


class Logout(BaseView):
    def __init__(self):
        BaseView.__init__(self)

    def get(self):
        res = make_response(redirect('/login'))
        res.set_cookie('auth_token', "token", max_age=60 * 60 * 24)
        return res

class Index(BaseView):
    def __init__(self):
        BaseView.__init__(self)

    def get(self):
        if self.check_token(request):
            print('qwrqwr')
            return render_template('index.html')
        else:
            return redirect('/login')
