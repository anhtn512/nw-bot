from datetime import datetime

from config_bot import *
import telebot
import logging


logger = telebot.logger
telebot.logger.setLevel(logging.NOTSET)  # Outputs debug messages to console.

bot = telebot.TeleBot(TEST_TOKEN, parse_mode='Markdown')

groups = [
    '-1001527481292', #NEARisNOW
    '-1001721312529', #NearMedia
    '-1001255242947', #merchantsofnear
    '-1001375169474', #nearindia
    #'@nearinsider_chat',
    #'@nearity',
    '-1001313395854', #nearvietnamofficial
    '-620864296', #NEARWEEK Agents
    '-1001430242011', #Shitzu Apes
    '-1001848978670', #$Near Chill&Shill
    '-1001501401334', #nearsf
    '-1001359461894', #cryptonear
    #'-1001720689268', #nearnyc
]

@bot.channel_post_handler(func=lambda m: True)
def handle_posts(message):
    print('new message - {}'.format(message.message_id))
    for group in groups:
        try:
            print('sending to {}'.format(group))
            bot.forward_message(group, message.chat.id, message.message_id)
        except Exception as e:
            print('======================')
            print(datetime.now())
            print('group: {}'.format(group))
            print(f'message: {str(e)}')
while True:
    print("start")
    try:
        bot.polling()
    except Exception as e:
        print(f'message: {str(e)}')
