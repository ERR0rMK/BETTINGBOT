from time import sleep

from telegram import TelegramError, Update
from telegram.ext import (
    CallbackContext,
    CommandHandler,
    run_async,
)

import Altron.modules.helper_funcs.users_sql as sql
from Altron import dispatcher
from Altron.modules.helper_funcs.chat_status import dev_plus


@run_async
@dev_plus
def broadcast(update: Update, context: CallbackContext):
    chats = sql.get_all_chats() or []
    for chat in chats:
        try:
            context.bot.sendMessage(
                int(chat.chat_id),
                "BETTING STARTED",
                parse_mode="MARKDOWN",
                disable_web_page_preview=True,
            )
            sleep(0.1)
        except TelegramError:
            pass

__help__ = ""

BROADCAST_HANDLER = CommandHandler(
    ["broadcast", "broadcastusers", "broadcastgroups"], broadcast
)

dispatcher.add_handler(BROADCAST_HANDLER)

__handlers__ = [BROADCAST_HANDLER]
