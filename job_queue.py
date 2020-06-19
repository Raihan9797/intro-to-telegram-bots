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

job_minute = j.run_repeating(callback_minute, interval=60, first=0)
## ignore the type annotations if you are on Python 2

def callback_30(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id=uid, text = '1 message with a 30s delay')

j.run_once(callback_30, 30)

# job_minute.enabled = False # temporarily disables the job
# job_minute.schedule_removal() # remove the job completely (marked for removal, will be removed once the current interval is over. it will not run again after being marked for removal)


def callback_increasing(context: telegram.ext.CallbackContext):
    job = context.job
    context.bot.send_message(chat_id= uid, text = 'sending msgs with increasing up to 10s, then stops')

    job.interval += 1.0
    if job.interval >= 10:
        job.schedule_removal()
j.run_repeating(callback_increasing, 1)

j.start()