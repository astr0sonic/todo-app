import logging
import os

import telebot


class TelegramHandler(logging.Handler):
    # def __init__(self, token: str, chat_id: int) -> None:
    #     self.token = token
    #     self.chat_id = chat_id

    def emit(self, log_record: logging.LogRecord) -> None:
        log_msg = self.format(log_record)
        bot_token = os.getenv("BOT_TOKEN", "123")
        bot = telebot.TeleBot(bot_token)
        bot.send_message(123456, log_msg)
