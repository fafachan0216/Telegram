import logging
import random
import telegram

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import User, InlineKeyboardMarkup

updater = Updater("1312704556:AAE23BjzU1lL4SrREPqpdi6WNXSrb1z12f8", use_context=True)
TEMP = 0
List = []

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)



# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help_command(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


#def echo(update, context):
#    """Echo the user message."""
#    text = update.message.text
#    if ( text.lower() =='dllm'):
#        update.message.reply_text('dllm')
#    if ( text.lower() == 'source'):
#        update.message.reply_text('here is the source link :'+
#        'https://connectpolyu-my.sharepoint.com/:f:/g/personal/18022038d_connect_polyu_hk/EoftV3mXfn9Em_HTMLRGWwkBIJHySPhJrKfn237Z5T3rtA?e=sggDys')

def echo(update, context):
    """Echo the user message."""
    if((update.message.text).lower() == 'dllm'):
        #context.bot.delete_message(update.message.message_id,update.message)
        context.bot.deleteMessage(chat_id=update.message.chat.id, message_id=update.message.message_id)
        print(update.message.chat.id)
        print(update.message.from_user.id)
        x = update.message.from_user.id
        is_found =False
        for  i in range(len(List)):
            for j in range(len(List[i])):
                if List[i][j] == x:
                    is_found = True
                    Temp = i
                    break
            if is_found:
                List[Temp][1] += 1
                if(List[Temp][1]%5==0):
                    context.bot.sendMessage(chat_id=update.message.chat.id,text = 'Dont say dllm plz, you speaked '+str(List[Temp][1])+' times ' + str(update.message.from_user.username))
                break
        if not is_found:
            List.append([x,1])
            print('abc')
            print(List)

def main():
    """Start the bot."""

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command , echo))
    

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()