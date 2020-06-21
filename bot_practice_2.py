from telegram.ext import CommandHandler, MessageHandler, Filters 
from bot_token import token

### creating the updater and dispatcher
from telegram.ext import Updater
updater = Updater(token = token, use_context=True)
dispatcher = updater.dispatcher

### storing list of letters and dictionary into the bot_data
import json
fn = 'all_letters/names.json'
with open(fn, 'r') as fo:
    names = json.load(fo)

fn = 'all_letters/list_of_descriptions.txt'
with open(fn, 'r') as fo:
    descriptions = fo.read()


# def store_letters(update, context):
    # context.bot_data['names'] = names
    # context.bot_data['list_of_descriptions'] = descriptions


### logging to see errors
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


### start function
def start(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = "Starting! \nType '/help' to know the commands!")
    # store data
    context.bot_data['names'] = names
    context.bot_data['descriptions'] = descriptions

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

### list letter names function
def list_letters(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = str(context.bot_data['names']) )

list_handler = CommandHandler('list', list_letters)
dispatcher.add_handler(list_handler)

### list descriptions from a txt file function
def list_descriptions(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = str(context.bot_data['descriptions']) )

desc_handler = CommandHandler('desc', list_descriptions)
dispatcher.add_handler(desc_handler)

### read a letter function
fn = 'practice data/practice_dict.json'
with open(fn, 'r') as fo:
    letter_dict = json.load(fo)


def read(update, context):
    key = update.message.text.partition(' ')[2]

    try:
        letter_to_read = letter_dict[key]
        update.message.reply_text(letter_to_read)
    except KeyError:
        update.message.reply_text("no such letter found")

read_handler = CommandHandler('read',read)
dispatcher.add_handler(read_handler)

def help(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = "/list: list all the letters \n/read letter <number>: fetches the full letter")
help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)

updater.start_polling()
updater.idle()