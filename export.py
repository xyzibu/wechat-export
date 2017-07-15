#!/usr/bin/env python
# encoding: utf-8

import os
import time
import datetime
import ConfigParser
from wxpy import *

cf = ConfigParser.ConfigParser()
cf.read('wechat.conf')
path = cf.get('wechat', 'path')
group_name = cf.get('wechat', 'group_name').decode('utf-8')
hour_conf = cf.getint('wechat', 'hour')

bot = Bot(cache_path=True, console_qr=True)
group = ensure_one(bot.groups().search(group_name))
day = time.strftime("%Y-%m-%d")


@bot.register(group)
def print_msg(msg):
    file_name = '%s.%s.txt' % (group_name, day)
    if hour_conf <= msg.create_time.hour:
        today = datetime.date.today()
        tomorrow = today + datetime.timedelta(1)
        file_name = '%s.%s' % (group_name, tomorrow.strftime("%Y-%m-%d"))
    file_ab_path = os.path.join(path, file_name)

    create_time = msg.create_time.strftime('%Y-%m-%d %H:%M:%S')
    name = msg.member.name
    if msg.type == TEXT:
        with open(file_ab_path, "a+") as f:
            word = "%s %s:%s\n" % (create_time, name, msg.text)
            f.write(word.encode('utf-8'))

bot.join()
