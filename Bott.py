import telegram
from telegram.ext import MessageHandler, Filters, Updater, CommandHandler
import pymorphy2
import requests

from lxml import objectify, etree, html
import urllib

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
                    text="Hello!\n" +
                         "I'm PartyDetector bot. \n" +
                         "/help - get help about using\n" +
                         "/start - info about me\n" +
                         "/isParty - Check the party\n" +
                         "/loudness - Get value of sound sensor\n" +
                         "/brightness - Get value of light sensor\n" +
                         "/vibration - Get value of vibration sensor\n" +
                         "/allSensors - Get value of all sensors",
                    parse_mode=telegram.ParseMode.HTML)


def help_command(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    bot.sendMessage(chat_id=update.message.chat_id,
                    text="/help - get help about using\n" +
                         "/start - info about me\n" +
                         "/isParty - Check the party\n" +
                         "/loudness - Get value of sound sensor\n" +
                         "/brightness - Get value of light sensor\n" +
                         "/vibration - Get value of vibration sensor\n" +
                         "/allSensors - Get value of all sensors")


def loudness(bot, update):
    flag = True
    bot.sendChatAction(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    bot.sendMessage(chat_id=update.message.chat_id,
                    text=urllib.urlopen('http://localhost:8998/loudness').read().decode('utf-8'))


def brightness(bot, update):
    flag = True
    bot.sendChatAction(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    bot.sendMessage(chat_id=update.message.chat_id,
                    text=urllib.urlopen('http://localhost:8998/brightness').read().decode('utf-8'))


def vibration(bot, update):
    flag = True
    bot.sendChatAction(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    bot.sendMessage(chat_id=update.message.chat_id,
                    text=urllib.urlopen('http://localhost:8998/vibration').read().decode('utf-8'))


def allSensors(bot, update):
    flag = True
    bot.sendChatAction(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    bot.sendMessage(chat_id=update.message.chat_id,
                    text=urllib.urlopen('http://localhost:8998/allSensors').read().decode('utf-8'))


def isParty(bot, update):
    flag = True
    bot.sendChatAction(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    bot.sendMessage(chat_id=update.message.chat_id,
                    text=urllib.urlopen('http://localhost:8998/isParty').read().decode('utf-8'))


def echo(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    encoded_q = update.message.text.lower().encode('utf-8')
    mess = update.message.text
    bot.sendMessage(chat_id=update.message.chat_id, text=str("Mur"))

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help_command))
dispatcher.add_handler(CommandHandler('loudness', loudness))
dispatcher.add_handler(CommandHandler('brightness', brightness))
dispatcher.add_handler(CommandHandler('vibration', vibration))
dispatcher.add_handler(CommandHandler('allSensors', allSensors))
dispatcher.add_handler(CommandHandler('isParty', isParty))
dispatcher.add_handler(MessageHandler(Filters.text, echo))

updater.start_polling()
input()
updater.stop()