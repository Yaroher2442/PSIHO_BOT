from database import models
import subprocess
from database.DB_interface import DBInterface


def makemigrations(logger=None):
    try:
        models_classes = [v for k, v in models.__dict__.items() if "Model:" in str(v)][1:]
    except Exception as e:
        logger.error(f"Migrations | {e}")
        return False
    try:
        for m in models_classes:
            try:
                res = subprocess.check_output(["pem", "add", f"models.{m.__name__}"])
            except:
                logger.info(f"Migrations | models.{m.__name__} already in the watch list")
        res = subprocess.check_output(["pem", "watch"]).decode().rstrip()
        logger.info("Migrations | " + res)
        try:
            res = subprocess.check_output(["pem", "migrate"]).decode().rstrip()
            logger.info("Migrations |" + res)
        except Exception as e:
            logger.error("Migrations |" + f"Can't migrate : {res}")
            db = DBInterface()
        try:
            models.AdminUser.get(models.AdminUser.email == "admin@admin.admin")
        except Exception as e:
            logger.info("Migrations |" + "Admin user not set, try to create one")
            try:
                db.auth.registry_user(name="admin", email="admin@admin.admin", passwrd="admin")
                logger.info("Migrations |" + "Admin user is set")
            except Exception as e:
                logger.info("Migrations |" + f"Admin user setter not work finally : {e}")
                raise e
        except:
            pass
        return True
    except Exception as e:
        logger.error(f"Migrations | {e}")
    return False


if __name__ == '__main__':
    makemigrations()
