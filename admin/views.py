from flask.views import MethodView
from flask import Response, request, jsonify, send_from_directory, make_response
import uuid
from database.DB_interface import ApiDB


class BaseView(MethodView):
    def __init__(self):
        self.db = ApiDB()

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
        pass

    def post(self):
        print(request.form.get('name'))
        if self.db.auth.registry_user(request.form.get('name'), request.form.get('password')):
            return 'User create'
        else:
            return 'User not be created'


class Login(BaseView):
    def __init__(self):
        BaseView.__init__(self)

    def get(self):
        pass

    def post(self):
        token = self.db.auth.login_user(request.form.get('name'), request.form.get('password'))
        if token:
            res = make_response("Setting a cookie")
            res.set_cookie('auth_token', token, max_age=60 * 60 * 24)
            return res
        else:
            return 'User not logined'


class Index(BaseView):
    def __init__(self):
        BaseView.__init__(self)

    def get(self):
        if self.check_token(request):
            return 'Привет как ты?'
        else:
            return 'no token'
