import feedparser
import logging
import telebot
from telebot import types
from config import API_TOKEN

bot = telebot.TeleBot(API_TOKEN)

keyboard = types.ReplyKeyboardMarkup(row_width=4, one_time_keyboard=True)
itembtn1 = types.KeyboardButton('\U0001F621')  # :(
itembtn2 = types.KeyboardButton('\U0001F60F')  # :|
itembtn3 = types.KeyboardButton('\U0001F60C')  # :)
itembtn4 = types.KeyboardButton('\U0001F60B')  # :D
keyboard.add(itembtn1, itembtn2, itembtn3, itembtn4)

keyEmpty = types.ReplyKeyboardMarkup(row_width=2)


@bot.message_handler(commands=["start"])
def cmd_start(m):
    bot.send_message(m.chat.id, 'Как твоё настроение сегодня?', reply_markup=keyboard)


@bot.message_handler(func=lambda message: True, content_types=["text"])
def pub(m):
    if m.text == '\U0001F60B':
        bot.send_message(m.chat.id, 'Хорошего рабочего дня!', reply_markup=keyEmpty)
    elif m.text == '\U0001F60C':
        f = feedparser.parse("https://www.anekdot.ru/rss/export_j.xml")
        i = 0
        for entry in f['entries']:
            if i < 3 and len(entry['description']) < 1500:
                bot.send_message(m.chat.id, entry['description'].replace('<br>', "\n"), reply_markup=keyEmpty, disable_web_page_preview=True)
                i += 1
    elif m.text == '\U0001F60F':
        f = feedparser.parse("https://www.anekdot.ru/rss/export_j.xml")
        i = 0
        for entry in f['entries']:
            if i < 5 and len(entry['description']) < 1500:
                bot.send_message(m.chat.id, entry['description'].replace('<br>', "\n"), reply_markup=keyEmpty, disable_web_page_preview=True)
                i += 1
    elif m.text == '\U0001F621':
        bot.send_message(m.chat.id, 'Подойди пожалуйста в кабинет к HR, посмотрим что можно сделать', reply_markup=keyboard)
    else:
        bot.send_message(m.chat.id, 'Как твоё настроение сегодня?', reply_markup=keyboard)


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
bot.polling(none_stop=True)
print('started')
