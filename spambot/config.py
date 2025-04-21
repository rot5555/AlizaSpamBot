import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "25782653"))
    API_HASH = os.environ.get("API_HASH", "ac9b63ba0ac9ecdbbdc1a07373a4acfe")
    BOT_TOKEN1 = os.environ.get("BOT_TOKEN1", "7899033434:AAHpIWmOSgqmhNXCVLP7kxZiOzHqK6b7YU0")
    BOT_TOKEN2 = os.environ.get("BOT_TOKEN2", "5748926642:AAE6knIAlbBaSst9wD7FnanOlyUZBIJlRB8")
    BOT_TOKEN3 = os.environ.get("BOT_TOKEN3", "5529110275:AAEJPsspJmI5fYNl2fvQgFkxxEIhKRHP_HI")
    BOT_TOKEN4 = os.environ.get("BOT_TOKEN4", "5717105219:AAExAPCdl10DLsUyruuMwh1XrctRqeI8DW4")
    BOT_TOKEN5 = os.environ.get("BOT_TOKEN5", "5545960274:AAHtHGP_cOwiKy1D0bGL3RCisdrxPvHH7JE")
    OWNER_ID = int(os.environ.get("OWNER_ID", "8035192866"))
    OWNER_NAME = os.environ.get("OWNER_NAME", "Deep")
    OWNER_USERNAME =os.environ.get("OWNER_USERNAME", "Itz_me_AR")
    CO_OWNER_ID = set(int(x) for x in os.environ.get("CO_OWNER_ID", "6658689373").split())
    SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "1832668205").split())
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_ID", None)
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
    DISPLAY_PIC = os.environ.get("DISPLAY_PIC", "https://graph.org/file/99eb35e73777775a57528.jpg")
    BIO_MSG =  os.environ.get("BIO_MSG", "Maa Chudao Shavvu and Shekhu")
