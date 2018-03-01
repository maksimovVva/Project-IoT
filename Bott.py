import telegram
from telegram.ext import MessageHandler, Filters, Updater, CommandHandler
import pymorphy2
import requests

# import Edison #isParty, getSensorsValue
# edison = Edison.Edison()

morph = pymorphy2.MorphAnalyzer()
Tag = morph.TagClass

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

telegram_api_token = '526860315:AAFrSFROetVrLIQZOG8GhhQyGyAlIYBoef8'
updater = Updater(token=telegram_api_token)
dispatcher = updater.dispatcher

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
    flag = True
    bot.sendChatAction(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    bot.sendMessage(chat_id=update.message.chat_id, text='Party is detected!')


def echo(bot, update):
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