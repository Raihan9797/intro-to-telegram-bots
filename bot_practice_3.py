from telegram.ext import CommandHandler, MessageHandler, Filters 
from bot_token import token

### creating the updater and dispatcher
from telegram.ext import Updater
updater = Updater(token = token, use_context=True)
dispatcher = updater.dispatcher

### storing list of letters and dictionary into the bot_data
fn = 'all_letters/names.json'
import json
with open(fn, 'r') as fo:
    names = json.load(fo)

### logging to see errors
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


### start function
def start(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = "Starting bot practice 3!")
    # store data
    context.bot_data['names'] = names 

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


### list descriptions from a txt file function
def list_names_and_descriptions(update, context):
    for i in range(0, 20):
        context.bot.send_message(chat_id = update.effective_chat.id, text = str(context.bot_data['names'][i]) )


list_handler = CommandHandler('list', list_names_and_descriptions)
dispatcher.add_handler(list_handler)

### read a letter function
def read(update, context):
    key = update.message.text.partition(' ')[2]

    try:
        letter_to_read = context.bot_data['letters_dict'][key]
        update.message.reply_text(letter_to_read)
    except KeyError:
        update.message.reply_text("no such letter found")

read_handler = CommandHandler('read',read)
dispatcher.add_handler(read_handler)


updater.start_polling()
updater.idle()