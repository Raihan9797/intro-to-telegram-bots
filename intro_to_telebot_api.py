import telegram
# import bot_token.token # does not work
from bot_token import token

bot = telegram.Bot(token)

print(bot.get_me()) # check whether this is actually your bot!

