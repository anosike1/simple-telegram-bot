import constants as Key
import responses as R
from telegram.ext import *
updater = Updater (Key.BOT_API, use_context = True)
dp = updater.dispatcher


print ("Bot started....")

def start (update, context):
    update.message.reply_text ("Type something - that actually makes sense please.")

def help (update, context):
    update.message.reply_text ("***\n/start - Thanks for using this bot.\n/help - Where we are right now.\n/content - About this bot...\n***")

def handle (update, context):
    text = str (update.message.text).lower()
    response = R.sample_responses (text)
    update.message.reply_text (response)
    
def error (update, context):
    print (f"Update {update} caused error {context.error}")

def main ():
    dp.add_handler(CommandHandler ("start", start))
    dp.add_handler(CommandHandler ("help", help))
    dp.add_handler(MessageHandler (Filters.text, handle))  
    dp.add_error_handler (error)
    
    updater.start_polling (0)
    updater.idle()


main()