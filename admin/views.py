from flask.views import MethodView
from flask import Response, request, jsonify, send_from_directory, \
    make_response, render_template, redirect, g
import uuid
import copy
from database.DB_interface import DBInterface
from admin.helpers import *


class BaseView(MethodView):
    def __init__(self):
        self.db = DBInterface()
        self.store = store

    def set_notices(self, type, message):
        self.store.notices.append(Notice(type, message))

    def render_with_notices(self, template, **kwargs):
        curent_notifys = copy.copy(self.store.notices)
        self.store.notices.clear()
        return render_template(template, notifys=curent_notifys, **kwargs)

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
            return redirect('/login')
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
            return render_template('index.html')
        else:
            return redirect('/login')


class Bots(BaseView):
    def __init__(self):
        BaseView.__init__(self)

    def get(self):
        if self.check_token(request):
            return render_template('bots.html')
        else:
            return redirect('/login')


class Menus(BaseView):
    def __init__(self):
        BaseView.__init__(self)

    def post(self):
        if all(request.form.to_dict().values()):
            new_status = self.db.Statuses.set_row(descr="new_status")
            if new_status:
                if self.db.Menu.set_row(**request.form.to_dict(), status_id=new_status.id):
                    self.set_notices(Notice.success, 'Меню успешно создано')
                else:
                    self.set_notices(Notice.danger, 'Не удалось создать меню, попробуйте ещё раз')
            else:
                self.set_notices(Notice.danger, 'Не удалось создать меню, попробуйте ещё раз')
            return redirect('/menus')
        else:
            self.set_notices(Notice.danger, 'Не все поля заполнены проверьте ещё раз')
            return redirect('/menus')

    def get(self):
        if self.check_token(request):
            return self.render_with_notices('pages/menus.html', menus=self.db.Menu.get_all(order=self.db.Menu.table.id))
        else:
            return redirect('/login')


class Buttons(BaseView):
    def __init__(self):
        BaseView.__init__(self)

    def post(self):
        up_req = request.form.to_dict()
        if all(up_req.values()):
            for k, v in up_req.items():
                if v.isdigit():
                    up_req[k] = int(v)
                if v == "None":
                    up_req[k] = None
            if self.db.MenuButton.set_row(**up_req):
                self.set_notices(Notice.success, 'Кнопка добавлена')
                return redirect('/buttons')
            else:
                self.set_notices(Notice.danger, 'Не удалось создать кнопку, попробуйте ещё раз')
                return redirect('/buttons')
        else:
            self.set_notices(Notice.danger, 'Не все поля заполнены проверьте ещё раз')
            return redirect('/buttons')

    def get(self):
        if self.check_token(request):
            class OBJ:
                def __init__(self, menu, btn, to_menu):
                    self.menu = menu
                    self.btn = btn
                    self.to_menu = to_menu

            obj_lst = []
            btns = self.db.MenuButton.get_all()
            menus = self.db.Menu.get_all()
            for i in btns:
                for j in menus:
                    if i.menu_id == j:
                        q = OBJ(j, i, to_menu=self.db.Menu.get_by_id(i.to_status))

                        obj_lst.append(q)
            return self.render_with_notices('pages/buttons.html',
                                            buttons=obj_lst,
                                            menus=self.db.Menu.get_all())
        else:
            return redirect('/login')


class Texts(BaseView):
    def __init__(self):
        BaseView.__init__(self)

    def post(self):
        up_req = request.form.to_dict()
        if all(up_req.values()):
            if self.db.TextAnswers.set_row(**up_req):
                self.set_notices(Notice.success, 'Текстовый ответ добавлен')
                return redirect('/texts')
            else:
                self.set_notices(Notice.danger, 'Не удалось создать текстовый ответ, попробуйте ещё раз')
                return redirect('/texts')
        else:
            self.set_notices(Notice.danger, 'Не все поля заполнены проверьте ещё раз')
            return redirect('/texts')

    def get(self):
        if self.check_token(request):
            return self.render_with_notices('pages/texts.html',
                                            texts=self.db.TextAnswers.get_all(order=self.db.TextAnswers.table.id))
        else:
            return redirect('/login')
