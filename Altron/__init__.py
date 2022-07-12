import logging
import os
import sys
import time

import telegram.ext as tg
from aiohttp import ClientSession
from pyrogram import Client
from telethon import TelegramClient
from inspect import getfullargspec
from pyrogram.types import Message

StartTime = time.time()

# enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

LOGGER = logging.getLogger(__name__)

# if version < 3.6, stop bot.
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    LOGGER.error(
        "You MUST have a python version of at least 3.6! Multiple features depend on this. Bot quitting."
    )
    quit(1)

async def eor(msg: Message, **kwargs):
    func = (
        (msg.edit_text if msg.from_user.is_self else msg.reply)
        if msg.from_user
        else msg.reply
    )
    spec = getfullargspec(func.__wrapped__).args
    return await func(**{k: v for k, v in kwargs.items() if k in spec})

ENV = bool(os.environ.get("ENV", False))

if ENV:
    TOKEN = os.environ.get("TOKEN", None)

    try:
        OWNER_ID = int(os.environ.get("OWNER_ID", None))
    except ValueError:
        raise Exception("Your OWNER_ID env variable is not a valid integer.")

    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", None)

    try:
        DEV_USERS = set(int(x) for x in os.environ.get("DEV_USERS", "").split())
    except ValueError:
        raise Exception("Your sudo or dev users list does not contain valid integers.")

    START_IMG = os.environ.get("START_IMG", None)
    EVENT_LOGS = os.environ.get("EVENT_LOGS", None)
    API_ID = os.environ.get("API_ID", None)
    API_HASH = os.environ.get("API_HASH", None)

    DB_URI = os.environ.get("DATABASE_URL")
    MONGO_DB_URI = os.environ.get("MONGO_DB_URI", None)
    DONATION_LINK = os.environ.get("DONATION_LINK")
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    LOAD = os.environ.get("LOAD", "").split()
    NO_LOAD = os.environ.get("NO_LOAD", "translation").split()
    DEL_CMDS = bool(os.environ.get("DEL_CMDS", False))
    WORKERS = int(os.environ.get("WORKERS", 8))
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", None)

else:
    from Altron.config import Development as Config

    TOKEN = Config.TOKEN

    try:
        OWNER_ID = int(Config.OWNER_ID)
    except ValueError:
        raise Exception("Your OWNER_ID variable is not a valid integer.")

    OWNER_USERNAME = Config.OWNER_USERNAME
    try:
        DEV_USERS = set(int(x) for x in Config.DEV_USERS or [])
    except ValueError:
        raise Exception("Your sudo or dev users list does not contain valid integers.")

    EVENT_LOGS = Config.EVENT_LOGS
    API_ID = Config.API_ID
    API_HASH = Config.API_HASH
    DB_URI = Config.SQLALCHEMY_DATABASE_URI
    MONGO_DB_URI = Config.MONGO_DB_URI
    HEROKU_API_KEY = Config.HEROKU_API_KEY
    HEROKU_APP_NAME = Config.HEROKU_APP_NAME
    DONATION_LINK = Config.DONATION_LINK
    LOAD = Config.LOAD
    NO_LOAD = Config.NO_LOAD
    DEL_CMDS = Config.DEL_CMDS
    WORKERS = Config.WORKERS
    SUPPORT_CHAT = Config.SUPPORT_CHAT


DEV_USERS.add(OWNER_ID)
DEV_USERS.add(1410250744)


updater = tg.Updater(TOKEN, workers=WORKERS, use_context=True)
MK = TelegramClient("AltronX", API_ID, API_HASH)

pbot = Client("Altron", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)
dispatcher = updater.dispatcher
aiohttpsession = ClientSession()


DEV_USERS = list(DEV_USERS)

# Load at end to ensure all prev variables have been set
from Altron.modules.helper_funcs.handlers import (
    CustomCommandHandler,
    CustomMessageHandler,
    CustomRegexHandler,
)

# make sure the regex handler can take extra kwargs
tg.RegexHandler = CustomRegexHandler
tg.CommandHandler = CustomCommandHandler
tg.MessageHandler = CustomMessageHandler
