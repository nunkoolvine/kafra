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
from discord.utils import get
global min
global dralast
client = discord.Client()


global channel
global current1
global later1
global current2
global later2
tima11 = 1
tima12 = 1
tima13 = 1

@client.event
async def on_ready():
    print("bot online!")


@client.event
async def on_message(message):
    #print(message.channel)

    if message.content.startswith('/직업') or message.content.startswith('/알림'):
        textrole = ""
        learn = message.content.split(" ")
        vrsize = len(learn)  # 배열크기
        vrsize = int(vrsize)
        for i in range(1, 2):  # 띄어쓰기 한 텍스트들 인식함
            textrole = textrole + learn[i]
            textrole = str(textrole)
#        if message.content.find("엔젤링"):
            #print(textrole)
            role = get(message.guild.roles, name=textrole)
            member = message.author
            #print(member)
            #print(role)
            await member.add_roles(role)

    if message.content.startswith('엔젤링') or message.content.startswith('ㅇㅈㄹ'):
        global on01
        on01 = 0
        await asyncio.sleep(1)
        current1 = datetime.datetime.now()
        textmin = ""
        textsec = ""
        learn = message.content.split(" ")
        vrsize = len(learn)  # 배열크기
        vrsize = int(vrsize)
        #print(message)
        #print(vrsize)

        for i in range(1, 2):  # 띄어쓰기 한 텍스트들 인식함
            textmin = textmin + " " + learn[i]
            #print(Text)


        for i in range(2, 3):  # 띄어쓰기 한 텍스트들 인식함
            textsec = textsec + " " + learn[i]
        

        
        minint = int(textmin)
        min = minint
        #print(min)
        secint = int(textsec)
        sec = secint
        #print(sec)
        current1 = datetime.datetime.now()
        if min * 60 + sec > 900:
            tima11=1
            tima12=1
            tima13=1
        elif min * 60 + sec > 300:
            tima11=0
            tima12=1
            tima13=1
        elif min * 60 + sec > 0:
            tima11=0
            tima12=0
            tima13=1
        later11 = current1 + datetime.timedelta(seconds=min*60+sec-900)
        later12 = current1 + datetime.timedelta(seconds=min*60+sec-300)
        later13 = current1 + datetime.timedelta(seconds=min*60+sec)

        #print(tima11)
        #print(tima12)
        #print(tima13)
        on01 = 1
        while on01 == 1:
            await asyncio.sleep(0.1) 
            current1 =  datetime.datetime.now()
            #print(current1)
            if current1 > later11 and tima11==1:
                commander = discord.utils.get(message.guild.roles, name="엔젤링")
                await message.channel.send("{} 젠까지 15분 남았습니다.".format(commander.mention))
                tima11=0
            if current1 > later12 and tima12==1:
                commander = discord.utils.get(message.guild.roles, name="엔젤링")
                await message.channel.send("{} 젠까지 5분 남았습니다.".format(commander.mention))
                tima12=0
            if current1 > later13 and tima13==1:
                commander = discord.utils.get(message.guild.roles, name="엔젤링")
                await message.channel.send("{}이 포링섬에 나타났습니다.".format(commander.mention))
                tima13=0
                break
    if message.content.startswith('황도') or message.content.startswith('ㅎㄷ'):
        global on02
        on02 = 0
        await asyncio.sleep(1)
        current1 = datetime.datetime.now()
        textmin = ""
        textsec = ""
        learn = message.content.split(" ")
        vrsize = len(learn)  # 배열크기
        vrsize = int(vrsize)
        #print(message)
        #print(vrsize)

        for i in range(1, 2):  # 띄어쓰기 한 텍스트들 인식함
            textmin = textmin + " " + learn[i]
            #print(Text)


        for i in range(2, 3):  # 띄어쓰기 한 텍스트들 인식함
            textsec = textsec + " " + learn[i]
        

        
        minint = int(textmin)
        min = minint
        #print(min)
        secint = int(textsec)
        sec = secint
        #print(sec)
        current1 = datetime.datetime.now()
        if min * 60 + sec > 900:
            tima11=1
            tima12=1
            tima13=1
        elif min * 60 + sec > 300:
            tima11=0
            tima12=1
            tima13=1
        elif min * 60 + sec > 0:
            tima11=0
            tima12=0
            tima13=1
        later11 = current1 + datetime.timedelta(seconds=min*60+sec-900)
        later12 = current1 + datetime.timedelta(seconds=min*60+sec-300)
        later13 = current1 + datetime.timedelta(seconds=min*60+sec)

        #print(tima11)
        #print(tima12)
        #print(tima13)
        on02 = 1
        while on02 == 1:
            await asyncio.sleep(0.1) 
            current1 =  datetime.datetime.now()
            #print(current1)
            if current1 > later11 and tima11==1:
                commander = discord.utils.get(message.guild.roles, name="황금 도둑벌레")
                await message.channel.send("{} 젠까지 15분 남았습니다.".format(commander.mention))
                tima11=0
            if current1 > later12 and tima12==1:
                commander = discord.utils.get(message.guild.roles, name="황금 도둑벌레")
                await message.channel.send("{} 젠까지 5분 남았습니다.".format(commander.mention))
                tima12=0
            if current1 > later13 and tima13==1:
                commander = discord.utils.get(message.guild.roles, name="황금 도둑벌레")
                await message.channel.send("{}가 지하수로 2층에 나타났습니다.".format(commander.mention))
                tima13=0
                break        
    if message.content.startswith('데빌링') or message.content.startswith('데빌링'):
        global on03
        on03 = 0
        await asyncio.sleep(1)
        current1 = datetime.datetime.now()
        textmin = ""
        textsec = ""
        learn = message.content.split(" ")
        vrsize = len(learn)  # 배열크기
        vrsize = int(vrsize)
        #print(message)
        #print(vrsize)

        for i in range(1, 2):  # 띄어쓰기 한 텍스트들 인식함
            textmin = textmin + " " + learn[i]
            #print(Text)


        for i in range(2, 3):  # 띄어쓰기 한 텍스트들 인식함
            textsec = textsec + " " + learn[i]
        

        
        minint = int(textmin)
        min = minint
        #print(min)
        secint = int(textsec)
        sec = secint
        #print(sec)
        current1 = datetime.datetime.now()
        if min * 60 + sec > 900:
            tima11=1
            tima12=1
            tima13=1
        elif min * 60 + sec > 300:
            tima11=0
            tima12=1
            tima13=1
        elif min * 60 + sec > 0:
            tima11=0
            tima12=0
            tima13=1
        later11 = current1 + datetime.timedelta(seconds=min*60+sec-900)
        later12 = current1 + datetime.timedelta(seconds=min*60+sec-300)
        later13 = current1 + datetime.timedelta(seconds=min*60+sec)

        #print(tima11)
        #print(tima12)
        #print(tima13)
        on03 = 1
        while on03 == 1:
            await asyncio.sleep(0.1) 
            current1 =  datetime.datetime.now()
            #print(current1)
            if current1 > later11 and tima11==1:
                commander = discord.utils.get(message.guild.roles, name="데빌링")
                await message.channel.send("{} 젠까지 15분 남았습니다.".format(commander.mention))
                tima11=0
            if current1 > later12 and tima12==1:
                commander = discord.utils.get(message.guild.roles, name="데빌링")
                await message.channel.send("{} 젠까지 5분 남았습니다.".format(commander.mention))
                tima12=0
            if current1 > later13 and tima13==1:
                commander = discord.utils.get(message.guild.roles, name="데빌링")
                await message.channel.send("{}이 포링섬에 나타났습니다.".format(commander.mention))
                tima13=0
                break   
    if message.content.startswith('오히') or message.content.startswith('ㅇㅎ'):
        global on04
        on04 = 0
        await asyncio.sleep(1)
        current1 = datetime.datetime.now()
        textmin = ""
        textsec = ""
        learn = message.content.split(" ")
        vrsize = len(learn)  # 배열크기
        vrsize = int(vrsize)
        #print(message)
        #print(vrsize)

        for i in range(1, 2):  # 띄어쓰기 한 텍스트들 인식함
            textmin = textmin + " " + learn[i]
            #print(Text)


        for i in range(2, 3):  # 띄어쓰기 한 텍스트들 인식함
            textsec = textsec + " " + learn[i]
        

        
        minint = int(textmin)
        min = minint
        #print(min)
        secint = int(textsec)
        sec = secint
        #print(sec)
        current1 = datetime.datetime.now()
        if min * 60 + sec > 900:
            tima11=1
            tima12=1
            tima13=1
        elif min * 60 + sec > 300:
            tima11=0
            tima12=1
            tima13=1
        elif min * 60 + sec > 0:
            tima11=0
            tima12=0
            tima13=1
        later11 = current1 + datetime.timedelta(seconds=min*60+sec-900)
        later12 = current1 + datetime.timedelta(seconds=min*60+sec-300)
        later13 = current1 + datetime.timedelta(seconds=min*60+sec)

        #print(tima11)
        #print(tima12)
        #print(tima13)
        on04 = 1
        while on04 == 1:
            await asyncio.sleep(0.1) 
            current1 =  datetime.datetime.now()
            #print(current1)
            if current1 > later11 and tima11==1:
                commander = discord.utils.get(message.guild.roles, name="오크 히어로")
                await message.channel.send("{} 젠까지 15분 남았습니다.".format(commander.mention))
                tima11=0
            if current1 > later12 and tima12==1:
                commander = discord.utils.get(message.guild.roles, name="오크 히어로")
                await message.channel.send("{} 젠까지 5분 남았습니다.".format(commander.mention))
                tima12=0
            if current1 > later13 and tima13==1:
                commander = discord.utils.get(message.guild.roles, name="오크 히어로")
                await message.channel.send("{}가 오크 마을에 나타났습니다.".format(commander.mention))
                tima13=0
                break
    if message.content.startswith('마야') or message.content.startswith('ㅁㅇ'):
        global on05
        on05 = 0
        await asyncio.sleep(1)
        current1 = datetime.datetime.now()
        textmin = ""
        textsec = ""
        learn = message.content.split(" ")
        vrsize = len(learn)  # 배열크기
        vrsize = int(vrsize)
        #print(message)
        #print(vrsize)

        for i in range(1, 2):  # 띄어쓰기 한 텍스트들 인식함
            textmin = textmin + " " + learn[i]
            #print(Text)


        for i in range(2, 3):  # 띄어쓰기 한 텍스트들 인식함
            textsec = textsec + " " + learn[i]
        

        
        minint = int(textmin)
        min = minint
        #print(min)
        secint = int(textsec)
        sec = secint
        #print(sec)
        current1 = datetime.datetime.now()
        if min * 60 + sec > 900:
            tima11=1
            tima12=1
            tima13=1
        elif min * 60 + sec > 300:
            tima11=0
            tima12=1
            tima13=1
        elif min * 60 + sec > 0:
            tima11=0
            tima12=0
            tima13=1
        later11 = current1 + datetime.timedelta(seconds=min*60+sec-900)
        later12 = current1 + datetime.timedelta(seconds=min*60+sec-300)
        later13 = current1 + datetime.timedelta(seconds=min*60+sec)

        #print(tima11)
        #print(tima12)
        #print(tima13)
        on05 = 1
        commander = discord.utils.get(message.guild.roles, name="마야")
        while on05 == 1:
            await asyncio.sleep(0.1) 
            current1 =  datetime.datetime.now()
            #print(current1)
            if current1 > later11 and tima11==1:
                await message.channel.send("{} 젠까지 15분 남았습니다.".format(commander.mention))
                tima11=0
            if current1 > later12 and tima12==1:
                await message.channel.send("{} 젠까지 5분 남았습니다.".format(commander.mention))
                tima12=0
            if current1 > later13 and tima13==1:
                await message.channel.send("{}가 개미 지옥에 나타났습니다.".format(commander.mention))
                tima13=0
                break
    if message.content.startswith('오로') or message.content.startswith('ㅇㄹ'):
        global on06
        on06 = 0
        await asyncio.sleep(1)
        current1 = datetime.datetime.now()
        textmin = ""
        textsec = ""
        learn = message.content.split(" ")
        vrsize = len(learn)  # 배열크기
        vrsize = int(vrsize)
        #print(message)
        #print(vrsize)

        for i in range(1, 2):  # 띄어쓰기 한 텍스트들 인식함
            textmin = textmin + " " + learn[i]
            #print(Text)


        for i in range(2, 3):  # 띄어쓰기 한 텍스트들 인식함
            textsec = textsec + " " + learn[i]
        

        
        minint = int(textmin)
        min = minint
        #print(min)
        secint = int(textsec)
        sec = secint
        #print(sec)
        current1 = datetime.datetime.now()
        if min * 60 + sec > 900:
            tima11=1
            tima12=1
            tima13=1
        elif min * 60 + sec > 300:
            tima11=0
            tima12=1
            tima13=1
        elif min * 60 + sec > 0:
            tima11=0
            tima12=0
            tima13=1
        later11 = current1 + datetime.timedelta(seconds=min*60+sec-900)
        later12 = current1 + datetime.timedelta(seconds=min*60+sec-300)
        later13 = current1 + datetime.timedelta(seconds=min*60+sec)

        #print(tima11)
        #print(tima12)
        #print(tima13)
        on06 = 1
        commander = discord.utils.get(message.guild.roles, name="오크 로드")
        while on06 == 1:
            await asyncio.sleep(0.1) 
            current1 =  datetime.datetime.now()
            #print(current1)
            if current1 > later11 and tima11==1:
                await message.channel.send("{} 젠까지 15분 남았습니다.".format(commander.mention))
                tima11=0
            if current1 > later12 and tima12==1:
                await message.channel.send("{} 젠까지 5분 남았습니다.".format(commander.mention))
                tima12=0
            if current1 > later13 and tima13==1:
                await message.channel.send("{}가 오크 마을에 나타났습니다.".format(commander.mention))
                tima13=0
                break
    if message.content.startswith('고리') or message.content.startswith('ㄱㄹ'):
        global on07
        on07 = 0
        await asyncio.sleep(1)
        current1 = datetime.datetime.now()
        textmin = ""
        textsec = ""
        learn = message.content.split(" ")
        vrsize = len(learn)  # 배열크기
        vrsize = int(vrsize)
        #print(message)
        #print(vrsize)

        for i in range(1, 2):  # 띄어쓰기 한 텍스트들 인식함
            textmin = textmin + " " + learn[i]
            #print(Text)


        for i in range(2, 3):  # 띄어쓰기 한 텍스트들 인식함
            textsec = textsec + " " + learn[i]
        

        
        minint = int(textmin)
        min = minint
        #print(min)
        secint = int(textsec)
        sec = secint
        #print(sec)
        current1 = datetime.datetime.now()
        if min * 60 + sec > 900:
            tima11=1
            tima12=1
            tima13=1
        elif min * 60 + sec > 300:
            tima11=0
            tima12=1
            tima13=1
        elif min * 60 + sec > 0:
            tima11=0
            tima12=0
            tima13=1
        later11 = current1 + datetime.timedelta(seconds=min*60+sec-900)
        later12 = current1 + datetime.timedelta(seconds=min*60+sec-300)
        later13 = current1 + datetime.timedelta(seconds=min*60+sec)

        #print(tima11)
        #print(tima12)
        #print(tima13)
        on07 = 1
        commander = discord.utils.get(message.guild.roles, name="고블린 리더")
        while on07 == 1:
            await asyncio.sleep(0.1) 
            current1 =  datetime.datetime.now()
            #print(current1)
            if current1 > later11 and tima11==1:
                await message.channel.send("{} 젠까지 15분 남았습니다.".format(commander.mention))
                tima11=0
            if current1 > later12 and tima12==1:
                await message.channel.send("{} 젠까지 5분 남았습니다.".format(commander.mention))
                tima12=0
            if current1 > later13 and tima13==1:
                await message.channel.send("{}가 고블린 숲에 나타났습니다.".format(commander.mention))
                tima13=0
                break
    if message.content.startswith('드레'):
        global on08
        on08 = 0
        await asyncio.sleep(1)
        current1 = datetime.datetime.now()
        textmin = ""
        textsec = ""
        learn = message.content.split(" ")
        vrsize = len(learn)  # 배열크기
        vrsize = int(vrsize)
        #print(message)
        #print(vrsize)

        for i in range(1, 2):  # 띄어쓰기 한 텍스트들 인식함
            textmin = textmin + " " + learn[i]
            #print(Text)


        for i in range(2, 3):  # 띄어쓰기 한 텍스트들 인식함
            textsec = textsec + " " + learn[i]
        

        
        minint = int(textmin)
        min = minint
        #print(min)
        secint = int(textsec)
        sec = secint
        #print(sec)
        current1 = datetime.datetime.now()
        if min * 60 + sec > 900:
            tima11=1
            tima12=1
            tima13=1
        elif min * 60 + sec > 300:
            tima11=0
            tima12=1
            tima13=1
        elif min * 60 + sec > 0:
            tima11=0
            tima12=0
            tima13=1
        later11 = current1 + datetime.timedelta(seconds=min*60+sec-900)
        later12 = current1 + datetime.timedelta(seconds=min*60+sec-300)
        later13 = current1 + datetime.timedelta(seconds=min*60+sec)

        #print(tima11)
        #print(tima12)
        #print(tima13)
        on08 = 1
        commander = discord.utils.get(message.guild.roles, name="드레이크")
        while on08 == 1:
            await asyncio.sleep(0.1) 
            current1 =  datetime.datetime.now()
            #print(current1)
            if current1 > later11 and tima11==1:
                await message.channel.send("{} 젠까지 15분 남았습니다.".format(commander.mention))
                tima11=0
            if current1 > later12 and tima12==1:
                await message.channel.send("{} 젠까지 5분 남았습니다.".format(commander.mention))
                tima12=0
            if current1 > later13 and tima13==1:
                await message.channel.send("{}가 침몰선 1층에 나타났습니다.".format(commander.mention))
                tima13=0
                break
    if message.content.startswith('에드가') or message.content.startswith('ㅇㄷ'):
        global on09
        on09 = 0
        await asyncio.sleep(1)
        current1 = datetime.datetime.now()
        textmin = ""
        textsec = ""
        learn = message.content.split(" ")
        vrsize = len(learn)  # 배열크기
        vrsize = int(vrsize)
        #print(message)
        #print(vrsize)

        for i in range(1, 2):  # 띄어쓰기 한 텍스트들 인식함
            textmin = textmin + " " + learn[i]
            #print(Text)


        for i in range(2, 3):  # 띄어쓰기 한 텍스트들 인식함
            textsec = textsec + " " + learn[i]
        

        
        minint = int(textmin)
        min = minint
        #print(min)
        secint = int(textsec)
        sec = secint
        #print(sec)
        current1 = datetime.datetime.now()
        if min * 60 + sec > 900:
            tima11=1
            tima12=1
            tima13=1
        elif min * 60 + sec > 300:
            tima11=0
            tima12=1
            tima13=1
        elif min * 60 + sec > 0:
            tima11=0
            tima12=0
            tima13=1
        later11 = current1 + datetime.timedelta(seconds=min*60+sec-900)
        later12 = current1 + datetime.timedelta(seconds=min*60+sec-300)
        later13 = current1 + datetime.timedelta(seconds=min*60+sec)

        #print(tima11)
        #print(tima12)
        #print(tima13)
        on09 = 1
        commander = discord.utils.get(message.guild.roles, name="에드가")
        while on09 == 1:
            await asyncio.sleep(0.1) 
            current1 =  datetime.datetime.now()
            #print(current1)
            if current1 > later11 and tima11==1:
                await message.channel.send("{} 젠까지 15분 남았습니다.".format(commander.mention))
                tima11=0
            if current1 > later12 and tima12==1:
                await message.channel.send("{} 젠까지 5분 남았습니다.".format(commander.mention))
                tima12=0
            if current1 > later13 and tima13==1:
                await message.channel.send("{}가 페이욘 숲 깊은 곳에 나타났습니다.".format(commander.mention))
                tima13=0
                break
    if message.content.startswith('미스') or message.content.startswith('ㅁㅅ'):
        global on10
        on10 = 0
        await asyncio.sleep(1)
        current1 = datetime.datetime.now()
        textmin = ""
        textsec = ""
        learn = message.content.split(" ")
        vrsize = len(learn)  # 배열크기
        vrsize = int(vrsize)
        #print(message)
        #print(vrsize)

        for i in range(1, 2):  # 띄어쓰기 한 텍스트들 인식함
            textmin = textmin + " " + learn[i]
            #print(Text)


        for i in range(2, 3):  # 띄어쓰기 한 텍스트들 인식함
            textsec = textsec + " " + learn[i]
        

        
        minint = int(textmin)
        min = minint
        #print(min)
        secint = int(textsec)
        sec = secint
        #print(sec)
        current1 = datetime.datetime.now()
        if min * 60 + sec > 900:
            tima11=1
            tima12=1
            tima13=1
        elif min * 60 + sec > 300:
            tima11=0
            tima12=1
            tima13=1
        elif min * 60 + sec > 0:
            tima11=0
            tima12=0
            tima13=1
        later11 = current1 + datetime.timedelta(seconds=min*60+sec-900)
        later12 = current1 + datetime.timedelta(seconds=min*60+sec-300)
        later13 = current1 + datetime.timedelta(seconds=min*60+sec)

        #print(tima11)
        #print(tima12)
        #print(tima13)
        on10 = 1
        commander = discord.utils.get(message.guild.roles, name="미스트레스")
        while on10 == 1:
            await asyncio.sleep(0.1) 
            current1 =  datetime.datetime.now()
            #print(current1)
            if current1 > later11 and tima11==1:
                await message.channel.send("{} 젠까지 15분 남았습니다.".format(commander.mention))
                tima11=0
            if current1 > later12 and tima12==1:
                await message.channel.send("{} 젠까지 5분 남았습니다.".format(commander.mention))
                tima12=0
            if current1 > later13 and tima13==1:
                await message.channel.send("{}가 화원에 나타났습니다.".format(commander.mention))
                tima13=0
                break
    if message.content.startswith('오시') or message.content.startswith('ㅇㅅ'):
        global on11
        on11 = 0
        await asyncio.sleep(1)
        current1 = datetime.datetime.now()
        textmin = ""
        textsec = ""
        learn = message.content.split(" ")
        vrsize = len(learn)  # 배열크기
        vrsize = int(vrsize)
        #print(message)
        #print(vrsize)

        for i in range(1, 2):  # 띄어쓰기 한 텍스트들 인식함
            textmin = textmin + " " + learn[i]
            #print(Text)


        for i in range(2, 3):  # 띄어쓰기 한 텍스트들 인식함
            textsec = textsec + " " + learn[i]
        

        
        minint = int(textmin)
        min = minint
        #print(min)
        secint = int(textsec)
        sec = secint
        #print(sec)
        current1 = datetime.datetime.now()
        if min * 60 + sec > 900:
            tima11=1
            tima12=1
            tima13=1
        elif min * 60 + sec > 300:
            tima11=0
            tima12=1
            tima13=1
        elif min * 60 + sec > 0:
            tima11=0
            tima12=0
            tima13=1
        later11 = current1 + datetime.timedelta(seconds=min*60+sec-900)
        later12 = current1 + datetime.timedelta(seconds=min*60+sec-300)
        later13 = current1 + datetime.timedelta(seconds=min*60+sec)

        #print(tima11)
        #print(tima12)
        #print(tima13)
        on11 = 1
        commander = discord.utils.get(message.guild.roles, name="오시리스")
        while on11 == 1:
            await asyncio.sleep(0.1) 
            current1 =  datetime.datetime.now()
            #print(current1)
            if current1 > later11 and tima11==1:
                await message.channel.send("{} 젠까지 15분 남았습니다.".format(commander.mention))
                tima11=0
            if current1 > later12 and tima12==1:
                await message.channel.send("{} 젠까지 5분 남았습니다.".format(commander.mention))
                tima12=0
            if current1 > later13 and tima13==1:
                await message.channel.send("{}가 피라미드 3층에 나타났습니다.".format(commander.mention))
                tima13=0
                break
    if message.content.startswith('프리') or message.content.startswith('ㅍㄹㅇㄴ') or message.content.startswith('ㅇㄴ'):
        global on12
        on12 = 0
        await asyncio.sleep(1)
        current1 = datetime.datetime.now()
        textmin = ""
        textsec = ""
        learn = message.content.split(" ")
        vrsize = len(learn)  # 배열크기
        vrsize = int(vrsize)
        #print(message)
        #print(vrsize)

        for i in range(1, 2):  # 띄어쓰기 한 텍스트들 인식함
            textmin = textmin + " " + learn[i]
            #print(Text)


        for i in range(2, 3):  # 띄어쓰기 한 텍스트들 인식함
            textsec = textsec + " " + learn[i]
        

        
        minint = int(textmin)
        min = minint
        #print(min)
        secint = int(textsec)
        sec = secint
        #print(sec)
        current1 = datetime.datetime.now()
        if min * 60 + sec > 900:
            tima11=1
            tima12=1
            tima13=1
        elif min * 60 + sec > 300:
            tima11=0
            tima12=1
            tima13=1
        elif min * 60 + sec > 0:
            tima11=0
            tima12=0
            tima13=1
        later11 = current1 + datetime.timedelta(seconds=min*60+sec-900)
        later12 = current1 + datetime.timedelta(seconds=min*60+sec-300)
        later13 = current1 + datetime.timedelta(seconds=min*60+sec)

        #print(tima11)
        #print(tima12)
        #print(tima13)
        on12 = 1
        commander = discord.utils.get(message.guild.roles, name="프리오니")
        while on12 == 1:
            await asyncio.sleep(0.1) 
            current1 =  datetime.datetime.now()
            #print(current1)
            if current1 > later11 and tima11==1:
                await message.channel.send("{} 젠까지 15분 남았습니다.".format(commander.mention))
                tima11=0
            if current1 > later12 and tima12==1:
                await message.channel.send("{} 젠까지 5분 남았습니다.".format(commander.mention))
                tima12=0
            if current1 > later13 and tima13==1:
                await message.channel.send("{}가 소그라트 남부에 나타났습니다.".format(commander.mention))
                tima13=0
                break
    if message.content.startswith('월야화') or message.content.startswith('ㅇㅇㅎ'):
        global on13
        on13 = 0
        await asyncio.sleep(1)
        current1 = datetime.datetime.now()
        textmin = ""
        textsec = ""
        learn = message.content.split(" ")
        vrsize = len(learn)  # 배열크기
        vrsize = int(vrsize)
        #print(message)
        #print(vrsize)

        for i in range(1, 2):  # 띄어쓰기 한 텍스트들 인식함
            textmin = textmin + " " + learn[i]
            #print(Text)


        for i in range(2, 3):  # 띄어쓰기 한 텍스트들 인식함
            textsec = textsec + " " + learn[i]
        

        
        minint = int(textmin)
        min = minint
        #print(min)
        secint = int(textsec)
        sec = secint
        #print(sec)
        current1 = datetime.datetime.now()
        if min * 60 + sec > 900:
            tima11=1
            tima12=1
            tima13=1
        elif min * 60 + sec > 300:
            tima11=0
            tima12=1
            tima13=1
        elif min * 60 + sec > 0:
            tima11=0
            tima12=0
            tima13=1
        later11 = current1 + datetime.timedelta(seconds=min*60+sec-900)
        later12 = current1 + datetime.timedelta(seconds=min*60+sec-300)
        later13 = current1 + datetime.timedelta(seconds=min*60+sec)

        #print(tima11)
        #print(tima12)
        #print(tima13)
        on13 = 1
        commander = discord.utils.get(message.guild.roles, name="월야화")
        while on13 == 1:
            await asyncio.sleep(0.1) 
            current1 =  datetime.datetime.now()
            #print(current1)
            if current1 > later11 and tima11==1:
                await message.channel.send("{} 젠까지 15분 남았습니다.".format(commander.mention))
                tima11=0
            if current1 > later12 and tima12==1:
                await message.channel.send("{} 젠까지 5분 남았습니다.".format(commander.mention))
                tima12=0
            if current1 > later13 and tima13==1:
                await message.channel.send("{}가 페이욘 동굴 3층에 나타났습니다.".format(commander.mention))
                tima13=0
                break
    if message.content.startswith('드라') or message.content.startswith('ㄷㄹ'):
        global on14
        on14 = 0
        await asyncio.sleep(1)
        current1 = datetime.datetime.now()
        textmin = ""
        textsec = ""
        learn = message.content.split(" ")
        vrsize = len(learn)  # 배열크기
        vrsize = int(vrsize)
        #print(message)
        #print(vrsize)

        for i in range(1, 2):  # 띄어쓰기 한 텍스트들 인식함
            textmin = textmin + " " + learn[i]
            #print(Text)


        for i in range(2, 3):  # 띄어쓰기 한 텍스트들 인식함
            textsec = textsec + " " + learn[i]
        

        
        minint = int(textmin)
        min = minint
        #print(min)
        secint = int(textsec)
        sec = secint
        #print(sec)
        current1 = datetime.datetime.now()
        if min * 60 + sec > 900:
            tima11=1
            tima12=1
            tima13=1
        elif min * 60 + sec > 300:
            tima11=0
            tima12=1
            tima13=1
        elif min * 60 + sec > 0:
            tima11=0
            tima12=0
            tima13=1
        later11 = current1 + datetime.timedelta(seconds=min*60+sec-900)
        later12 = current1 + datetime.timedelta(seconds=min*60+sec-300)
        later13 = current1 + datetime.timedelta(seconds=min*60+sec)

        #print(tima11)
        #print(tima12)
        #print(tima13)
        on14 = 1
        while on14 == 1:
            await asyncio.sleep(0.1) 
            current1 =  datetime.datetime.now()
            #print(current1)
            if current1 > later11 and tima11==1:
                commander = discord.utils.get(message.guild.roles, name="드라큐라")
                await message.channel.send("{} 젠까지 15분 남았습니다.".format(commander.mention))
                tima11=0
            if current1 > later12 and tima12==1:
                commander = discord.utils.get(message.guild.roles, name="드라큐라")
                await message.channel.send("{} 젠까지 5분 남았습니다.".format(commander.mention))
                tima12=0
            if current1 > later13 and tima13==1:
                commander = discord.utils.get(message.guild.roles, name="드라큐라")
                await message.channel.send("{}가 게펜 탑 2층에 나타났습니다.".format(commander.mention))
                tima13=0
                break
    if message.content.startswith('도플') or message.content.startswith('ㄷㅍ'):
        global on15
        on15 = 0
        await asyncio.sleep(1)
        current1 = datetime.datetime.now()
        textmin = ""
        textsec = ""
        learn = message.content.split(" ")
        vrsize = len(learn)  # 배열크기
        vrsize = int(vrsize)
        #print(message)
        #print(vrsize)

        for i in range(1, 2):  # 띄어쓰기 한 텍스트들 인식함
            textmin = textmin + " " + learn[i]
            #print(Text)


        for i in range(2, 3):  # 띄어쓰기 한 텍스트들 인식함
            textsec = textsec + " " + learn[i]
        

        
        minint = int(textmin)
        min = minint
        #print(min)
        secint = int(textsec)
        sec = secint
        #print(sec)
        current1 = datetime.datetime.now()
        if min * 60 + sec > 900:
            tima11=1
            tima12=1
            tima13=1
        elif min * 60 + sec > 300:
            tima11=0
            tima12=1
            tima13=1
        elif min * 60 + sec > 0:
            tima11=0
            tima12=0
            tima13=1
        later11 = current1 + datetime.timedelta(seconds=min*60+sec-900)
        later12 = current1 + datetime.timedelta(seconds=min*60+sec-300)
        later13 = current1 + datetime.timedelta(seconds=min*60+sec)

        #print(tima11)
        #print(tima12)
        #print(tima13)
        on15 = 1
        commander = discord.utils.get(message.guild.roles, name="도플갱어")
        while on15 == 1:
            await asyncio.sleep(0.1) 
            current1 =  datetime.datetime.now()
            #print(current1)
            if current1 > later11 and tima11==1:
                await message.channel.send("{} 젠까지 15분 남았습니다.".format(commander.mention))
                tima11=0
            if current1 > later12 and tima12==1:
                await message.channel.send("{} 젠까지 5분 남았습니다.".format(commander.mention))
                tima12=0
            if current1 > later13 and tima13==1:
                await message.channel.send("{}가 게펜탑 3층에 나타났습니다.".format(commander.mention))
                tima13=0
                break
    if message.content.startswith('파라오') or message.content.startswith('ㅍㄹㅇ'):
        global on16
        on16 = 0
        await asyncio.sleep(1)
        current1 = datetime.datetime.now()
        textmin = ""
        textsec = ""
        learn = message.content.split(" ")
        vrsize = len(learn)  # 배열크기
        vrsize = int(vrsize)
        #print(message)
        #print(vrsize)

        for i in range(1, 2):  # 띄어쓰기 한 텍스트들 인식함
            textmin = textmin + " " + learn[i]
            #print(Text)


        for i in range(2, 3):  # 띄어쓰기 한 텍스트들 인식함
            textsec = textsec + " " + learn[i]
        

        
        minint = int(textmin)
        min = minint
        #print(min)
        secint = int(textsec)
        sec = secint
        #print(sec)
        current1 = datetime.datetime.now()
        if min * 60 + sec > 900:
            tima11=1
            tima12=1
            tima13=1
        elif min * 60 + sec > 300:
            tima11=0
            tima12=1
            tima13=1
        elif min * 60 + sec > 0:
            tima11=0
            tima12=0
            tima13=1
        later11 = current1 + datetime.timedelta(seconds=min*60+sec-900)
        later12 = current1 + datetime.timedelta(seconds=min*60+sec-300)
        later13 = current1 + datetime.timedelta(seconds=min*60+sec)

        #print(tima11)
        #print(tima12)
        #print(tima13)
        on16 = 1
        commander = discord.utils.get(message.guild.roles, name="파라오")
        while on16 == 1:
            await asyncio.sleep(0.1) 
            current1 =  datetime.datetime.now()
            #print(current1)
            if current1 > later11 and tima11==1:
                await message.channel.send("{} 젠까지 15분 남았습니다.".format(commander.mention))
                tima11=0
            if current1 > later12 and tima12==1:
                await message.channel.send("{} 젠까지 5분 남았습니다.".format(commander.mention))
                tima12=0
            if current1 > later13 and tima13==1:
                await message.channel.send("{}가 스핑크스 지하 2층에 나타났습니다.".format(commander.mention))
                tima13=0
                break
    if message.content.startswith('바포') or message.content.startswith('ㅂㅍ'):
        global on17
        on17 = 0
        await asyncio.sleep(1)
        current1 = datetime.datetime.now()
        textmin = ""
        textsec = ""
        learn = message.content.split(" ")
        vrsize = len(learn)  # 배열크기
        vrsize = int(vrsize)
        #print(message)
        #print(vrsize)

        for i in range(1, 2):  # 띄어쓰기 한 텍스트들 인식함
            textmin = textmin + " " + learn[i]
            #print(Text)


        for i in range(2, 3):  # 띄어쓰기 한 텍스트들 인식함
            textsec = textsec + " " + learn[i]
        

        
        minint = int(textmin)
        min = minint
        #print(min)
        secint = int(textsec)
        sec = secint
        #print(sec)
        current1 = datetime.datetime.now()
        if min * 60 + sec > 900:
            tima11=1
            tima12=1
            tima13=1
        elif min * 60 + sec > 300:
            tima11=0
            tima12=1
            tima13=1
        elif min * 60 + sec > 0:
            tima11=0
            tima12=0
            tima13=1
        later11 = current1 + datetime.timedelta(seconds=min*60+sec-900)
        later12 = current1 + datetime.timedelta(seconds=min*60+sec-300)
        later13 = current1 + datetime.timedelta(seconds=min*60+sec)

        #print(tima11)
        #print(tima12)
        #print(tima13)
        on17 = 1
        commander = discord.utils.get(message.guild.roles, name="바포메트")
        while on17 == 1:
            await asyncio.sleep(0.1) 
            current1 =  datetime.datetime.now()
            #print(current1)
            if current1 > later11 and tima11==1:
                await message.channel.send("{} 젠까지 15분 남았습니다.".format(commander.mention))
                tima11=0
            if current1 > later12 and tima12==1:
                await message.channel.send("{} 젠까지 5분 남았습니다.".format(commander.mention))
                tima12=0
            if current1 > later13 and tima13==1:
                await message.channel.send("{}가 미궁 숲 1층에 나타났습니다.".format(commander.mention))
                tima13=0
                break
                                    
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)

