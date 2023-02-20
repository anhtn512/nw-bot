import traceback

from config_bot import *
import telebot
import logging


logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)  # Outputs debug messages to console.

bot = telebot.TeleBot(TEST_TOKEN, parse_mode='Markdown')

groups = [
    '-812674095',
    '-885234662'
]


@bot.channel_post_handler(func=lambda m: True)
def handle_posts(message):
    print('new message - {}'.format(message.message_id))
    for group in groups:
        print('fowword to https://web.telegram.org/k/#-{}', group)
        bot.forward_message(group, message.chat.id, message.message_id)


while True:
    print("start")
    try:
        bot.polling()
    except Exception as e:
        print(traceback.format_exc(e))
