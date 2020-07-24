# My introduction to Telegram Bots using Python

## Why did I do this?
I created this repository as a way to practice the [python-telegram-bot API](https://github.com/python-telegram-bot/python-telegram-bot).

This is part of a personal project to make a telegram bot and the other part of this practice is from [Texts From a Stoic](https://github.com/Raihan9797/Texts-from-a-Stoic)

## What did I learn from this?
1. Creating a basic bot that makes use of Updaters, Handlers and Dispatchers. Also the use of polling to take inputs from users
With these basic tools, the bot can take in commands (eg. /help) and message (eg. Bot replies if you say "hello!")

2. Storing and accessing data in the bot.
I was able to store .txt files as well as json lists and dictionaries that could be used by the bot to interact with users. With this, I was able to ask the bot to send me a specific letter that it has stored in its own data.

3. Job Queues.
This allows certain operations to be done at certain time intervals (per day, per minute) depending on the operation required. With this, I can allow my bot to prompt users with daily texts etc.

4. Inline Keyboard
The Bot can be used from within your keyboard ie. no need to chat with the Bot! An example of this would be typing "@youtube" which will allow you to search for youtube videos without leaving Telegram. I was able to use it to capitalise my messages automatically.

5. Webhooks to host my Bot
Webhooks is a more efficient way of waiting for input from users as compared to polling(). Using this info, I was able to host my bot on Heroku.

6. name == main for automatic startup of the bot.
Again, hosting a bot has different issues as compared to running it by yourself. For one, the bot shuts down when you host it on a free domain. By using this method, the bot is able to automatically load its data so the user does not have to keep restart the bot using (/start)