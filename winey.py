import os
from telegram.ext import Updater, CommandHandler

TOKEN = "358433791:AAGovZQX0V8iOa1050MiRGtt2SGTHX4x9Xs"

def start(bot, update):
    update.message.reply_text('Hello World!')

def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

if __name__ == "__main__":
    PORT = int(os.environ.get('PORT', '5000'))
    updater = Updater(TOKEN)
    # add handlers
    updater.start_webhook(listen="0.0.0.0",
                          port=PORT,
                          url_path=TOKEN)
    updater.bot.setWebhook("https://wineyapp.herokuapp.com/" + TOKEN)
    updater.idle()