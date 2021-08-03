from database.DB_interface import DBInterface


def bot_db_test():
    db = DBInterface()
    db.Statuses.set_row(descr="1")
    db.Statuses.set_row(descr="2")
    db.Statuses.set_row(descr="3")

    db.TextAnswers.set_row(on_status=1, question="/start", answer="Привет, я бот Толя", use_same_texts=False,
                           to_status=2)

    db.Menu.set_row(descr="Первое меню", status=2)
    db.MenuButton.set_row(menu_id=1, text='первая кнопка')
    db.MenuButton.set_row(menu_id=1, text='Вторая кнопка')
    db.MenuButton.set_row(menu_id=1, text='Третья кнопка')

    db.TextAnswers.set_row(on_status=2, question="первая кнопка", answer="Привет, ты нажал кнопку первая кнопка",
                           use_same_texts=False,
                           to_status=3)

    db.Menu.set_row(descr="Второе меню", status=3)
    db.MenuButton.set_row(menu_id=2, text='Кнопка 2.2')
    db.MenuButton.set_row(menu_id=2, text='Назад')

    db.TextAnswers.set_row(on_status=3, question="Назад", answer="Привет, ты нажал кнопку назад",
                           use_same_texts=False,
                           to_status=2)

    db.TextAnswers.set_row(on_status=3, question="Тигр", answer="Привет, ты сказал тигр?",
                           use_same_texts=True,
                           to_status=None)

    db.TextAnswers.set_row(on_status=3, question="Игры с огнём", answer="Привет, ты сказал Игры с огнём?",
                           use_same_texts=True,
                           to_status=None)

    db.Statuses.set_row(descr="4")
    db.Menu.set_row(descr="меню меню", status=4)

    db.TextAnswers.set_row(on_status=2, question="Вторая кнопка", answer="Привет, ты нажал кнопку Вторая кнопка",
                           use_same_texts=False,
                           to_status=4)

    db.MenuButton.set_row(menu_id=3, text='Назад')

    db.TextAnswers.set_row(on_status=4, question="Назад", answer="Привет, ты нажал кнопку назад",
                           use_same_texts=False,
                           to_status=2)
