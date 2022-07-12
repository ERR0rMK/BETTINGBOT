# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open("{}/Altron/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 123456  # integer value, dont use ""
    API_HASH = "awoo"
    TOKEN = "BOT_TOKEN"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 1410250744  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "TheAltronX"
    SUPPORT_CHAT = "TheAltron"  # Your own group for support, do not add the @
    EVENT_LOGS = (
        -1001777776331
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "something://somewhat:user@hosturl:port/databasename"  # needed for any database modules
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    SPAMWATCH_API = ""  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@TheAltron"

    # OPTIONAL
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    DONATION_LINK = None  # EG, paypal
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
