from flask.views import MethodView
from flask import Response, request, jsonify, send_from_directory, make_response
import uuid
from database.db_worker import AdminDB


class BaseView(MethodView):
    def __init__(self):
        self.db = AdminDB()
    def get_check_token(self,request):
        return request.cookies.get('auth_token')

class Register(BaseView):
    def __init__(self):
        BaseView.__init__(self)

    def post(self):
        print(request.form.get('name'))
        if self.db.registry_user(request.form.get('name'), request.form.get('password')):
            return 'User create'
        else:
            return 'User not be created'


class Login(BaseView):
    def __init__(self):
        BaseView.__init__(self)

    def post(self):
        token=self.db.login_user(request.form.get('name'), request.form.get('password'))
        print(token)
        if token:
            res = make_response("Setting a cookie")
            res.set_cookie('auth_token',token, max_age=60 * 60 * 24)
            return res
        else:
            return 'User not logined'


class Index(BaseView):
    def __init__(self):
        BaseView.__init__(self)

    def get(self):
        if self.get_check_token(request):
            return 'Привет как ты?'
        else:
            return 'asfasf'
