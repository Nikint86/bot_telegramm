import os

from dotenv import load_dotenv
from pytimeparse import parse

import ptbot


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def notify_progress(chat_id,question):
    message_id = bot.send_message(chat_id, "\nЗапускаю Таймер...\n")
    bot.create_countdown(parse(question), notify,chat_id = chat_id,message_id = message_id,question = question)
    bot.create_timer(parse(question), choose, chat_id = chat_id)


def choose(chat_id):
    bot.send_message(chat_id,"Время вышло!")


def notify(secs_left, chat_id, message_id,question):
    bot.update_message(chat_id, message_id, "\nОсталось {} секунд!\n".format(secs_left) + render_progressbar(parse(question),secs_left))


if __name__ == '__main__':
    load_dotenv()
    my_secret = os.getenv('TELEGRAM_TOKEN')
    TG_TOKEN = my_secret
    TG_CHAT_ID = '1248233669'
    bot = ptbot.Bot(TG_TOKEN)
    bot.reply_on_message(notify_progress)
    bot.run_bot()







