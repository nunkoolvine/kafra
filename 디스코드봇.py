import discord
import asyncio
import threading
import random
import openpyxl
from discord import Member
from discord.ext import commands
from urllib.request import urlopen, Request
import schedule
import time
import datetime
import os
global min
global dralast
client = discord.Client()
current1 = datetime.datetime.now()
current2 = datetime.datetime.now()
on1=1
on2=1
tima11 = 1
tima12 = 1
tima13 = 1
@client.event
async def on_ready():
    print("bot online!")



@client.event
async def on_message(message):
    #print(message.channel)
    global channel
    global on1
    global on2
    global current1
    global later1
    global current2
    global later2
    global tima11
    global tima12
    global tima13
    if message.content.startswith('드라'):
        on1 = 0
        await asyncio.sleep(1)
        tima11 = 1
        tima12 = 1
        tima13 = 1
        current1 =  datetime.datetime.now()
        textmin = ""
        textsec = ""
        learn = message.content.split(" ")
        vrsize = len(learn)  # 배열크기
        vrsize = int(vrsize)
        #print(message)
        print(vrsize)

        for i in range(1, 2):  # 띄어쓰기 한 텍스트들 인식함
            textmin = textmin + " " + learn[i]
            #print(Text)


        for i in range(2, 3):  # 띄어쓰기 한 텍스트들 인식함
            textsec = textsec + " " + learn[i]


        

        
        minint = int(textmin)
        min = minint
        print(min)
        secint = int(textsec)
        sec = secint
        print(sec)
        current1 =  datetime.datetime.now()
        later11 = current1 + datetime.timedelta(seconds=min*60+sec-900)
        later12 = current1 + datetime.timedelta(seconds=min*60+sec-300)
        later13 = current1 + datetime.timedelta(seconds=min*60+sec)

        
        print('later1')
        print(later1)
        on1 = 1
        while on1 == 1:
            await asyncio.sleep(0.1) 
            current1 =  datetime.datetime.now()
            print(current1)
            if current1 > later11 and tima11==1:
                commander = discord.utils.get(message.guild.roles, name="드라큐라")
                await message.channel.send("{} 갱신까지 5분 남았습니다.".format(commander.mention))
                tima11=0
                break
            if current1 > later12 and tima12==1:
                commander = discord.utils.get(message.guild.roles, name="드라큐라")
                await message.channel.send("{} 갱신까지 5분 남았습니다.".format(commander.mention))
                tima12=0
                break
            if current1 > later13 and tima13==1:
                commander = discord.utils.get(message.guild.roles, name="드라큐라")
                await message.channel.send("{} 갱신까지 5분 남았습니다.".format(commander.mention))
                tima13=0
                break


    if message.content.startswith('에드가'):
        on2 = 0
        await asyncio.sleep(1) 
        current2 =  datetime.datetime.now()
        textmin = ""
        textsec = ""
        learn = message.content.split(" ")
        vrsize = len(learn)  # 배열크기
        vrsize = int(vrsize)
        #print(message)
        print(vrsize)

        for i in range(1, 2):  # 띄어쓰기 한 텍스트들 인식함
            textmin = textmin + " " + learn[i]
            #print(Text)


        for i in range(2, 3):  # 띄어쓰기 한 텍스트들 인식함
            textsec = textsec + " " + learn[i]


        

        
        minint = int(textmin)
        min = minint
        print(min)
        secint = int(textsec)
        sec = secint
        print(sec)
        current2 =  datetime.datetime.now()
        later2 = current2 + datetime.timedelta(seconds=min*60+sec-300)
        
        
        #await client.send_message(channel,'daracula is about to come back.')

        #threading.Timer(aasdf,draann)
        print('later2')
        print(later2)
        on2 = 1
        while on2 == 1:
            await asyncio.sleep(0.1) 
            current2 =  datetime.datetime.now()
            print(current2)
            if current2 > later2:
                commander = discord.utils.get(message.guild.roles, name="에드가")
                await message.channel.send("{} 갱신까지 5분 남았습니다.".format(commander.mention))
                break


#       """ if min*60+sec > 595
#            await asyncio.sleep((min-10)*60+sec)
#
#        if min*60+sec > 295
#            await asyncio.sleep(300)# 이거 생각해보니까 마지막거가 아니고 맨 나중에 끝나는 거 위주로 됨..
#        
#            if(count1 == countt1):
#                commander = discord.utils.get(message.guild.roles, name="드라큐라")
#                await message.channel.send("{} 갱신까지 5분 남았습니다.".format(commander.mention))
#                count1 = 0
#                countt1 = 1
#            else:
#                countt1 += 1
#        else:
            
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)

