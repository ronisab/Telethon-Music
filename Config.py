import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "2156559"))
    API_HASH = os.environ.get("API_HASH", "fea80bd8ede83bcb1a3290c43e5691bd")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "2138748531:AAHfB17Vd1KZVsUqhblKcIQuHMH9NQRWVbU")
    STRING_SESSION = os.environ.get("STRING_SESSION", "")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@kylieverzosabot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "1492235056")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
