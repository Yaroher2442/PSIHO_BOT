from fuzzywuzzy import fuzz
from database.DB_interface import ApiDB


class BotDBLogic(ApiDB):
    def __init__(self):
        ApiDB.__init__(self)

    def create_answr_meaasge(self, message):
        user_state = self.TgClient.get_status(message.from_user.id)
        current_buttons = self.Menu.get_all_buttons(self.Menu.get_by_id(user_state))
        answr = None
        if message.text not in [btn_text.text for btn_text in current_buttons]:
            for txt in self.TextAnswers.get_all():
                if message.text == txt.question:
                    answr = txt.answer
                else:
                    if txt.use_same_texts and fuzz.WRatio(txt.question, message.text) > 80:
                        answr = txt.answer
                    else:
                        continue
            if answr:
                return answr
            else:
                return "cant answering"
        else:
            for btn in current_buttons:
                if message.text == btn.text:
                    if btn.next_menu != 0:
                        next = self.Menu.get_all_buttons(self.Menu.get_by_id(btn.next_menu))
                        self.TgClient.set_status(message.from_user.id, status=user_state)
                        return next
                    else:
                        answr = btn.text
                else:
                    continue
            if answr:
                return answr
            else:
                return "cant answering"


if __name__ == '__main__':
    pass
