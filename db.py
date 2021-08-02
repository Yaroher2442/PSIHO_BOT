from database import DB_interface
from database import models

if __name__ == '__main__':
    # DB_interface.create_db()
    DB_interface.create_one_table(models.AnswersStatistic)
