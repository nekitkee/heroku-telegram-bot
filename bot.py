# -*- coding: utf-8 -*-
#!/usr/bin/python

# encoding=utf8
import telebot
import datetime
#from ast import literal_eval as le

#import os
import ssl
import random
import urllib.request
import json
import wikipedia
#import sys
#import xml.etree.ElementTree as EE
#import codecs
from xml.dom import minidom
import time
import logger
import requests
import ast


token="NO TOKEN ZAZAZA"
url='https://blockchain.info/ru/ticker'
urlz='http://img.ignio.com/r/export/utf/xml/daily/com.xml'
delta=86400
gmt=7200



bot = telebot.TeleBot(token)
bot.send_message(56387565, "TEST PC")

@bot.message_handler(commands=['tsi'])
def handle_text(message):
    _now = datetime.datetime.now()
    datahh = ""
    a = str(_now)
    a = str(a[0:10] + " 00:00:00")
    timehh = time.strptime(a, '%Y-%m-%d %H:%M:%S')
    a = time.mktime(timehh)
    a = str(a)
    # dataaaaaaaaa
    thisday = 'сегодня '
    a = int(a[0:10])
    #a = a+delta
    # answer2=str(timehh)
    b = str(a + delta)
    a = str(a)
    urla = str('http://services.tsi.lv/schedule/api/service.asmx/GetLocalizedEvents?from=' + a + '&to=' + b + '&teachers=&rooms=&groups=1308&lang=%27ru%27')
    rs = requests.get(urla)
    text = rs.text
    # data=json.loads(text[1:-1])
    data = ast.literal_eval(text)
    res = json.loads(data['d'])
    urlas = 'http://services.tsi.lv/schedule/api/service.asmx/GetItems'
    rss = requests.get(urlas)
    texts = rss.text
    # data=json.loads(text[1:-1])
    datas = ast.literal_eval(texts)
    ress = json.loads(datas['d'])
    # name
    try:
        res1 = res['events']['values'][0][4]
    except IndexError:
        res1 = ""
    try:
        res2 = res['events']['values'][1][4]
    except IndexError:
        res2 = ""
    try:
        res3 = res['events']['values'][2][4]
    except IndexError:
        res3 = ""
    try:
        res4 = res['events']['values'][3][4]
    except IndexError:
        res4 = ""
    try:
        res5 = res['events']['values'][4][4]
    except IndexError:
        res5 = ""
    # time
    try:
        tim1 = int(res['events']['values'][0][0]) - gmt
        tim1 = str(time.ctime(tim1))
        datahh = tim1[3:-13]
        tim1 = tim1[11:-8]
    except IndexError:
        tim1 = ""
    try:
        tim2 = int(res['events']['values'][1][0]) - gmt
        tim2 = str(time.ctime(tim2))
        tim2 = tim2[11:-8]
    except IndexError:
        tim2 = ""
    try:
        tim3 = int(res['events']['values'][2][0]) - gmt
        tim3 = str(time.ctime(tim3))
        tim3 = tim3[11:-8]
    except IndexError:
        tim3 = ""
    try:
        tim4 = int(res['events']['values'][3][0]) - gmt
        tim4 = str(time.ctime(tim4))
        tim4 = tim4[11:-8]
    except IndexError:
        tim4 = ""
    try:
        tim5 = int(res['events']['values'][4][0]) - gmt
        tim5 = str(time.ctime(tim5))
        tim5 = tim5[11:-8]
    except IndexError:
        tim5 = ""
    # room
    try:
        rom1 = str(res['events']['values'][0][1])
        rom1 = rom1[1:-1]
        rom1 = str(ress['rooms'][rom1])
    except IndexError:
        rom1 = ""
    try:
        rom2 = str(res['events']['values'][1][1])
        rom2 = rom2[1:-1]
        rom2 = str(ress['rooms'][rom2])
    except IndexError:
        rom2 = ""
    try:
        rom3 = str(res['events']['values'][2][1])
        rom3 = rom3[1:-1]
        rom3 = str(ress['rooms'][rom3])
    except IndexError:
        rom3 = ""
    try:
        rom4 = str(res['events']['values'][3][1])
        rom4 = rom4[1:-1]
        rom4 = str(ress['rooms'][rom4])
    except IndexError:
        rom4 = ""
    try:
        rom5 = str(res['events']['values'][4][1])
        rom5 = rom5[1:-1]
        rom5 = str(ress['rooms'][rom5])
    except IndexError:
        rom5 = ""
    # teacher
    try:
        tec1 = str(res['events']['values'][0][3])
        tec1 = str(ress['teachers'][tec1])
    except IndexError:
        tec1 = ""
    try:
        tec2 = str(res['events']['values'][1][3])
        tec2 = str(ress['teachers'][tec2])
    except IndexError:
        tec2 = ""
    try:
        tec3 = str(res['events']['values'][2][3])
        tec3 = str(ress['teachers'][tec3])
    except IndexError:
        tec3 = ""
    try:
        tec4 = str(res['events']['values'][3][3])
        tec4 = str(ress['teachers'][tec4])
    except IndexError:
        tec4 = ""
    try:
        tec5 = str(res['events']['values'][4][3])
        tec5 = str(ress['teachers'][tec5])
    except IndexError:
        tec5 = ""
    if len(res1) < 1:
        answer = "Сегодня пар нет 🎉🌈"
    else:
        if (len(res1) > 1 and len(res2) < 1):
            answer = str('<b>' + datahh + ". " + thisday + ' 1 пара :</b>\n 1️⃣  ' + res1 + '\n 🕘 ' + tim1 + '\n 🏠 ' + rom1 + "\n 🤵🏻 " + tec1)
        else:
            if (len(res2) > 1 and len(res3) < 1):
                answer = str('<b>' + datahh + "🗓 " + thisday + ' 2 пары :</b>\n\n 1️⃣  ' + res1 + '\n 🕘 ' + tim1 + '\n 🏠 ' + rom1 + "\n 🤵🏻 <i>" + tec1 + '</i>\n\n 2️⃣  ' + res2 + '\n 🕚 ' + tim2 + '\n 🏠 ' + rom2 + "\n 🤵🏻 <i>" + tec2 + "</i>")
            else:
                if (len(res3) > 1 and len(res4) < 1):
                    answer = str('<b>' + datahh + "🗓 " + thisday + ' 3 пары :</b>\n\n 1️⃣  ' + res1 + '\n 🕘 ' + tim1 + '\n 🏠 ' + rom1 + "\n 🤵🏻 <i>" + tec1 + '</i>\n\n 2️⃣  ' + res2 + '\n 🕚 ' + tim2 + '\n 🏠 ' + rom2 + "\n 🤵🏻 <i>" + tec2 + '</i>\n\n 3️⃣  ' + res3 + '\n 🕚 ' + tim3 + '\n 🏠 ' + rom3 + "\n 🤵🏻 <i>" + tec3 + "</i>")
                else:
                    if (len(res4 > 1) and len(res5) < 1):
                        answer = str('<b>' + datahh + "🗓 " + thisday + ' 4 пары :</b>\n\n 1️⃣  ' + res1 + '\n 🕘 ' + tim1 + '\n 🏠 ' + rom1 + "\n 🤵🏻 <i>" + tec1 + '</i>\n\n 2️⃣  ' + res2 + '\n 🕚 ' + tim2 + '\n 🏠 ' + rom2 + "\n 🤵🏻 <i>" + tec2 + '</i>\n\n 3️⃣  ' + res3 + '\n 🕚 ' + tim3 + '\n 🏠 ' + rom3 + "\n 🤵🏻 <i>" + tec3 + "</i>" + '</i>\n\n 4️⃣ ' + res4 + '\n 🕚 ' + tim4 + '\n 🏠 ' + rom4 + "\n 🤵🏻 <i>" + tec4 + "</i>")
                    else:
                        answer = str('<b>' + datahh + "🗓 " + thisday + ' 4 пары :</b>\n\n 1️⃣  ' + res1 + '\n 🕘 ' + tim1 + '\n 🏠 ' + rom1 + "\n 🤵🏻 <i>" + tec1 + '</i>\n\n 2️⃣  ' + res2 + '\n 🕚 ' + tim2 + '\n 🏠 ' + rom2 + "\n 🤵🏻 <i>" + tec2 + '</i>\n\n 3️⃣  ' + res3 + '\n 🕚 ' + tim3 + '\n 🏠 ' + rom3 + "\n 🤵🏻 <i>" + tec3 + "</i>" + '</i>\n\n 4️⃣ ' + res4 + '\n 🕚 ' + tim4 + '\n 🏠 ' + rom4 + "\n 🤵🏻 <i>" + tec4 + '</i>\n\n 5️⃣ ' + res5 + '\n 🕚 ' + tim5 + '\n 🏠 ' + rom5 + "\n 🤵🏻 <i>" + tec5 + "</i>")
    log(message, answer)
    bot.send_message(message.chat.id, parse_mode='HTML', text=answer)


##

@bot.message_handler(commands=['tzi'])
def handle_text(message):
    _now = datetime.datetime.now()
    datahh = ""
    a = str(_now)
    a = str(a[0:10] + " 00:00:00")
    timehh = time.strptime(a, '%Y-%m-%d %H:%M:%S')
    a = time.mktime(timehh)
    a = str(a)
    # dataaaaaaaaa
    thisday = 'завтра '
    a = int(a[0:10])
    a = a+delta
    # answer2=str(timehh)
    b = str(a + delta)
    a = str(a)
    urla = str('http://services.tsi.lv/schedule/api/service.asmx/GetLocalizedEvents?from=' + a + '&to=' + b + '&teachers=&rooms=&groups=1308&lang=%27ru%27')
    rs = requests.get(urla)
    text = rs.text
    # data=json.loads(text[1:-1])
    data = ast.literal_eval(text)
    res = json.loads(data['d'])
    urlas = 'http://services.tsi.lv/schedule/api/service.asmx/GetItems'
    rss = requests.get(urlas)
    texts = rss.text
    # data=json.loads(text[1:-1])
    datas = ast.literal_eval(texts)
    ress = json.loads(datas['d'])
    # name
    try:
        res1 = res['events']['values'][0][4]
    except IndexError:
        res1 = ""
    try:
        res2 = res['events']['values'][1][4]
    except IndexError:
        res2 = ""
    try:
        res3 = res['events']['values'][2][4]
    except IndexError:
        res3 = ""
    try:
        res4 = res['events']['values'][3][4]
    except IndexError:
        res4 = ""
    try:
        res5 = res['events']['values'][4][4]
    except IndexError:
        res5 = ""
    # time
    try:
        tim1 = int(res['events']['values'][0][0]) - gmt
        tim1 = str(time.ctime(tim1))
        datahh = tim1[3:-13]
        tim1 = tim1[11:-8]
    except IndexError:
        tim1 = ""
    try:
        tim2 = int(res['events']['values'][1][0]) - gmt
        tim2 = str(time.ctime(tim2))
        tim2 = tim2[11:-8]
    except IndexError:
        tim2 = ""
    try:
        tim3 = int(res['events']['values'][2][0]) - gmt
        tim3 = str(time.ctime(tim3))
        tim3 = tim3[11:-8]
    except IndexError:
        tim3 = ""
    try:
        tim4 = int(res['events']['values'][3][0]) - gmt
        tim4 = str(time.ctime(tim4))
        tim4 = tim4[11:-8]
    except IndexError:
        tim4 = ""
    try:
        tim5 = int(res['events']['values'][4][0]) - gmt
        tim5 = str(time.ctime(tim5))
        tim5 = tim5[11:-8]
    except IndexError:
        tim5 = ""
    # room
    try:
        rom1 = str(res['events']['values'][0][1])
        rom1 = rom1[1:-1]
        rom1 = str(ress['rooms'][rom1])
    except IndexError:
        rom1 = ""
    try:
        rom2 = str(res['events']['values'][1][1])
        rom2 = rom2[1:-1]
        rom2 = str(ress['rooms'][rom2])
    except IndexError:
        rom2 = ""
    try:
        rom3 = str(res['events']['values'][2][1])
        rom3 = rom3[1:-1]
        rom3 = str(ress['rooms'][rom3])
    except IndexError:
        rom3 = ""
    try:
        rom4 = str(res['events']['values'][3][1])
        rom4 = rom4[1:-1]
        rom4 = str(ress['rooms'][rom3])
    except IndexError:
        rom4 = ""
    try:
        rom5 = str(res['events']['values'][4][1])
        rom5 = rom5[1:-1]
        rom5 = str(ress['rooms'][rom5])
    except IndexError:
        rom5 = ""
    # teacher
    try:
        tec1 = str(res['events']['values'][0][3])
        tec1 = str(ress['teachers'][tec1])
    except IndexError:
        tec1 = ""
    try:
        tec2 = str(res['events']['values'][1][3])
        tec2 = str(ress['teachers'][tec2])
    except IndexError:
        tec2 = ""
    try:
        tec3 = str(res['events']['values'][2][3])
        tec3 = str(ress['teachers'][tec3])
    except IndexError:
        tec3 = ""
    try:
        tec4 = str(res['events']['values'][3][3])
        tec4 = str(ress['teachers'][tec4])
    except IndexError:
        tec4 = ""
    try:
        tec5 = str(res['events']['values'][4][3])
        tec5 = str(ress['teachers'][tec5])
    except IndexError:
        tec5 = ""
    if len(res1) < 1:
        answer = "Завтра пар нет 🌈🎉"
    else:
        if (len(res1) > 1 and len(res2) < 1):
            answer = str('<b>' + datahh + ". " + thisday + ' 1 пара :</b>\n 1️⃣  ' + res1 + '\n 🕘 ' + tim1 + '\n 🏠 ' + rom1 + "\n 🤵🏻 " + tec1)
        else:
            if (len(res2) > 1 and len(res3) < 1):
                answer = str('<b>' + datahh + "🗓 " + thisday + ' 2 пары :</b>\n\n 1️⃣  ' + res1 + '\n 🕘 ' + tim1 + '\n 🏠 ' + rom1 + "\n 🤵🏻 <i>" + tec1 + '</i>\n\n 2️⃣  ' + res2 + '\n 🕚 ' + tim2 + '\n 🏠 ' + rom2 + "\n 🤵🏻 <i>" + tec2 + "</i>")
            else:
                if (len(res3) > 1 and len(res4) < 1):
                    answer = str('<b>' + datahh + "🗓 " + thisday + ' 3 пары :</b>\n\n 1️⃣  ' + res1 + '\n 🕘 ' + tim1 + '\n 🏠 ' + rom1 + "\n 🤵🏻 <i>" + tec1 + '</i>\n\n 2️⃣  ' + res2 + '\n 🕚 ' + tim2 + '\n 🏠 ' + rom2 + "\n 🤵🏻 <i>" + tec2 + '</i>\n\n 3️⃣  ' + res3 + '\n 🕚 ' + tim3 + '\n 🏠 ' + rom3 + "\n 🤵🏻 <i>" + tec3 + "</i>")
                else:
                    if (len(res4 > 1) and len(res5) < 1):
                        answer = str('<b>' + datahh + "🗓 " + thisday + ' 4 пары :</b>\n\n 1️⃣  ' + res1 + '\n 🕘 ' + tim1 + '\n 🏠 ' + rom1 + "\n 🤵🏻 <i>" + tec1 + '</i>\n\n 2️⃣  ' + res2 + '\n 🕚 ' + tim2 + '\n 🏠 ' + rom2 + "\n 🤵🏻 <i>" + tec2 + '</i>\n\n 3️⃣  ' + res3 + '\n 🕚 ' + tim3 + '\n 🏠 ' + rom3 + "\n 🤵🏻 <i>" + tec3 + "</i>" + '</i>\n\n 4️⃣ ' + res4 + '\n 🕚 ' + tim4 + '\n 🏠 ' + rom4 + "\n 🤵🏻 <i>" + tec4 + "</i>")
                    else:
                        answer = str('<b>' + datahh + "🗓 " + thisday + ' 4 пары :</b>\n\n 1️⃣  ' + res1 + '\n 🕘 ' + tim1 + '\n 🏠 ' + rom1 + "\n 🤵🏻 <i>" + tec1 + '</i>\n\n 2️⃣  ' + res2 + '\n 🕚 ' + tim2 + '\n 🏠 ' + rom2 + "\n 🤵🏻 <i>" + tec2 + '</i>\n\n 3️⃣  ' + res3 + '\n 🕚 ' + tim3 + '\n 🏠 ' + rom3 + "\n 🤵🏻 <i>" + tec3 + "</i>" + '</i>\n\n 4️⃣ ' + res4 + '\n 🕚 ' + tim4 + '\n 🏠 ' + rom4 + "\n 🤵🏻 <i>" + tec4 + '</i>\n\n 5️⃣ ' + res5 + '\n 🕚 ' + tim5 + '\n 🏠 ' + rom5 + "\n 🤵🏻 <i>" + tec5 + "</i>")
    log(message, answer)
    bot.send_message(message.chat.id, parse_mode='HTML', text=answer)



########HOROSCOPE

@bot.message_handler(commands=['horo'])
def handle_text(message):
    answer=""" Выбери свои знак зодиака🌚
   /aries - Овен
   /taurus - Телец 
   /gemini - Близнецы 
   /cancer - Рак 
   /leo - Лев 
   /virgo - Дева
   /libra - Весы 
   /scorpio - Скорпион 
   /sagittarius - Стрелец 
   /capricorn - Козерог 
   /aquarius - Водолей 
   /pisces - Рыбы """
    bot.send_message(message.chat.id, parse_mode='HTML', text=answer)
    log(message, answer)


@bot.message_handler(commands=['aries'])
def handle_text(message):
 zodiak = 'Овен'
 try:
     dom=minidom.parse(urllib.request.urlopen(urlz))
     day=dom.getElementsByTagName('date')
     day = str(day[0].attributes['today'].value)
    #####################
     today=dom.getElementsByTagName('today')[0].firstChild.data
     answer=str(" ♈️<strong>"+zodiak+"</strong> ♈️\n("+day +")\n"+today)

 except:
     answer="Sorry, there is no internet connection 😴"
     # ##########
 bot.send_message(message.chat.id, parse_mode='HTML', text=answer)
 log(message, answer)


@bot.message_handler(commands=['taurus'])
def handle_text(message):
     zodiak = 'Телец'
     try:
        dom = minidom.parse(urllib.request.urlopen(urlz))
        day = dom.getElementsByTagName('date')
        day = str(day[0].attributes['today'].value)
     #####################
        today = dom.getElementsByTagName('today')[1].firstChild.data
        answer = str(" ♉️<strong>" + zodiak + "</strong> ♉️️\n(" + day + ")\n" + today)
     except:
         answer = "Sorry, there is no internet connection 😴"
     bot.send_message(message.chat.id, parse_mode='HTML', text=answer)
     log(message, answer)

@bot.message_handler(commands=['gemini'])
def handle_text(message):
 zodiak = 'Близнецы'
 try:
    dom=minidom.parse(urllib.request.urlopen(urlz))
    day=dom.getElementsByTagName('date')
    day = str(day[0].attributes['today'].value)
    #####################
    today=dom.getElementsByTagName('today')[2].firstChild.data
    answer = str(" ♊️<strong>" + zodiak + "</strong> ♊️\n(" + day + ")\n" + today)
 except:
     answer="Sorry, there is no internet connection 😴"
 bot.send_message(message.chat.id, parse_mode='HTML', text=answer)
 log(message, answer)

@bot.message_handler(commands=['cancer'])
def handle_text(message):
     zodiak = 'Рак'
     try:
        dom = minidom.parse(urllib.request.urlopen(urlz))
        day = dom.getElementsByTagName('date')
        day = str(day[0].attributes['today'].value)
        #####################
        today = dom.getElementsByTagName('today')[3].firstChild.data
        answer = str(" ♋️<strong>" + zodiak + "</strong> ♋️\n(" + day + ")\n" + today)
     except:
         answer = "Sorry, there is no internet connection 😴"
     bot.send_message(message.chat.id, parse_mode='HTML', text=answer)
     log(message, answer)

@bot.message_handler(commands=['leo'])
def handle_text(message):
 zodiak = 'Лев'
 try:
    dom=minidom.parse(urllib.request.urlopen(urlz))
    day=dom.getElementsByTagName('date')
    day = str(day[0].attributes['today'].value)
    #####################
    today=dom.getElementsByTagName('today')[4].firstChild.data
    answer = str(" ♌️<strong>" + zodiak + "</strong> ♌️️\n(" + day + ")\n" + today)
 except:
     answer="Zzzz 😴"
 bot.send_message(message.chat.id, parse_mode='HTML', text=answer)
 log(message, answer)

@bot.message_handler(commands=['virgo'])
def handle_text(message):
     zodiak = 'Дева'
     try:
        dom = minidom.parse(urllib.request.urlopen(urlz))
        day = dom.getElementsByTagName('date')
        day = str(day[0].attributes['today'].value)
        #####################
        today = dom.getElementsByTagName('today')[5].firstChild.data
        answer = str(" ♍️<strong>" + zodiak + "</strong> ♍️\n(" + day + ")\n" + today)
     except:
         answer = "Sorry, there is no internet connection 😴"
     bot.send_message(message.chat.id, parse_mode='HTML', text=answer)
     log(message, answer)

@bot.message_handler(commands=['libra'])
def handle_text(message):
     zodiak = 'Весы'
     try:
        dom = minidom.parse(urllib.request.urlopen(urlz))
        day = dom.getElementsByTagName('date')
        day = str(day[0].attributes['today'].value)
        #####################
        today = dom.getElementsByTagName('today')[6].firstChild.data
        answer = str(" ♎️<strong>" + zodiak + "</strong> ♎️\n(" + day + ")\n" + today)
     except:
         answer = "Sorry, there is no internet connection 😴"
     bot.send_message(message.chat.id, parse_mode='HTML', text=answer)
     log(message, answer)

@bot.message_handler(commands=['scorpio'])
def handle_text(message):
 zodiak = 'Скорпион'
 try:
    dom=minidom.parse(urllib.request.urlopen(urlz))
    day=dom.getElementsByTagName('date')
    day = str(day[0].attributes['today'].value)
    #####################
    today=dom.getElementsByTagName('today')[7].firstChild.data
    answer = str(" ♏️<strong>" + zodiak + "</strong> ♏️\n(" + day + ")\n" + today)
 except:
     answer = "Sorry, there is no internet connection 😴"
 bot.send_message(message.chat.id, parse_mode='HTML', text=answer)
 log(message, answer)

@bot.message_handler(commands=['sagittarius'])
def handle_text(message):
 zodiak = 'Стрелец'
 try:
    dom=minidom.parse(urllib.request.urlopen(urlz))
    day=dom.getElementsByTagName('date')
    day = str(day[0].attributes['today'].value)
 #####################
    today=dom.getElementsByTagName('today')[8].firstChild.data
    answer = str(" ♐️<strong>" + zodiak + "</strong> ♐️\n(" + day + ")\n" + today)
 except:
     answer = "Sorry, there is no internet connection 😴"
 bot.send_message(message.chat.id, parse_mode='HTML', text=answer)
 log(message, answer)

@bot.message_handler(commands=['capricorn'])
def handle_text(message):
 zodiak = 'Козерог'
 dom=minidom.parse(urllib.request.urlopen(urlz))
 day=dom.getElementsByTagName('date')
 day = str(day[0].attributes['today'].value)
 #####################
 today=dom.getElementsByTagName('today')[9].firstChild.data
 answer = str(" ♑️<strong>" + zodiak + "</strong> ♑️\n(" + day + ")\n" + today)
 bot.send_message(message.chat.id, parse_mode='HTML', text=answer)
 log(message, answer)

@bot.message_handler(commands=['aquarius'])
def handle_text(message):
 zodiak = 'Водолей'
 try:
    dom=minidom.parse(urllib.request.urlopen(urlz))
    day=dom.getElementsByTagName('date')
    day = str(day[0].attributes['today'].value)
 #####################
    today=dom.getElementsByTagName('today')[10].firstChild.data
    answer = str(" ♒️<strong>" + zodiak + "</strong> ♒️\n(" + day + ")\n" + today)
 except:
     answer = "Sorry, there is no internet connection 😴"
 bot.send_message(message.chat.id, parse_mode='HTML', text=answer)
 log(message, answer)

@bot.message_handler(commands=['pisces'])
def handle_text(message):
     zodiak = 'Рыбы'
     try:
        dom = minidom.parse(urllib.request.urlopen(urlz))
        day = dom.getElementsByTagName('date')
        day = str(day[0].attributes['today'].value)
     #####################
        today = dom.getElementsByTagName('today')[11].firstChild.data
        answer = str(" ♓️<strong>" + zodiak + "</strong> ♓️\n(" + day + ")\n" + today)
     except:
         answer = "Sorry, there is no internet connection 😴"
     bot.send_message(message.chat.id, parse_mode='HTML', text=answer)
     log(message, answer)

def log(message,answer):
    print("\n ---------")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2} ), (chat id = {3}) \n Текст - {4}".format(message.from_user.first_name,
                                                                   message.from_user.last_name,
                                                                   str(message.from_user.id),
                                                                   str(message.chat.id),
                                                                   message.text))
    print(answer)
    dataid = str(message.from_user.id)
    dataname = str(message.from_user.first_name)
    datatext = str(message.text)
    datalastname = str(message.from_user.last_name)
    datachat = str(message.chat.id)
    datatitle = str(message.chat.title)
    datausername = str(message.from_user.username)
    data = "{id=" + dataid + " \n Чат =" + datatitle + "\n chat_id=" + datachat + " \n Имя =" + dataname + " \nФам =" + datalastname + "\n\n username=" + datausername + " \n Вопрос =" + datatext + " }\n ---------\n" + " \n Ответ= " + answer
    bot.send_message(-181158852,  parse_mode='HTML',text= data)



###########echo
@bot.message_handler(commands=['echo'])
def handle_text(message):
 data = str(message.text)
 answer=data.replace("/echo","")
 q=0
 while q<5:
    bot.send_message(message.chat.id, answer)
    q=q+1
 log(message, answer)

###########WIKI
@bot.message_handler(commands=['wiki'])
def handle_text(message):
 data = str(message.text)
 wikipedia.set_lang("ru")
 answer = data.replace("/wiki", "")
 answerflag = False
 if len(answer) > 1:
     answerflag = True
 if answerflag == False:
     answer = "Попробуй так : \n/wiki [запрос]"
 if answerflag == True:
     try:
         page = wikipedia.page(answer)
         wurl = page.url
         wcont=str(page.content[0:300])
         wtitle=page.title
         answer = str("<strong>" + wtitle + "</strong> 🔍 \n" + "" + wcont + "" + ".." + "\n 👉🏻 <a href='" + wurl + "'>Читать дальше..</a>")
         print(answer)
     except wikipedia.exceptions.DisambiguationError:
         topics = wikipedia.search(answer)
         choice = 1
         page=wikipedia.page(topics[choice])
         wurl = page.url
         wcont = str(page.content[0:300])
         wtitle = page.title
         answer = str("<strong>" + wtitle + "</strong> 🔍\n" +"" +wcont +""+ ".." + "\n 👉🏻 <a href='" + wurl + "'>Читать дальше..</a>")
         print(answer)
     except wikipedia.exceptions.PageError:
         answer = '404 :('

 bot.send_message(message.chat.id ,disable_web_page_preview=True , parse_mode='HTML',text=answer )
 log(message, answer)

####geteng
@bot.message_handler(commands=['geten'])
def handle_text(message):
 random.seed()
 temp = str(random.randint(1, 1900))
 urli=str('https://xkcd.com/'+temp+'/info.0.json')
 gcontext = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
 response = urllib.request.urlopen(urli, context=gcontext)
 content = response.read()
 data = json.loads(content.decode("utf8"))
 img=data['img']
 alt=data['alt']
 answer=str('<i>'+alt+'</i> <a href="'+img+'">['+temp+']</a>')
 bot.send_message(message.chat.id, parse_mode='HTML',text=answer)
 log(message, answer)

 #######joke
@bot.message_handler(commands=['joke'])
def handle_text(message):
     urli = str('http://rzhunemogu.ru/RandJSON.aspx?CType=1')
     response = urllib.request.urlopen(urli)
     content = str(response.read().decode('cp1251'))
     answer = content[12:-2]
     bot.send_message(message.chat.id, answer)
     log(message, answer)

@bot.message_handler(commands=['quote'])
def handle_text(message):
     urli = str('http://rzhunemogu.ru/RandJSON.aspx?CType=5')
     response = urllib.request.urlopen(urli)
     content = str(response.read().decode('cp1251'))
     answer = content[12:-2]
     bot.send_message(message.chat.id, answer)
     log(message, answer)

@bot.message_handler(commands=['tost'])
def handle_text(message):
     urli = str('http://rzhunemogu.ru/RandJSON.aspx?CType=6')
     response = urllib.request.urlopen(urli)
     content = str(response.read().decode('cp1251'))
     answer = content[12:-2]
     bot.send_message(message.chat.id, answer)
     log(message, answer)

@bot.message_handler(commands=['joke8'])
def handle_text(message):
     urli = str('http://rzhunemogu.ru/RandJSON.aspx?CType=11')
     response = urllib.request.urlopen(urli)
     content = str(response.read().decode('cp1251'))
     answer = content[12:-2]
     bot.send_message(message.chat.id, answer)
     log(message, answer)


@bot.message_handler(commands=['verse'])
def handle_text(message):
     urli = str('http://rzhunemogu.ru/RandJSON.aspx?CType=13')
     response = urllib.request.urlopen(urli)
     content = str(response.read().decode('cp1251'))
     answer = content[12:-2]
     bot.send_message(message.chat.id, answer)
     log(message, answer)

@bot.message_handler(commands=['tost8'])
def handle_text(message):
     urli = str('http://rzhunemogu.ru/RandJSON.aspx?CType=16')
     response = urllib.request.urlopen(urli)
     content = str(response.read().decode('cp1251'))
     answer=content[12:-2]
     bot.send_message(message.chat.id,answer)
     log(message, answer)

@bot.message_handler(commands=['jokes'])
def handle_text(message):
     answer = 'jokesh'
     log(message, answer)
     bot.send_message(message.chat.id, parse_mode='HTML', text="""/joke - анекдот 
/quote - цитаты
/tost - тост 🍾🥂
/joke8- Анекдот 🔞
/verse - Стишки 🔞
/tost8 - Тосты 🔞 """)

###########BTC
@bot.message_handler(commands=['btc'])
def handle_text(message):
 response = urllib.request.urlopen(url)
 content = response.read()
 data = json.loads(content.decode("utf8"))
 sell = str(data['EUR']['sell'])
 buy=str(data['EUR']['buy'])
 usell=str(data['USD']['sell'])
 ubuy=str(data['USD']['buy'])

 answer=str("💎 <b>BTC</b> 💎 \n\n <b>💶EUR💶</b> \n<i>buy:</i> "+buy+"\n<i>sell:</i> " +sell +"\n\n <b>💵USD💵</b> \n<i>buy:</i> "+ubuy+"\n<i>sell:</i> " +usell+"\n\n (c) blockchain")
 bot.send_message( message.chat.id ,parse_mode='HTML',text= answer )
 log(message, answer)

################
@bot.message_handler(commands=['radio'])
def handle_text(message):
 answer = ('🎵 Рекомендуем к прослушиванию Интернет-радиостанцию https://hqradio.ru/ - БЕСПЛАТНЫЕ стримы от DI.FM в высоком качестве . Более 90 жанров Электронной музыки , Рок , Джаз , Классика и многое дргугое .  ')
 bot.send_message( message.chat.id, answer)
 log(message, answer)


@bot.message_handler(commands=['commands'])
def handle_text(message):
 answer = 'commands'
 log(message, answer)
 bot.send_message(message.chat.id, parse_mode='HTML', text=""" Мои возможности весьма специфичны⬇️⬇️⬇️
/start - 🐣
/commands - список команд.
/get - <strong>рандомный xkcd комикс</strong> 📣
/geten - random xkcd comics (eng)
/btc - курс биткоина
/echo [text] - повторяет текст
/radio - Интернет-радио.
/jokes - анекдоты и тосты 🗣
/catstickers - несколько классных стикерпаков с котами 🐈  
/who - very usefull thing
/wiki [text] - поиск в энциклопедии 🔍
/8ball [Вопрос] - предсказать будущее 🎱
/riga - 👉🏻<i> рижские стикеры</i> 👈🏻 
/fsb -  Федеральная Служба Безопасности 
/fck - вместо тысячи слов.
/math - шпоры 
/horo - гороскоп 💫✨
/help - ⚒ техподдержка ⚒""")

@bot.message_handler(commands=['math'])
def handle_text(message):
     answer = 'math'
     log(message, answer)
     bot.send_message(message.chat.id, parse_mode='HTML', text=""" <b>Список шпор :</b>
 /der - Таблица производных
 /fun - Таблица эквивалентных бесконечно малых функций
 /cos - Основные формулы Тригонометрии 
 /sin - Значения sin , cos , tg , ctg """)

@bot.message_handler(commands=['der'])
def handle_text(message):
 answer = 'math'
 log(message, answer)
 bot.send_message(message.chat.id, parse_mode='HTML', text="""<b> Таблица производных</b> <a href="http://ru.solverbook.com/my_images/pic358.png" >!</a>""")

@bot.message_handler(commands=['fun'])
def handle_text(message):
 answer = 'math'
 log(message, answer)
 bot.send_message(message.chat.id, parse_mode='HTML', text="""<b> Таблица эквивалентных бесконечно малых функций</b> <a href="http://ru.solverbook.com/my_images/pic1082.png" >!</a>\n При условии что Х стремится к 0 <i></i>""")

@bot.message_handler(commands=['sin'])
def handle_text(message):
 answer = 'math'
 log(message, answer)
 bot.send_message(message.chat.id, parse_mode='HTML', text="""<b> Таблица значений тригонометрических функций </b> <a href="https://pp.userapi.com/c841638/v841638774/38c27/TxzJW1bHhKI.jpg" >!</a>\n  <i></i>""")

@bot.message_handler(commands=['cos'])
def handle_text(message):
 answer = 'math'
 log(message, answer)
 bot.send_message(message.chat.id, parse_mode='HTML', text="""<b>Основные тригонометрические формулы</b> <a href="https://pp.userapi.com/c841638/v841638774/38c1e/igae_2GTypQ.jpg" >!</a>\n """)

@bot.message_handler(commands=['start'])
def handle_text(message):
 answer=""" Приветствую тебя , дорогой анонимус ! используй /commands чтобы узнать , что я умею делать  """
 log(message, answer)
 bot.send_message(message.chat.id,answer )

@bot.message_handler(commands=['who'])
def handle_text(message):
 answer=""" ¯\_(ツ)_/¯  """
 log(message, answer)
 bot.send_message(message.chat.id,answer )

@bot.message_handler(commands=['help'])
def handle_text(message):
 answer = """ вы можете связаться с создателем бота 👤 @happykillers """
 log(message, answer)
 bot.send_message(message.chat.id, answer)

@bot.message_handler(commands=['fsb'])
def handle_text(message):
 answer ="You can follow them too "
 log(message, answer)
 bot.send_message(message.chat.id, parse_mode='HTML', text='<a href="https://twitter.com/federal_of_Russ/" >Они</a> следят за тобой')
 bot.send_message(message.chat.id,answer)
 bot.send_sticker(message.chat.id, 'CAADAgADigEAAs-71A6lnXmEVUCeNAI')

@bot.message_handler(commands=['fck'])
def handle_text(message):
 answer="Держите путевку на  👇🏿"
 bot.send_message(message.chat.id,answer)
 bot.send_location(message.chat.id,59.11834 ,10.360698)
 log(message, answer)

@bot.message_handler(commands=['get'])
def handle_text(message):
 random.seed()
 temp = random.randint(1, 95)
 if temp == 1 :
    answer= ('<i>Магнитогидродинамика объединяет интуитивную природу максвелловских уравнений с простотой решения уравнений Навье — Стокса. Это настолько очевидно, что физики добавляют слова «релятивистский» и «квантовый», чтобы не было так скучно.</i> <a href="https://xkcd.ru/i/1851_v1.png">[1851]</a>')
 elif temp == 2 :
    answer= ('<i>Кстати: Роджер Долтри изначально написал «Не отправляйте в жж все, что мы говорим», но стер второе ­­«ж», когда перешел на LiveInternet.</i> <a href="https://xkcd.ru/i/274_v1.png">[274]</a>')
 elif temp == 3 :
    answer= ('<i>Ненавижу быть самым медленным парнем в лаборатории</i> <a href="https://xkcd.ru/i/564_v1.png">[564]</a>')
 elif temp == 4 :
    answer= ('<i>Плюс, когда кто-то в конце концов отберёт твои очки и растопчет, стоимость замены будет значительно меньше 1 500 долларов.</i> <a href="https://xkcd.ru/i/1304_v1.png">[1304]</a>')
 elif temp == 5 :
    answer= ('<i>Не нажимайте на крыло.</i> <a href="https://xkcd.ru/i/726_v2.png">[726]</a>')
 elif temp == 6 :
    answer= ('<i>Можно было бы использовать тот эпизод из Футурамы с собакой Фрая, но над ним плачут даже боты</i> <a href="https://xkcd.ru/i/233_v1.png">[233]</a>')
 elif temp == 7 :
    answer= ('<i>1916 — «Папочка-физик» добрался до гравитации и вы не поверите, что он нашел. [картинки] [18+]</i> <a href="https://xkcd.ru/i/1283_v3.png">[1283]</a>')
 elif temp == 8 :
    answer= ('<i>Я предлагала найти приближенное численное решение, но неееет.</i> <a href="https://xkcd.ru/i/613_v1.png">[613]</a>')
 elif temp == 9 :
    answer= ('<i>Иногда я так делаю со столбиками километража на шоссе.</i> <a href="https://xkcd.ru/i/247_v1.png">[247]</a>')
 elif temp == 10 :
    answer=('<i>Самое ужасное, когда трещины на тротуаре не совпадают с твоим нормальным шагом.</i> <a href="https://xkcd.ru/i/245_v1.png">[245]</a>')
 elif temp == 11 :
    answer= ('<i>Иногда по-настоящему веселые вещи со стороны кажутся скучными.</i> <a href="https://xkcd.ru/i/324_v1.png">[324]</a>')
 elif temp == 12 :
    answer= ('<i> "Тафт в конкурсе мокрых футболок" - ключевой образ здесь</i> <a href="https://xkcd.ru/i/214_v1.png">[214]</a>')
 elif temp == 13 :
    answer= ('<i>На самом деле, единственная такая игра, в которую я играл, была «Зона 51».</i> <a href="https://xkcd.ru/i/53_v5.png">[53]</a>')
 elif temp == 14 :
    answer= ('<i>Ты смеешься, чтобы не плакать, ты вычисляешь, чтобы не плакать…</i> <a href="https://xkcd.ru/i/128_v1.png">[128]</a>')
 elif temp == 15 :
    answer= ('<i>Популярность динозавров вымерла после вероломной отмены бронтозавров.</i> <a href="https://xkcd.ru/i/460_v5.png">[460]</a>')
 elif temp == 16 :
    answer= ('<i>Наука должна быть настолько классной, насколько звучат заголовки новостей. Как например «РУССКИЕ РАЗРЕЗАЮТ НА ЧАСТИ И ПЕРЕСОБИРАЮТ СОБАК».</i> <a href="https://xkcd.ru/i/465_v1.png">[465]</a>')
 elif temp == 17 :
    answer= ('<i>А, стойте, вроде было новое письмо во время последнего F5</i> <a href="https://xkcd.ru/i/264_v1.jpg">[264]</a>')
 elif temp == 18 :
    answer= ('<i>2031г., Google в защиту вращающихся сканирующих электронных микроскопов на крышах своих автомобилей Street View: «Мы не раскрываем никаких подробностей, не доступных уже и так любому пешеходу, сканирующему ваш дом электронным микроскопом».</i> <a href="https://xkcd.ru/i/1204_v3.png">[1204]</a>')
 elif temp == 19 :
    answer= ('<i> Восьмой кадр - мой любимый</i> <a href="https://xkcd.ru/i/68_v1.png">[68]</a>')
 elif temp == 20 :
    answer= ('<i>Не хочешь поужинать, как только мы по-быстрому уничтожим все созданные нами запасы X-7?</i> <a href="https://xkcd.ru/i/734_v4.png">[734]</a>')
 elif temp == 21 :
    answer= ('<i> О, какое совпадение — пять фанатов Айн Рэнд в одном вагоне! Наверное, едут на конвент.</i> <a href="https://xkcd.ru/i/610_v1.png">[610]</a>')
 elif temp == 22 :
    answer= ('<i>Это имя пойдет в кучу конфигов по всей сети. Поменять имя ребенку куда легче!</i> <a href="https://xkcd.ru/i/910_v5.png">[910]</a>')
 elif temp == 23 :
    answer= ('<i>Она отправится в коллекцию спутников, проткнутая булавками и установленная в демонстрационную коробку. Не обязательно МОЮ коллекцию.</i> <a href="https://xkcd.ru/i/1243_v1.png">[1243]</a>')
 elif temp == 24 :
    answer= ('<i>Если бы вся небесная сфера была спроецирована прямо на поверхность Земли, астрономия была бы ГОРАЗДО проще; хватило бы обыкновенной лупы.</i> <a href="https://xkcd.ru/i/1276_v1.png">[1276]</a>')
 elif temp == 25 :
    answer= ('<i>И всё же, я каждый раз думаю: «Конечно, все эти продукты стоят дороже, чем порция еды из ресторана, но, только подумать, на сколько их хватит! Особенно, если учесть, что после каждого получаются ещё и остатки!»</i> <a href="https://xkcd.ru/i/854_v3.png">[854]</a>')
 elif temp == 26 :
    answer= ('<i> А если вызвать такси, то останется меньше денег на пиво.(Волк, коза и капуста - простенькая детская «логистическая» задачка.)</i> <a href="https://xkcd.ru/i/589_v1.png">[589]</a>')
 elif temp == 27 :
    answer= ('<i>Он видит тебя, когда ты спишь, он знает, когда ты просыпаешься, он читает /var/spool/mail/root, так что, ради всего святого, будь послушным.</i> <a href="https://xkcd.ru/i/838_v2.png">[838]</a>')
 elif temp == 28 :
    answer= ('<i>Если андроиды когда-нибудь всё-таки будут мечтать об электроовцах, не забудьте объявить переменную sheepCount как длинное целое.</i> <a href="https://xkcd.ru/i/571_v1.png">[571]</a>')
 elif temp == 29 :
    answer= ('<i>Если вы, зная толк в теории информации и информационной безопасности, ввязались в яростный спор с тем, кто толку в них не знает (и, не исключаю, чередует прописные и строчные), я искренне извиняюсь перед вами.</i> <a href="https://xkcd.ru/i/936_v3.png">[936]</a>')
 elif temp == 30 :
    answer= ('<i>И, конечно, так как их поучительная история была напечатана в бумажной газете, её никто не прочитал.В переводе с английского <b> kindle </b> — зажигать, загораться.</i> <a href="https://xkcd.ru/i/750_v4.png">[750]</a>')
 elif temp == 31 :
    answer=('<i>«Свету тех миллионов звезд, которые вы видите, скорее всего, много тысяч лет» — это замечательный пример того, как обычные люди существенно ПЕРЕоценивают астрономические величины.</i> <a href="https://xkcd.ru/i/1342_v2.png">[1342]</a>')
 elif temp == 32 :
    answer= ('<i>Когда я говорю, что мы должны как-нибудь что-нибудь сделать, в глубине души я надеюсь, что ты скажешь: „Почему бы не сейчас?“</i> <a href="https://xkcd.ru/i/187_v1.png">[187]</a>')
 elif temp == 33 :
    answer= ('<i>— Алло, Охотники за привидениями? — ууУУуууу те, кто родился через годы после этого фильма, уже заводят второго ребенка ууУуууУуу</i> <a href="https://xkcd.ru/i/1393_v2.png">[1393]</a>')
 elif temp == 34 :
    answer= ('<i>К тому же я всегда её ненавидел.</i> <a href="https://xkcd.ru/i/945_v10.png">[945]</a>')
 elif temp == 35 :
    answer= ('<i>Полагаю, если бы она верила в нелогичные реальности, вряд ли она была бы моей фантазией.</i> <a href="https://xkcd.ru/i/429_v1.png">[429]</a>')
 elif temp == 36 :
    answer= ('<i> Никогда не приноси текилу на собрания по обмену подписями ключей.(Основа сети доверия — это подписывание ключей. Поскольку для подтверждения достоверности ключа требуется личная встреча, иногда проводятся собрания по обмену подписями ключей.)</i> <a href="https://xkcd.ru/i/364_v1.png">[364]</a>')
 elif temp == 37 :
    answer= ('<i>Скажи спасибо, что у меня кончились скобки для степлера.</i> <a href="https://xkcd.ru/i/262_v1.png">[262]</a>')
 elif temp == 38 :
    answer= ('<i>Похоже, после каждого «Нам нужны значки, чтобы пояснять, о чём речь!» приходит озарение «Постойте, слова и сами справляются».</i> <a href="https://xkcd.ru/i/1306_v1.png">[1306]</a>')
 elif temp == 39 :
    answer= ('<i>Я посмотрел кое-какие дампы с уязвимых сайтов, и это… ужасно. Я видел письма, пароли, подсказки к паролям. Ключи SSL и куки сессий. Крупные серверы, до краев полные IP-адресами посетителей. Горящие боевые корабли на подступах к Ориону, си-лучи, мерцающие во тьме близ врат Тангейзера. Похоже, мне стоит пропатчить OpenSSL.</i> <a href="https://xkcd.ru/i/1353_v2.png">[1353]</a>')
 elif temp == 40 :
    answer= ('<i>Там было что-то про чашку, меч, дерево и зелёный холм ...</i> <a href="https://xkcd.ru/i/430_v1.png">[430]</a>')
 elif temp == 41 :
    answer= ('<i>Просто подумал, что ты должна знать</i> <a href="https://xkcd.ru/i/15_v1.jpg">[15]</a>')
 elif temp == 42 :
    answer= ('<i> Требуются добровольцы для изучения возможности заражения урушиолом через прямой контакт с тонкими полосками бумаги.</i> <a href="https://xkcd.ru/i/749_v1.png">[749]</a>')
 elif temp == 43 :
    answer= ('<i>В недоступной памяти по адресу 0x-1 все компьютеры хранят секрет. Я нашёл его, и он в том, что все люд... SEGMENTATION FAULT /// В оригинале комикс содержал игру слов, которую пришлось немного исказить при переводе. (-can you give me a few pointers? -0x3A28213A , 0x6339392C .. </i> <a href="https://xkcd.ru/i/138_v7.png">[138]</a>')
 elif temp == 44 :
    answer= ('<i>Восьмой кадр - мой любимый</i> <a href="https://xkcd.ru/i/68_v1.png">[68]</a>')
 elif temp == 45 :
    answer= ('<i>Свидания с самим собой — это теперь что, главная тема в xkcd? Беспокоюсь.</i> <a href="https://xkcd.ru/i/267_v1.jpg">[267]</a>')
 elif temp == 46 :
    answer=('<i>Я твёрдо придерживаюсь мнения, что если на чём-то не указан год, срок годности каждый раз сбрасывается, и оно опять съедобно в течение двух недель перед указанной датой.</i> <a href="https://xkcd.ru/i/737_v2.png">[737]</a>')
 elif temp == 47 :
    answer= ('<i>К моменту написания, Убунту 6.10 и FireFox 2.0 оставили мой компьютер в полном беспорядке.</i> <a href="https://xkcd.ru/i/178_v1.png">[178]</a>')
 elif temp == 48 :
    answer= ('<i>«Я был хорош в стрельбе по тарелочкам, пока меня не вышибли оттуда за то, что я ловил их сачком и казнил выстрелом в упор».</i> <a href="https://xkcd.ru/i/929_v3.png">[929]</a>')
 elif temp == 49 :
    answer= ('<i>Удобно приближаемое значением e + 2, число Пау широко известно как Дьявольская пропорция (потому что среди первых 200 знаков его восьмеричной записи "666" встречается четырежды, тогда как ни одна другая последовательность из трех или более одинаковых цифр не встречается более раза)</i> <a href="https://xkcd.ru/i/1292_v1.png">[1292]</a>')
 elif temp == 50 :
    answer= ('<i>Почему, рассказывая о моих обязанностях, вы растягиваете первый слог в слове «работа»?</i> <a href="https://xkcd.ru/i/1293_v1.png">[1293]</a>')
 elif temp == 51 :
    answer= ('<i>Я слышал, что если ты проработал 256 дней, то они обучают тебя секрету левитации.</i> <a href="https://xkcd.ru/i/192_v1.png">[192]</a>')
 elif temp == 52 :
    answer= ('<i>Если я — бог, то почему Мару не мой кот?</i> <a href="https://xkcd.ru/i/676_v1.png">[676]</a>')
 elif temp == 53 :
    answer= ('<i>Кто-то сказал — не помню, когда и где, — что апеллирование к свободе слова при защите своей позиции равносильно безоговорочной капитуляции, ведь самым веским аргументом спорящего становится тот факт, что его позицию можно высказать, не попав за решетку.</i> <a href="https://xkcd.ru/i/1357_v2.png">[1357]</a>')
 elif temp == 54 :
    answer= ('<i>Это даже лучше, чем мой прошлый корпус для смартфона: трубка от старого стационарного телефона Western Electric Model 2500. На ней даже болтался обрывок потертого кабеля, все как положено.</i> <a href="https://xkcd.ru/i/1372_v4.png">[1372]</a>')
 elif temp == 55 :
    answer= ('<i>Грустная, но правдивая история. По крайней мере, я узнал команду say в OS X.</i> <a href="https://xkcd.ru/i/530_v1.png">[530]</a>')
 elif temp == 56 :
    answer= ('<i>Слушай, они требуют, чтобы ты перестал ставить метку «ТАМ, ГДЕ ТЫ РАЗБИЛА МОЁ СЕРДЦЕ» на свой дом.</i> <a href="https://xkcd.ru/i/489_v1.png">[489]</a>')
 elif temp == 57 :
    answer= ('<i>Сторона обвинения вызывает Готфрида Лейбница.</i> <a href="https://xkcd.ru/i/1153_v1.png">[1153]</a>')
 elif temp == 58 :
    answer= ('<i>«Свету тех миллионов звезд, которые вы видите, скорее всего, много тысяч лет» — это замечательный пример того, как обычные люди существенно ПЕРЕоценивают астрономические величины.</i> <a href="https://xkcd.ru/i/1342_v2.png">[1342]</a>')
 elif temp == 59 :
    answer= ('<i>— Ждите меня с первыми лучами пятого дня. На заре взгляните на восток. — А потом на запад, чтоб убедиться, что нет машин.</i> <a href="https://xkcd.ru/i/1272_v2.png">[1272]</a>')
 elif temp == 60 :
    answer= ('<i>Если у тебя не будет удлинителя, я его тоже смогу принести. Ведь мы же друзья! Правда?</i> <a href="https://xkcd.ru/i/614_v1.png">[614]</a>')
 elif temp == 61 :
    answer= ('<i>Один инженер нашел решение проблемы P=NP, но оно навсегда осталось внутри процедуры калибровки электрических сбивалок для яичных белков. На каждое открытое нами 0x5f375a86 будут тысячи, о которых мы так и не узнаем.(0x5f375a86 — «магическая» константа, которая позволила создать невероятно быстрый алгоритм нахождения квадратного корня для игры Quake.)</i> <a href="https://xkcd.ru/i/664_v1.png">[664]</a>')
 elif temp == 62 :
    answer= ('<i>В конце концов, он был уничтожен ядерным оружием с разрушительной силой бомбы, сброшенной на Хиросиму.</i> <a href="https://xkcd.ru/i/1257_v1.png">[1257]</a>')
 elif temp == 63 :
    answer= ('<i>Кроме того, я прошу прощения за тот раз, когда я забрался в твой мир и испугал всех лесбийской оргией под надзором священника.(Флатландия — научно-фантастический роман Эдвина Э. Эбботта, вышедший в 1884 году. Считается полезным для людей, изучающих такие темы, как, например, понятия о других пространственных измерениях или гиперпространства.) </i> <a href="https://xkcd.ru/i/721_v15.png">[721]</a>')
 elif temp == 64 :
    answer= ('<i>Я склоняюсь к пятнадцати. Проблем довольно много.</i> <a href="https://xkcd.ru/i/1232_v3.png">[1232]</a>')
 elif temp == 65 :
    answer= ('<i>Мне придётся добавить что-либо в strum bar, чтобы он щёлкал как старые контроллеры. Я очень привык к обратной связи; бесшумность сбивает меня с толку.</i> <a href="https://xkcd.ru/i/359_v1.png">[359]</a>')
 elif temp == 66 :
    answer= ('<i>А ещё здесь каждый раз не выскакивает окошко с просьбой использовать настоящее имя. Больше того: здесь вообще нельзя указать имя. Просто нужно постоянно напоминать всем, кто ты такой.</i> <a href="https://xkcd.ru/i/1305_v1.png">[1305]</a>')
 elif temp == 67 :
    answer= ('<i> Господи, это будущее повсюду</i> <a href="https://xkcd.ru/i/209_v1.png">[209]</a>')
 elif temp == 68 :
    answer= ('<i>Папа, а где сейчас дедушка?</i> <a href=" https://xkcd.ru/i/659_v1.png">[659]</a>')
 elif temp == 69 :
    answer= ('<i>Почему у тебя не может быть обычных экзистенциальных тревог, как у других ребят?</i> <a href="https://xkcd.ru/i/167_v1.png">[167]</a>')
 elif temp == 70 :
    answer= ('<i>В более общем случае, великая сила влечет великую производную d(импульс)/dt.</i> <a href="https://xkcd.ru/i/643_v1.png">[643]</a>')
 elif temp == 71 :
    answer= ('<i>LEGO Group уже и так крупнейшие производители шин на планете.</i> <a href="https://xkcd.ru/i/1281_v1.png">[1281]</a>')
 elif temp == 72 :
    answer= ('<i>Я твёрдо верю, что с проектом всё будет в порядке, если ты носишь одну из таких штук.</i> <a href="https://xkcd.ru/i/649_v1.png">[649]</a>')
 elif temp == 73 :
    answer= ('<i>Слушай, они требуют, чтобы ты перестал ставить метку «ТАМ, ГДЕ ТЫ РАЗБИЛА МОЁ СЕРДЦЕ» на свой дом.</i> <a href="https://xkcd.ru/i/489_v1.png">[489]</a>')
 elif temp == 74 :
    answer= ('<i>Когда я попробовал, то врезался в пружину Cлинки, спускающуюся на удвоенной скорости.</i> <a href="https://xkcd.ru/i/252_v1.png">[252]</a>')
 elif temp == 75 :
    answer= ('<i> Советы бывалых: предел Шеннона — Хартли можно преодолеть, выставив нулевой размер шрифта.</i> <a href="https://xkcd.ru/i/1381_v1.png">[1381]</a>')
 elif temp == 76 :
    answer= ('<i>Что ж, дети определенно получат фенотип гиков от биологии.</i> <a href="https://xkcd.ru/i/634_v2.png">[634]</a>')
 elif temp == 77 :
    answer= ('<i>К счастью, с зарядками проблема была решена, теперь у нас у всех стандартизированные mini-USB. Или micro-USB? Чёрт.</i> <a href="https://xkcd.ru/i/927_v4.png">[927]</a>')
 elif temp == 78 :
    answer= ('<i>Проверка вменяемости среды сборки ... среда сборки ухмыляется и держит шпатель. Видимо нет.«Вменяемость (нормальность) среды сборки» — проверка, производимая Automake при подготовке к компиляции.</i> <a href="https://xkcd.ru/i/371_v1.png">[371]</a>')
 elif temp == 79 :
    answer= ('<i>Этот сюжет позже был воспроизведён в архивах Международной федерации рулетко-выдвигания, под названием "Основание вида спорта".</i> <a href="https://xkcd.ru/i/284_v1.png">[284]</a>')
 elif temp == 80 :
    answer= ('<i>Стоит поменять URL на “https” перед загрузкой.</i> <a href="https://xkcd.ru/i/1247_v1.png">[1247]</a>')
 elif temp == 81 :
    answer= ('<i>Немногие выбравшиеся обнаружили, что кнопка аварийного отключения не работает. Давка продолжалась два часа и три раза достигала низа эскалатора.</i> <a href="https://xkcd.ru/i/954_v2.png">[954]</a>')
 elif temp == 82 :
    answer= ('<i>Настоящие программисты задают универсальные константы в начале так, что вселенная изменяется таким образом, чтобы содержать диск с данными, которые они хотят.</i> <a href="https://xkcd.ru/i/378_v1.png">[378]</a>')
 elif temp == 83 :
    answer= ('<i>Возможно, когда-нибудь я напишу об этом месте статью в Википедии! А, то есть это, "не оригинальное исследование".</i> <a href="https://xkcd.ru/i/265_v1.jpg">[265]</a>')
 elif temp == 84 :
    answer= ('<i>Ну, не то чтобы МНОГО… они даже не могут позволить себе семплер. Ну, в смысле, после ремикса вышло бы вполне неплохо.</i> <a href="https://xkcd.ru/i/586_v1.png">[586]</a>')
 elif temp == 85 :
    answer= ('<i>Батарея ноутбука по взрывной мощности сравнима с ручной гранатой, и если её закоротить... Эй! Меня нельзя арестовывать за то, что я доказал непоследовательность ваших правил!</i> <a href="https://xkcd.ru/i/651_v1.png">[651]</a>')
 elif temp == 86 :
    answer= ('<i> БЛОК СХЕМЫ </i> <a href="https://xkcd.ru/i/1488_v3.png">[1488]</a>')
 elif temp == 87 :
    answer= ('<i>Я бы нажал на них, чтобы поправить, но не могу до них дотянуться.Может, попробуем быстро сменить несколько дней и ночей?(На жидкокристаллических мониторах «битые пиксели» действительно можно в большинстве случаев привести в нормальное состояние нажав на них. Так же помогает быстрое их включение/выключение).</i> <a href="https://xkcd.ru/i/395_v1.png">[395]</a>')
 elif temp == 88 :
    answer= ('<i>А музыкальные жанры рокстеди и бипоп стали для нас именами прихвостней из мультфильма так же, как увертюра из «Вильгельма Телля» стала для наших родителей темой «The Lone Ranger».</i> <a href="https://xkcd.ru/i/197_v1.png">[197]</a>')
 elif temp == 89 :
    answer= ('<i>В качестве стандарта я использую начало сна в полночь и пробуждение в 8 утра.</i> <a href="https://xkcd.ru/i/448_v1.png">[448]</a>')
 elif temp == 90 :
    answer= ('<i>Можно также игнорировать любое научное утверждение, где «квантовая механика» — самая сложная фраза.</i> <a href="https://xkcd.ru/i/1240_v1.png">[1240]</a>')
 elif temp == 91 :
    answer= ('<i>Неперезаписываемая лента? (Машина Тьюринга - классическое абстрактное вычислительное устройство. Включает в себя бесконечную ленту, по ячейкам которой может перемещаться, а также читать и записывать.) </i> <a href="https://xkcd.ru/i/205_v1.png">[205]</a>')
 elif temp == 92 :
    answer= ('<i>Ещё она начинает каждое письмо словами «Дорогой Будущий <ваше имя>».</i> <a href="https://xkcd.ru/i/630_v1.png">[630]</a>')
 elif temp == 93 :
    answer= ('<i>Быстрее, сделай страховку из кабеля 6-й категории и давай за мной.</i> <a href="https://xkcd.ru/i/308_v1.png">[308]</a>')
 elif temp == 94 :
    answer= ('<i>Я слышал, что они принимают идеи на iaupublic@iap.fr.</i> <a href="https://xkcd.ru/i/1253_v1.png">[1253]</a>')
 elif temp == 95 :
    answer= ('<i>Фейнман вспоминал другой хороший вопрос, который студенты-физики любили испытывать на только-только поступивших: когда смотришь на текст в зеркале, как так получается, что он развернут справа-налево, а не снизу-вверх? Что такого особенного именно в горизональном направлении?</i> <a href="https://xkcd.ru/i/1145_v3.png">[1145]</a>')
 log(message, answer)
 bot.send_message(message.chat.id, parse_mode='HTML', text=answer)

##############################
@bot.message_handler(commands=['8ball'])
def handle_text(message):
 random.seed()
 temp = random.randint(1, 20)
 data = str(message.text)
 question = data.replace("/8ball", "")
 answerflag = False
 if len(question) > 1:
     answerflag = True
 if answerflag==False:
     answer='Попробуй задать вопрос так: \n/8ball [Вопрос]'
     bot.reply_to(message, answer)

 if answerflag==True:
  if temp == 1 :
    answer= 'Бесспорно'
  elif temp == 2 :
    answer= 'Предрешено'
  elif temp == 3 :
    answer= 'Никаких сомнений'
  elif temp == 4 :
    answer= 'Определённо да'
  elif temp == 5 :
    answer= 'Можешь быть уверен в этом'
  elif temp == 6 :
    answer= 'Мне кажется — «да»'
  elif temp == 7 :
    answer= 'Вероятнее всего'
  elif temp == 8 :
    answer= 'Хорошие перспективы'
  elif temp == 9 :
    answer= 'Знаки говорят — «да»'
  elif temp == 10 :
    answer= 'Да'
  elif temp == 11 :
    answer= 'Пока не ясно, попробуй сновао'
  elif temp == 12 :
    answer= 'Спроси позже'
  elif temp == 13 :
    answer= 'Лучше не рассказывать'
  elif temp == 14 :
    answer= 'Сейчас нельзя предсказать'
  elif temp == 15 :
    answer= 'Сконцентрируйся и спроси опять'
  elif temp == 16 :
    answer= 'Даже не думай'
  elif temp == 17 :
    answer= 'Мой ответ — «нет»'
  elif temp == 18 :
    answer= 'По моим данным — «нет»'
  elif temp == 19 :
    answer= 'Перспективы не очень хорошие'
  elif temp == 20 :
    answer= 'Весьма сомнительно'
  log(message, answer)
  bot.reply_to(message, answer)

@bot.message_handler(commands=['riga'])
def handle_text(message):
 answer = '*RIGA*'
 log(message, answer)
 bot.send_message(message.chat.id ,parse_mode='HTML', text= ' Забирай <b> Рижские стикеры </b> к себе в коллекцию \n <i> З.Ы: Стикерпак регулярно дополняется.\n  З.Ы.Ы: Если ты являешься рижанином , и у тебя есть годные идеи для стикеров - пиши в лс.    </i> @happykillers @kvadrokub ')
 bot.send_sticker(message.chat.id, 'CAADBAADjAAD7WdcA_wH_ZceAdttAg')

@bot.message_handler(commands=['catstickers'])
def handle_text(message):
 random.seed()
 temp = random.randint(1, 30)
 if temp == 1:
    answer = 'CAADAgADFgADFvHqEujtupOyzES_Ag'
 elif temp == 2:
    answer = 'CAADAgAD3wEAAulVBRiqAAFnlYxLTYYC'
 elif temp == 3:
    answer = 'CAADBAADqwMAAv4zDQaHtXWYOAvnCwI'
 elif temp == 4:
    answer =  'CAADAgADugIAAu7EoQo_dZOtl6U8RQI'
 elif temp == 5:
    answer = 'CAADAgADIgYAAhhC7ggTiL8WiAABSAcC'
 elif temp == 6:
    answer = 'CAADAgADKAMAAoZALgI8Cc13uyaJLgI'
 elif temp == 7:
    answer = 'CAADAgADsgEAAs7Y6AvX1XS68TJ8AAEC'
 elif temp == 8:
    answer = 'CAADAgADaAEAAvR7GQAB8LLElrB2gvwC'
 elif temp == 9:
    answer ='CAADAQADswAD5fRhDPY4mBJQgJ-vAg'
 elif temp == 10:
    answer = 'CAADAgADAgADlMeUFSbkPuFrjuBBAg'
 elif temp == 11:
    answer = 'CAADAgADCgADKHdnB0zFRDy3Z88uAg'
 elif temp == 12:
    answer = 'CAADBAADoAEAAsHKsAP4X8GpPK1S4wI'
 elif temp == 13:
    answer = 'CAADBQADLQEAAn36qQcD8T_cc_PGsgI'
 elif temp == 14:
    answer = 'CAADAQADOwADXaFEEO7I8MvCtmf3Ag'
 elif temp == 15:
    answer = 'CAADAgADagAD-Aq8Am4WKbj8vrJiAg'
 elif temp == 16:
    answer = 'CAADAgADaQUAAvnWfQcR1CoJQfJDWwI'
 elif temp == 17:
    answer = 'CAADAgADhQEAAnPZKAzMOP9r84_r8AI'
 elif temp == 18:
    answer = 'CAADAgADdwEAAkcVaAk332205vjPNgI'
 elif temp == 19:
    answer = 'CAADAgADsAADTbVREToKfFqkMnrYAg'
 elif temp == 20:
    answer = 'CAADAgADzgADeVziCaM73-NsoDvHAg'
 elif temp == 21:
    answer = 'CAADAwADTQAD_EcJBczFASrnwslXAg'
 elif temp == 22:
    answer = 'CAADAgADHQADG7f5CtivB47TNXVbAg'
 elif temp == 23:
    answer = 'CAADAgADgAIAAs7Y6AuRNkERFTWNsQI'
 elif temp == 24:
    answer = 'CAADAgADnQADB4YVB0-8D4zxvGIsAg'
 elif temp == 25:
    answer ='CAADAgADawEAAhhC7gjfWNP8zCNjfAI'
 elif temp == 26:
    answer ='CAADBAADewMAAlI5kwbo405Q7ohuDgI'
 elif temp == 27:
    answer = 'CAADAgADewADiqODBVerMOK2AQ-eAg'
 elif temp == 28:
    answer = 'CAADBAADfAADEGBEBjtu5XQn1uwhAg'
 elif temp == 29:
    answer = 'CAADAQADGRIAAq8ZYgf8_MIUfhov0QI'
 elif temp == 30:
    answer = 'CAADAgADBywAAlOx9wPCKJ9D3O9nVQI'
 log(message,answer)
 bot.send_sticker(message.chat.id, answer)



@bot.message_handler(content_types=["text"])
def handle_command(message):
 FLAG = False
 if message.text == "Привет" or message.text == "Йо" or message.text == "привет" or message.text == "здаров":
     answer="Здаров"
     FLAG=True
 elif message.text == "Как дела?":
    answer="Зашибись ! Как сам ?"
    FLAG = True
 elif message.text == "?" and str(message.from_user.id)== "56387565":
     answer="Ты избранный , Нео."
     FLAG = True
 elif message.text == "VGN" or message.text == "vgn" or message.text == "Vgn"  or message.text == "ВГН"  or message.text == "Вгн"  or message.text == "вгн":
    answer="BAMBOLEO"
    FLAG = True
 elif message.text == ":D" or message.text == ":d":
     random.seed()
     temp = random.randint(1, 5)
     if temp == 1:
         answer = ":DDDDDDDDDDDDD"
         FLAG = True
     elif temp == 2:
         answer = "ОРУ"
         FLAG = True
     elif temp == 3:
         answer = "nothing"
     elif temp == 4:
         answer = ":P"
         FLAG = True
     elif temp == 5:
         answer = ":Дд "
         FLAG = True
 elif message.text == "XD" or message.text == "xd" or message.text == "хД" or message.text == "хд" or message.text == "xD" or message.text == "Хдд":
     random.seed()
     temp = random.randint(1, 7)
     if temp == 1:
         answer = "XDDDDDD"
         FLAG = True
     elif temp == 2:
         answer = "XDdd"
         FLAG = True
     elif temp == 3:
         answer = "Икс Дэ"
         FLAG = True
     elif temp == 4:
         answer = "ХддДд"
         FLAG = True
     elif temp == 5:
         answer = "nothing "
     elif temp == 6:
         answer = "nothing)"
     elif temp == 7:
         answer = "nothing "
 elif message.text == "Че вы?" or message.text == "че вы?" or message.text == "че вы" or message.text == "Че вы":
    answer="niCho"
    FLAG = True
 elif message.text == "(" or message.text == "((" or message.text == "(((" or message.text == "((((":
     random.seed()
     temp = random.randint(1, 3)
     if temp == 1:
         answer = "((((((((("
         FLAG = True
     elif temp == 2:
         answer = "сук"
         FLAG = True
     elif temp == 3:
         answer = "nothing"
 elif message.text == ")" or message.text == "))" or message.text == ")))" or message.text == "))))":
    answer="))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))"
    FLAG = True
 elif message.text == "Ааа" or message.text == "ааа" or message.text == "а" or message.text == "А" or message.text == "Аааа":
     random.seed()
     temp = random.randint(1, 7)
     if temp == 1:
         answer = "Ббб"
         FLAG = True
     elif temp == 2:
         answer = "б - бля"
         FLAG = True
     elif temp == 3:
         answer = "ААААсталбиней"
         FLAG = True
     elif temp == 4:
         answer = "ААААхуехал твой автобус)"
         FLAG = True
     elif temp == 5:
         answer = "nothing)"
     elif temp == 6:
         answer = "nothing "
     elif temp == 5:
         answer = "ААтсосиськи кожура "
         FLAG = True
     elif temp == 6:
         answer = "nothing)"
     elif temp == 7:
         answer = "nothing "
 elif message.text == "ооо" or message.text == "Ооо" or message.text == "о!":
    answer="О_о"
    FLAG = True
 elif message.text == "1-15" or message.text == "1 - 15":
    answer="5-65"
    FLAG = True
 elif message.text == "Лол" or message.text == "лол":
    random.seed()
    temp = random.randint(1, 3)
    if temp == 1:
      answer="Не то слово"
      FLAG = True
    elif temp == 2:
      answer="КеК"
      FLAG = True
    elif temp == 3:
      answer="LOOOL :--D"
      FLAG = True
 elif message.text == "Го гулять":
        answer = "ПОГНАЛЕЕ"
        FLAG = True
 elif message.text == "Гы" or message.text == "гы":
    answer="гЫг"
    FLAG = True
 elif message.text == "Я люблю тебя" or message.text == "I love you" or message.text == "i love you" or message.text == "я люблю тебя":
    answer="♥"
    FLAG = True
 elif message.text == "Да" or message.text == "да" or message.text == "Da" or message.text == "Даа" or message.text == "da":
     random.seed()
     temp = random.randint(1, 7)
     if temp == 1:
         answer = "манда"
         FLAG = True
     elif temp == 2:
         answer = "борода"
         FLAG = True
     elif temp == 3:
         answer = "звезда"
         FLAG = True
     elif temp == 4:
         answer = "nothing)"
     elif temp == 5:
         answer = "nothing)"
     elif temp == 6:
         answer = "nothing "
     elif temp == 7:
         answer = "nothing "
 elif message.text == "нет" or message.text == "Нет" or message.text == "net" or message.text == "Net" or message.text == "неет":
     random.seed()
     temp = random.randint(1, 7)
     if temp == 1:
             answer = "п*дора ответ"
             FLAG = True
     elif temp == 2:
             answer = "кларнет"
             FLAG = True
     elif temp == 3:
             answer = "🐬"
             FLAG = True
     elif temp == 4:
             answer = "nothing)"
     elif temp == 5:
             answer = "nothing)"
     elif temp == 6:
             answer = "nothing "
     elif temp == 7:
             answer = "nothing "
 #elif message.from_user.id == 56387565:
            #answer=message.text
            #bot.send_message(-181158852, answer)
            #log(message, answer)
 if FLAG == True :
     bot.send_message(message.chat.id, answer)
     log(message, answer)

#######для скрипта

@bot.message_handler(content_types=["commands"])
def handle_command(message):
    print("Пришла команда")

@bot.message_handler(content_types=["text"])
def handle_command(message):
    print("Пришло просто сообщение ")

@bot.message_handler(content_types=["document"])
def handle_command(message):
    print("Пришел документ")
    doc = str(message.document.file_id)
    bot.send_document(-181158852, doc)

@bot.message_handler(content_types=["audio"])
def handle_command(message):
    print("Пришла аудиозапись")
    dataudio = str(message.audio.file_id)
    bot.send_audio(-181158852, dataudio)
    bot.send_message(-181158852, dataudio )

@bot.message_handler(content_types=["photo"])
def handle_command(message):
    print("Пришло изображение")

@bot.message_handler(content_types=["sticker"])
def handle_command(message):
    print("Пришел стикер")

while True:
    try:
      bot.polling(none_stop=True)
    except Exception as e:
      logger.error(e)
      time.sleep(200)
