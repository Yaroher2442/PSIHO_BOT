from database import models
import subprocess


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
        res = subprocess.check_output(["pem", "migrate"]).decode().rstrip()
        logger.info("Migrations |" + res)
        return True
    except Exception as e:
        logger.error(f"Migrations | {e}")
        return False


if __name__ == '__main__':
    makemigrations()
