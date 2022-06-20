from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

updater = Updater('5439013352:AAEPdX_bXZDQ3CZsekfBREB2MC2N-BY1PyI',use_context=True)

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Enter the text you want to show to the user whenever they start the bot")

def youtube_url(update: Update, context: CallbackContext):
    update.message.reply_text("Youtube Link => \
        https://www.youtube.com/watch?v=HaEmIakO7f4")

def replit_url(update: Update, context: CallbackContext):
    update.message.reply_text("ReplIt Link => \
        https://replit.com/@AnwitaDivya/Bot#main.py")


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('youtube', youtube_url))
updater.dispatcher.add_handler(CommandHandler('replit', replit_url))
updater.start_polling()