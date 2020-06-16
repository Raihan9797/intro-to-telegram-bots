# obtained from: https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions-%E2%80%93-Your-first-Bot

# Updater: continuously fetches new updates from tele and passes them to Dispatcher.
# creating Updaters also creates a Dispatcher linked by a Queue.
# We handler different registers of handlers using Dispatchers which sorts updates fetched by Updater according to your specified handlers and deliver them to a callback function you defined.

token = '1215169390:AAHV5H5AxyL56zWF4_hlB3FK47Py0UEZy4A'

from telegram.ext import Updater

updater = Updater(token, use_context=True)
# use context = True for better backwards compatibility

dispatcher = updater.dispatcher

import logging
logging.basicConfig(format="%(asctime)s = %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text= "i'm a bot pls talk to me!!! am i alive?")


# we want this fn to be called everytime the bot receives a tele msg that contins '/start' commd. So we use CommandHandler

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# updater.start_polling()



################ ADDING THE MESSAGEHANDLER ##############
# added a handler that listens to TEXT and echoes them
def echo(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = update.message.text)

from telegram.ext import MessageHandler, Filters

# created a MessageHandler
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
# added it to the dispatcher
dispatcher.add_handler(echo_handler)

updater.start_polling()



########### ADDING CAPS FUNCTIONALITY ##########
def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id = update.effective_chat.id, text = text_caps)

# with this alone, you are able to write /caps <type your text> and it will repeat your text in caps!
caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)




########## INLINE FUNCTIONALITY #############
# inline functionality is the added functions you get while you are typing!! You have a bot without going to message him directly!
# examples of this are like the @gif, @youtube

from telegram import InlineQueryResultArticle, InputTextMessageContent

def inline_caps(update, context):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id = query.upper(),
            title = 'Caps',
            input_message_content = InputTextMessageContent(query.upper())
            )
    )
    context.bot.answer_inline_query(update.inline_query.id, results)

from telegram.ext import InlineQueryHandler
inline_caps_handler = InlineQueryHandler(inline_caps)
dispatcher.add_handler(inline_caps_handler)
# the normal bot still works too!
# however, if you type 'hello!' it only gives 'HELLO'



