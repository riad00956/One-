
import os
import logging
from logging.handlers import RotatingFileHandler


# Get a bot token from botfather
TG_BOT_TOKEN = os.environ.get("8135019248:AAErZL0HgDa0kzfLTHRQB-afvKDuQ8Fsn3s", "")

# Get from my.telegram.org (or @UseTGXBot)
APP_ID = int(os.environ.get("23732434", ""))

# Get from my.telegram.org (or @UseTGXBot)
API_HASH = os.environ.get("0175fda21b337c9b76722e8decab67ab", "")

# Generate a user session string 
TG_USER_SESSION = os.environ.get("158702140", "")

# ID of Channel from which the bot shoul search files
MAINCHANNEL_ID = os.environ.get("-1002333573799", "")




TG_BOT_SESSION = os.environ.get("TG_BOT_SESSION", "bot")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
LOG_FILE_NAME = "filterbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

