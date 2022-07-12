from time import time, sleep
from Altron import pbot, OWNER_ID
from telethon import events
from pyrogram import filters


def BetAI():
    pass


@pbot.on_message(filters.command("setbet"))
async def setbet(event):
    pass


@pbot.on_message(filters.command("startbet"))
async def start(event):
    if event.sender_id == OWNER_ID:
        if event.is_private:
            InitialTime = time()
            while True:
                if time() - InitialTime >= 70:
                    InitialTime = time()
                BetAI()
