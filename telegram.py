import telegram
from telegram.ext import MessageHandler, Filters, Updater, CommandHandler
import pymorphy2
import requests

import Edison #isParty, getSensorsValue
edison = Edison.Edison()

morph = pymorphy2.MorphAnalyzer()
Tag = morph.TagClass

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

telegram_api_token = '526860315:AAFrSFROetVrLIQZOG8GhhQyGyAlIYBoef8'
updater = Updater(token=telegram_api_token)
dispatcher = updater.dispatcher

from matplotlib import pyplot as plt


def plot_graph(memlist, title, ylabel):
    f, ax = plt.subplots(figsize=[4, 2])
    tmperiod = range(24)
    ax = plt.subplot(111)
    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)

    plt.xlabel('Time')
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid()
    plt.plot(tmperiod, memlist, 'b')
    plt.savefig('/tmp/graph.png')
    plt.close()
    f = open('/tmp/graph.png', 'rb')
    return f

def start(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    bot.sendMessage(chat_id=update.message.chat_id,
                    text="Hello",
                    parse_mode=telegram.ParseMode.HTML)

def help_command(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    bot.sendMessage(chat_id=update.message.chat_id,
                    text="Mur")


def alarm(bot, update):
    flag = True  # тут будет функция
    bot.sendChatAction(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    bot.sendMessage(chat_id=update.message.chat_id, text='Party is detected!')


def echo(bot, update):  # ЭТО ПОКА ТОЛЬКО ПРИМЕР, БУДЕТ БОЛЬШЕ ЗАПРОСОВ
    bot.sendChatAction(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    encoded_q = update.message.text.lower().encode('utf-8')
    mess = update.message.text
    bot.sendMessage(chat_id=update.message.chat_id,
                    text=str(requests.get('0.0.0.0:8998/loudness')))

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help_command))
dispatcher.add_handler(CommandHandler('alarm', alarm))
dispatcher.add_handler(MessageHandler(Filters.text, echo))

updater.start_polling()