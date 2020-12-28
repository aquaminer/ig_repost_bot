from typing import List

from instagram_private_api import Client
from telebot import TeleBot

from .. import config
from ..models import Target


class Storage:
    targets: List[Target] = list()
    api = Client(config["instagram"]["login"], config["instagram"]["password"])
    bot = TeleBot(config["telegram"]["bot_token"])


shared_storage = Storage()
