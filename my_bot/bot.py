# bot.py
import telebot
from my_bot import bot_utils


class AntiBoredBot:
    def __init__(self, token):
        self.bot = telebot.TeleBot(token)

    def run(self):
        @self.bot.message_handler(commands=['start'])
        def handle_start(message):
            bot_utils.start(self.bot, message)

        @self.bot.message_handler(commands=['help'])
        def handle_help(message):
            bot_utils.help(self.bot, message)

        @self.bot.message_handler(func=lambda message: message.text.startswith("Участників: "))
        def handle_create_activity(message):
            participants = int(message.text.split()[-1])
            if 1 <= participants <= 5:
                bot_utils.create_activity(self.bot, message, participants)
            else:
                bot_utils.input_exception(self.bot, message)

        self.bot.polling()
