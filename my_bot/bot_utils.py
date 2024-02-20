import telebot

from translator import translator
from api.boredapi import get_response
from dto.ActivityDTO import ActivityDTO


def start(tg_bot, message):
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2)
    buttons_row1 = []
    buttons_row2 = []

    for i in range(1, 3):
        buttons_row1.append(telebot.types.InlineKeyboardButton(text=f"Участників: {i}"))
    for i in range(3, 6):
        buttons_row2.append(telebot.types.InlineKeyboardButton(text=f"Участників: {i}"))

    keyboard.row(*buttons_row1)
    keyboard.row(*buttons_row2)

    tg_bot.send_message(message.chat.id, "Привіт! Я - Anti-Bored Bot. "
                                         "Надішли мені кількість участників і я згенерую ідею, як провести час\n"
                                         "Напиши /help щоб дізнатися про мене!", reply_markup=keyboard)


def help(tg_bot, message):
    tg_bot.send_message(message.chat.id,
                        "Я Anti-Bored Bot. Створений для того, щоб підкинути ідею як провести час).\n"
                        "Напиши /start щоб почати!")


def create_activity(tg_bot, message, participants):
    try:
        data = get_response(participants)
        activity = ActivityDTO.from_json(data)
        tg_bot.send_message(message.chat.id, translator.translate_to_ukr(activity.activity))
    except Exception as e:
        tg_bot.send_message(message.chat.id, "Погане інтернет з'єднання, спробуйте пізніше!")


def input_exception(tg_bot, message):
    tg_bot.send_message(message.chat.id, "Не обманюй мене:)\nДивись, що ти вводиш!")
