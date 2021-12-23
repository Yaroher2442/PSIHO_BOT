from flask.views import MethodView
from flask import Response, request, jsonify, send_from_directory, \
    make_response, render_template, redirect, g
import uuid
from playhouse.shortcuts import model_to_dict
import copy

from telegram.ext import ExtBot

from config_.conf import conf
from loguru import logger

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
        return render_template(template, notifys=curent_notifys, base_url=conf.server_conf.base_url, **kwargs)

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
        return self.render_with_notices('register.html')

    def post(self):
        if self.db.auth.registry_user(request.form.get('name'), request.form.get('email'),
                                      request.form.get('password')):
            return redirect(f'{conf.server_conf.base_url}/login')
        else:
            return self.render_with_notices('register.html')


class Login(BaseView):
    def __init__(self):
        BaseView.__init__(self)

    def get(self):
        return self.render_with_notices('login.html')

    def post(self):
        token = self.db.auth.login_user(request.form.get('email'), request.form.get('password'))
        if token:
            res = make_response(redirect(f'{conf.server_conf.base_url}/statistic'))
            res.set_cookie('auth_token', token, max_age=60 * 60 * 24)
            return res
        else:
            self.set_notices(Notice.danger, 'User not found')
            return redirect(f'{conf.server_conf.base_url}/login')


class Logout(BaseView):
    def __init__(self):
        BaseView.__init__(self)

    def get(self):
        res = make_response(redirect(f'{conf.server_conf.base_url}/login'))
        res.set_cookie('auth_token', "token", max_age=60 * 60 * 24)
        return res


class Index(BaseView):
    def __init__(self):
        BaseView.__init__(self)

    def get(self):
        return redirect(f'{conf.server_conf.base_url}/statistic')


class Bots(BaseView):
    def __init__(self):
        BaseView.__init__(self)

    def get(self):
        if self.check_token(request):
            return self.render_with_notices('pages/bots.html')
        else:
            return redirect(f'{conf.server_conf.base_url}/login')


class TgUsers(BaseView):
    def __init__(self):
        BaseView.__init__(self)

    def get(self):
        return self.render_with_notices('pages/users.html', users=self.db.get_users())


class Menus(BaseView):
    def __init__(self):
        BaseView.__init__(self)

    def post(self):
        form = request.form.to_dict()
        if all(form.values()):
            flag = form['flag'].split('_')
            form.pop('flag')
            if flag[0] == "update":
                if self.db.Menu.update(flag[1], **form):
                    self.set_notices(Notice.success, 'Меню успешно обновлено')
                else:
                    self.set_notices(Notice.danger, 'Не удалось обновить меню, попробуйте ещё раз')
                return redirect(f'{conf.server_conf.base_url}/menus')
            elif flag[0] == "insert":
                new_status = self.db.Statuses.set_row(descr="new_status")
                if new_status:
                    if self.db.Menu.set_row(**request.form.to_dict(), status_id=new_status.id):
                        self.set_notices(Notice.success, 'Меню успешно создано')
                    else:
                        self.set_notices(Notice.danger, 'Не удалось создать меню, попробуйте ещё раз')
                else:
                    self.set_notices(Notice.danger, 'Не удалось создать меню, попробуйте ещё раз')
                return redirect(f'{conf.server_conf.base_url}/menus')
        else:
            self.set_notices(Notice.danger, 'Не все поля заполнены проверьте ещё раз')
            return redirect(f'{conf.server_conf.base_url}/menus')

    def get(self):
        if self.check_token(request):
            return self.render_with_notices('pages/menus.html', menus=self.db.Menu.get_all(order=self.db.Menu.table.id))
        else:
            return redirect(f'{conf.server_conf.base_url}/login')


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
            flag = up_req['flag'].split('_')
            up_req.pop('flag')
            if flag[0] == "update":
                if self.db.MenuButton.update(flag[1], **up_req):
                    self.set_notices(Notice.success, 'Кнопка успешно обновлена')
                else:
                    self.set_notices(Notice.danger, 'Не удалось обновить кнопку, попробуйте ещё раз')
                return redirect(f'{conf.server_conf.base_url}/buttons')
            elif flag[0] == "insert":
                if self.db.MenuButton.set_row(**up_req):
                    self.set_notices(Notice.success, 'Кнопка добавлена')
                    return redirect(f'{conf.server_conf.base_url}/buttons')
                else:
                    self.set_notices(Notice.danger, 'Не удалось создать кнопку, попробуйте ещё раз')
                    return redirect(f'{conf.server_conf.base_url}/buttons')
        else:
            self.set_notices(Notice.danger, 'Не все поля заполнены проверьте ещё раз')
            return redirect(f'{conf.server_conf.base_url}/buttons')

    def get(self):
        if self.check_token(request):
            class OBJ:
                def __init__(self, menu, btn, to_menu):
                    self.menu = menu
                    self.btn = btn
                    self.to_menu = to_menu

            obj_lst = []
            btns = self.db.MenuButton.get_all(order=self.db.MenuButton.table.id)
            menus = self.db.Menu.get_all(order=self.db.Menu.table.id)
            for i in btns:
                for j in menus:
                    if i.menu_id == j:
                        logger.debug(i.to_status)
                        q = OBJ(j, i, to_menu=self.db.Menu.get_by_id(i.to_status))
                        obj_lst.append(q)
            return self.render_with_notices('pages/buttons.html',
                                            buttons=obj_lst,
                                            menus=self.db.Menu.get_all())
        else:
            return redirect(f'{conf.server_conf.base_url}/login')


class Texts(BaseView):
    def __init__(self):
        BaseView.__init__(self)

    def post(self):
        up_req = request.form.to_dict()
        if all(up_req.values()):
            flag = up_req['flag'].split('_')
            up_req.pop('flag')
            if flag[0] == "update":
                if self.db.TextAnswers.update(flag[1], **up_req):
                    self.set_notices(Notice.success, 'Текст успешно обновлен')
                else:
                    self.set_notices(Notice.danger, 'Не удалось обновить текст, попробуйте ещё раз')
                return redirect(f'{conf.server_conf.base_url}/texts')
            elif flag[0] == "insert":
                if self.db.TextAnswers.set_row(**up_req):
                    self.set_notices(Notice.success, 'Текстовый ответ добавлен')
                    return redirect(f'{conf.server_conf.base_url}/texts')
                else:
                    self.set_notices(Notice.danger, 'Не удалось создать текстовый ответ, попробуйте ещё раз')
                    return redirect(f'{conf.server_conf.base_url}/texts')
        else:
            self.set_notices(Notice.danger, 'Не все поля заполнены проверьте ещё раз')
            return redirect(f'{conf.server_conf.base_url}/texts')

    def get(self):
        if self.check_token(request):
            return self.render_with_notices('pages/texts.html',
                                            texts=self.db.TextAnswers.get_all(order=self.db.TextAnswers.table.id))
        else:
            return redirect(f'{conf.server_conf.base_url}/login')


class Commands(BaseView):
    def __init__(self):
        BaseView.__init__(self)

    def post(self):
        up_req = request.form.to_dict()
        if all(up_req.values()):
            flag = up_req['flag'].split('_')
            up_req.pop('flag')
            if flag[0] == "update":
                if self.db.Commands.update(flag[1], **up_req):
                    self.set_notices(Notice.success, 'Команда успешно обновленa')
                else:
                    self.set_notices(Notice.danger, 'Не удалось обновить команду, попробуйте ещё раз')
                return redirect(f'{conf.server_conf.base_url}/commands')
            elif flag[0] == "insert":
                if self.db.Commands.set_row(**up_req):
                    self.set_notices(Notice.success, 'Команда успешно добавлена')
                    return redirect(f'{conf.server_conf.base_url}/commands')
                else:
                    self.set_notices(Notice.danger, 'Не удалось создать комманду, попробуйте ещё раз')
                    return redirect(f'{conf.server_conf.base_url}/commands')
        else:
            self.set_notices(Notice.danger, 'Не все поля заполнены проверьте ещё раз')
            return redirect(f'{conf.server_conf.base_url}/commands')

    def get(self):
        if self.check_token(request):
            class OBJ:
                def __init__(self, menu, commands):
                    self.menu = menu
                    self.commands = commands

            obj_lst = []
            commands = self.db.Commands.get_all()
            menus = self.db.Menu.get_all()
            for i in commands:
                for j in menus:
                    if i.to_status == j.status:
                        q = OBJ(j, i)
                        obj_lst.append(q)
            return self.render_with_notices('pages/commands.html',
                                            commands=obj_lst,
                                            menus=self.db.Menu.get_all())
        else:
            return redirect(f'{conf.server_conf.base_url}/login')


class Delete(BaseView):
    redirect_data = {"TextAnswers": f'{conf.server_conf.base_url}/texts',
                     "Menu": f'{conf.server_conf.base_url}/menus',
                     "MenuButton": "/ru/buttons",
                     "Commands": "/ru/commands",
                     "UserModer": "/ru/moderations"}

    def __init__(self):
        BaseView.__init__(self)

    def get(self, table, item_id):
        if getattr(self.db, table).delete_row(item_id):
            self.set_notices(Notice.success, 'Успешно удалено')
            return redirect(self.redirect_data[table])
        else:
            self.set_notices(Notice.danger, 'Не удалось удалить объект')
            return redirect(self.redirect_data[table])


class Statistic(BaseView):
    redirect_data = {"TextAnswers": f'{conf.server_conf.base_url}/texts',
                     "Menu": f'{conf.server_conf.base_url}/menus',
                     "MenuButton": "/ru/buttons",
                     "Commands": "/ru/commands",
                     "UserModer": "/ru/moderations"}

    def __init__(self):
        BaseView.__init__(self)

    def get(self):
        if self.check_token(request):
            return self.render_with_notices('pages/statistic.html',
                                            statistic=self.db.AnswersStatistic.get_all(
                                                order=self.db.AnswersStatistic.table.id))
        else:
            return redirect(f'{conf.server_conf.base_url}/login')


class Moderation(BaseView):
    redirect_data = {"TextAnswers": f'{conf.server_conf.base_url}/texts',
                     "Menu": f'{conf.server_conf.base_url}/menus',
                     "MenuButton": "/ru/buttons",
                     "Commands": "/ru/commands",
                     "UserModer": "/ru/moderations"}

    def __init__(self):
        BaseView.__init__(self)

    def get(self):
        if self.check_token(request):
            return self.render_with_notices('pages/moderations.html',
                                            moder_data=self.db.UserModer.get_all(order=self.db.UserModer.table.id))
        else:
            return redirect(f'{conf.server_conf.base_url}/login')

    def post(self):
        up_req = request.form.to_dict()
        flag = up_req['flag'].split('_')
        up_req.pop('flag')
        if flag[0] == "update":
            logger.debug(up_req)
            if self.db.UserModer.update(flag[1], **up_req):
                self.set_notices(Notice.success, 'Ответ успешно обновлен')
            else:
                self.set_notices(Notice.danger, 'Не удалось обновить ответ, попробуйте ещё раз')
            return redirect(f'{conf.server_conf.base_url}/moderations')


class AproveModeration(BaseView):
    def __init__(self):
        BaseView.__init__(self)

    def post(self, item_id):
        # if self.db.TextAnswers.set_row()
        to_table = self.db.UserModer.get_by_id(item_id)
        if self.db.TextAnswers.set_row(question=to_table.question, answer=to_table.answer):
            to_table.accepted = True
            to_table.save()
            self.set_notices(Notice.success, "Успешно согласовано")
        else:
            self.set_notices(Notice.success, "Успешно согласовано")
        return redirect("/ru/moderations")


class UserModerPage(BaseView):
    def __init__(self):
        BaseView.__init__(self)

    def get(self):
        return self.render_with_notices('pages/user_moder.html',
                                        statistic=self.db.AnswersStatistic.get_all(
                                            order=self.db.AnswersStatistic.table.id))

    def post(self):
        form = request.form.to_dict()
        if self.db.UserModer.set_row(**form, accepted=False, deleted=False):
            self.set_notices(Notice.success, "Успешно отправлено на модерацию")
        else:
            self.set_notices(Notice.danger, "Не удалось согласовать объект объект")
        return redirect(f'{conf.server_conf.base_url}/request_answer')
        # self.db.UserModer.get_all(order=self.db.UserModer.table.id)
        # self.set_notices()


class NotificationsPage(BaseView):
    tg_bot: ExtBot = None

    def __init__(self):
        BaseView.__init__(self)

    def get(self):
        return self.render_with_notices('pages/notifications.html')

    def post(self):
        notification_text = request.form.to_dict()["notification"]
        if not notification_text:
            self.set_notices(Notice.warning, "Пустая строка отправки сообщения")
        users = self.db.get_users()
        exceptions = 0
        for user in users:
            try:
                self.tg_bot.send_message(user.tg_id, notification_text)
            except Exception as e:
                logger.warning(f"Can't send notify to {user.username}, cause: {e}")
                exceptions += 1
        if exceptions != 0:
            self.set_notices(Notice.warning,
                             f"{len(users) - exceptions} из {len(users)} ваших пользователей получили ваше сообщение, остальные закрыли диалог с ботом ")
        else:
            self.set_notices(Notice.success, f"{len(users)} пользователей получили ваше сообщение ")
        return redirect(f'{conf.server_conf.base_url}/notifications')
        # self.db.UserModer.get_all(order=self.db.UserModer.table.id)
        # self.set_notices()
