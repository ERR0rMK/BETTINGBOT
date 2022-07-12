from Altron.modules.helper_funcs import BASE, SESSION
from sqlalchemy import (
    Column,
    String,
    UnicodeText,
)

class Chats(BASE):
    __tablename__ = "chats"
    chat_id = Column(String(14), primary_key=True)
    chat_name = Column(UnicodeText, nullable=False)

    def __init__(self, chat_id, chat_name):
        self.chat_id = str(chat_id)
        self.chat_name = chat_name

    def __repr__(self):
        return "<Chat {} ({})>".format(self.chat_name, self.chat_id)

Chats.__table__.create(checkfirst=True)

def get_all_chats():
    try:
        return SESSION.query(Chats).all()
    finally:
        SESSION.close()
