import telegram.ext 
from telegram.ext import Updater
from bot_token import token, uid

### creating an updater also creates a jobqueue for you which is also linked to the dispatcher
### you should not instantiate a JobQueue on its own unless you have a good reason to do so.
u = Updater(token, use_context=True)

j = u.job_queue

### 3 job queue methods
## job_queue.run_once
## job_queue.run_repeating
## job_queue.run_daily


### add first job to queue by defining a callback function and adding it to the jobqueue
def callback_minute(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id= uid, text = 'one message every minute')

# job_minute = j.run_repeating(callback_minute, interval=60, first=0)
## ignore the type annotations if you are on Python 2

def callback_30(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id=uid, text = '1 message with a 30s delay')

# j.run_once(callback_30, 30)

# job_minute.enabled = False # temporarily disables the job
# job_minute.schedule_removal() # remove the job completely (marked for removal, will be removed once the current interval is over. it will not run again after being marked for removal)


def callback_increasing(context: telegram.ext.CallbackContext):
    job = context.job
    context.bot.send_message(chat_id= uid, text = 'sending msgs with increasing up to 10s, then stops')

    job.interval += 1.0
    if job.interval >= 10:
        job.schedule_removal()
# j.run_repeating(callback_increasing, 1)

# j.start()

########### ADDING JOBS IN RESPONSE TO USER INPUT ########
### all Handler classes can pass the jobqueue into their callback fns if needed. 
## set pass_job_queue = True
## or context keyword argument of Job and retrieve it later as long as the job exists

from telegram.ext import CommandHandler

def callback_alarm(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id = context.job.context, text = 'BEEP BEEP')

def callback_timer(update: telegram.Update, context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id= update.message.chat_id,
    text = 'setting a timer for 1 minute')
    context.job_queue.run_once(callback_alarm, 60, context=update.message.chat_id)
timer_handler = CommandHandler('timer', callback_timer)
u.dispatcher.add_handler(timer_handler)

# j.start()
u.start_polling()