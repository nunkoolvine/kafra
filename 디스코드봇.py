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
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.utils import get
sched = AsyncIOScheduler()
global min
global dralast
client = discord.Client()

global channel
global current1
global current2
tima11 = 1
tima12 = 1
tima13 = 1

async def monmorning():
    channell = client.get_channel(768663062449750046)
    guildd = client.get_guild(730294881020280873)
    dailyevent = discord.utils.get(guildd.roles, name="이벤트")
    await channell.send("{} 월요일에는 팀 데스매치가 20:50~21:30에 진행됩니다.".format(dailyevent.mention))
async def tuemorning():
    channell = client.get_channel(768663062449750046)
    guildd = client.get_guild(730294881020280873)
    dailyevent = discord.utils.get(guildd.roles, name="이벤트")
    await channell.send("{} 화요일에는 길드 파티가 20:00~20:20에, 극한 도전이 20:30~22:00에 진행됩니다.".format(dailyevent.mention))
async def wedmorning():
    channell = client.get_channel(768663062449750046)
    guildd = client.get_guild(730294881020280873)
    dailyevent = discord.utils.get(guildd.roles, name="이벤트")
    await channell.send("{} 수요일에는 패션 주간지가 05:00~24:00에, 길드 매칭전이 20:30~21:20에 진행됩니다.".format(dailyevent.mention))
async def thumorning():
    channell = client.get_channel(768663062449750046)
    guildd = client.get_guild(730294881020280873)
    dailyevent = discord.utils.get(guildd.roles, name="이벤트")
    await channell.send("{} 목요일에는 길드 파티가 20:00~20:20에, 극한 도전이 20:30~22:00에 진행됩니다.".format(dailyevent.mention))
async def frimorning():
    channell = client.get_channel(768663062449750046)
    guildd = client.get_guild(730294881020280873)
    dailyevent = discord.utils.get(guildd.roles, name="이벤트")
    await channell.send("{} 금요일에는 길드 사냥이 20:05부터, 팀 데스매치가 20:50~21:30에 진행됩니다.".format(dailyevent.mention))
async def satmorning():
    channell = client.get_channel(768663062449750046)
    guildd = client.get_guild(730294881020280873)
    dailyevent = discord.utils.get(guildd.roles, name="이벤트")
    await channell.send("{} 토요일에는 2인 이그드라실이 10:00~24:00에, 주말 길드 파티가 20:00~20:20에, 전장이 12:50~14:30과 21:20~23:00에 진행됩니다. 또, 아직 1인 이그드라실을 한번도 안 했다면 2회 완료하기 위해서라면 반드시 1인 이그드라실을 해야하는 날입니다.".format(dailyevent.mention))
async def sunmorning():
    channell = client.get_channel(768663062449750046)
    guildd = client.get_guild(730294881020280873)
    dailyevent = discord.utils.get(guildd.roles, name="이벤트")
    await channell.send("{} 일요일에는 2인 이그드라실이 10:00~24:00에, 무도회가 20:00~20:30에, 길드 사냥이 20:30부터, 전장이 12:50~14:30과 21:20~23:00에 진행됩니다. 또, 1인 이그드라실과 무한의 탑이 초기화되는 마지막 날입니다.".format(dailyevent.mention))



sched.add_job(monmorning,'cron', day_of_week = 'mon', hour ='10', minute = '0' )
sched.add_job(tuemorning,'cron', day_of_week = 'tue', hour ='10', minute = '0' )
sched.add_job(wedmorning,'cron', day_of_week = 'wed', hour ='10', minute = '0' )
sched.add_job(thumorning,'cron', day_of_week = 'thu', hour ='10', minute = '0' )
sched.add_job(frimorning,'cron', day_of_week = 'fri', hour ='10', minute = '0' )
sched.add_job(satmorning,'cron', day_of_week = 'sat', hour ='14', minute = '16' )
sched.add_job(sunmorning,'cron', day_of_week = 'sun', hour ='10', minute = '0' )
sched.start()
@client.event
async def on_ready():
    print("bot online!")


@client.event
async def on_message(message):
    if message.author == client.user: # 만약 메시지를 보낸 사람과 봇이 서로 같을 때 
        return
    if message.content.startswith('ㅇㅂㅌ?') or message.content.startswith('이벤트?'):
        now = time.localtime()
        week = ( '월', '화', '수', '목', '금', '토', '일' )
        if week[now.tm_wday] == '월':
            await message.channel.send("월요일에는 팀 데스매치가 20:50~21:30에 진행됩니다.")
        if week[now.tm_wday] == '화':
            await message.channel.send("화요일에는 길드 파티가 20:00~20:20에, 극한 도전이 20:30~22:00에 진행됩니다.")
        if week[now.tm_wday] == '수':
            await message.channel.send("수요일에는 패션 주간지가 05:00~24:00에, 길드 매칭전이 20:30~21:20에 진행됩니다.")
        if week[now.tm_wday] == '목':
            await message.channel.send("목요일에는 길드 파티가 20:00~20:20에, 극한 도전이 20:30~22:00에 진행됩니다.")
        if week[now.tm_wday] == '금':
            await message.channel.send("금요일에는 길드 사냥이 20:05부터, 팀 데스매치가 20:50~21:30에 진행됩니다.")
        if week[now.tm_wday] == '토':
            await message.channel.send("토요일에는 2인 이그드라실이 10:00~24:00에, 주말 길드 파티가 20:00~20:20에, 전장이 12:50~14:30과 21:20~23:00에 진행됩니다. 또, 아직 1인 이그드라실을 한번도 안 했다면 2회 완료하기 위해서라면 반드시 1인 이그드라실을 해야하는 날입니다.")
        if week[now.tm_wday] == '일':
            await message.channel.send("일요일에는 2인 이그드라실이 10:00~24:00에, 무도회가 20:00~20:30에, 길드 사냥이 20:30부터, 전장이 12:50~14:30과 21:20~23:00에 진행됩니다. 또, 1인 이그드라실과 무한의 탑이 초기화되는 마지막 날입니다.")
        return
    if message.content.startswith('엔젤링?') or message.content.startswith('ㅇㅈㄹ?'):
        global later013
        current1 = datetime.datetime.now()
        try:
            left = int((later013 - current1).seconds)
        except(NameError):
            await message.channel.send("아직 엔젤링 젠 시간이 등록되지 않았습니다. 확인 후 등록해주시기 바랍니다.")
            return
        if left>7200:
            left = 86400 - left
            leftmin = left // 60
            leftsec = left - leftmin * 60
            await message.channel.send("아직 엔젤링 젠 시간이 등록되지 않았습니다. 확인 후 등록해주시기 바랍니다. 등록된 마지막 젠으로부터 "+ str(leftmin) + "분 "+str(leftsec)+"초 지났습니다.")
            return
        leftmin = left // 60
        leftsec = left - leftmin * 60
        await message.channel.send("엔젤링 젠까지 " + str(leftmin) + "분 "+str(leftsec)+"초 남았습니다.")
        return

    if message.content.startswith('황도?') or message.content.startswith('ㅎㄷ?'):
        global later023
        current1 = datetime.datetime.now()
        try:
            left = int((later023 - current1).seconds)
        except(NameError):
            await message.channel.send("아직 황금 도둑벌레 젠 시간이 등록되지 않았습니다. 확인 후 등록해주시기 바랍니다.")
            return
        if left>7200:
            left = 86400 - left
            leftmin = left // 60
            leftsec = left - leftmin * 60
            await message.channel.send("아직 황금 도둑벌레 젠 시간이 등록되지 않았습니다. 확인 후 등록해주시기 바랍니다. 등록된 마지막 젠으로부터 "+ str(leftmin) + "분 "+str(leftsec)+"초 지났습니다.")
            return
        leftmin = left // 60
        leftsec = left - leftmin * 60
        await message.channel.send("황금 도둑벌레 젠까지 " + str(leftmin) + "분 "+str(leftsec)+"초 남았습니다.")
        return
    if message.content.startswith('데빌링?') or message.content.startswith('ㄷㅂㄹ?'):
        global later033
        current1 = datetime.datetime.now()
        try:
            left = int((later033 - current1).seconds)
        except(NameError):
            await message.channel.send("아직 데빌링 젠 시간이 등록되지 않았습니다. 확인 후 등록해주시기 바랍니다.")
            return
        if left>7200:
            left = 86400 - left
            leftmin = left // 60
            leftsec = left - leftmin * 60
            await message.channel.send("아직 데빌링 젠 시간이 등록되지 않았습니다. 확인 후 등록해주시기 바랍니다. 등록된 마지막 젠으로부터 "+ str(leftmin) + "분 "+str(leftsec)+"초 지났습니다.")
            return
        leftmin = left // 60
        leftsec = left - leftmin * 60
        await message.channel.send("데빌링 젠까지 " + str(leftmin) + "분 "+str(leftsec)+"초 남았습니다.")
        return
    if message.content.startswith('오히?') or message.content.startswith('ㅇㅎ?'):
        global later043
        current1 = datetime.datetime.now()
        try:
            left = int((later043 - current1).seconds)
        except(NameError):
            await message.channel.send("아직 오크 히어로 젠 시간이 등록되지 않았습니다. 확인 후 등록해주시기 바랍니다.")
            return
        if left>7200:
            left = 86400 - left
            leftmin = left // 60
            leftsec = left - leftmin * 60
            await message.channel.send("아직 오크 히어로 젠 시간이 등록되지 않았습니다. 확인 후 등록해주시기 바랍니다. 등록된 마지막 젠으로부터 "+ str(leftmin) + "분 "+str(leftsec)+"초 지났습니다.")
            return
        leftmin = left // 60
        leftsec = left - leftmin * 60
        await message.channel.send("오크 히어로 젠까지 " + str(leftmin) + "분 "+str(leftsec)+"초 남았습니다.")
        return
    if message.content.startswith('마야?') or message.content.startswith('ㅁㅇ?'):
        global later053
        current1 = datetime.datetime.now()
        try:
            left = int((later053 - current1).seconds)
        except(NameError):
            await message.channel.send("아직 마야 젠 시간이 등록되지 않았습니다. 확인 후 등록해주시기 바랍니다.")
            return
        if left>7200:
            left = 86400 - left
            leftmin = left // 60
            leftsec = left - leftmin * 60
            await message.channel.send("아직 마야 젠 시간이 등록되지 않았습니다. 확인 후 등록해주시기 바랍니다. 등록된 마지막 젠으로부터 "+ str(leftmin) + "분 "+str(leftsec)+"초 지났습니다.")
            return
        leftmin = left // 60
        leftsec = left - leftmin * 60
        await message.channel.send("마야 젠까지 " + str(leftmin) + "분 "+str(leftsec)+"초 남았습니다.")
        return
    if message.content.startswith('오로?') or message.content.startswith('ㅇㄹ?'):
        global later063
        current1 = datetime.datetime.now()
        try:
            left = int((later063 - current1).seconds)
        except(NameError):
            await message.channel.send("아직 오크 로드 젠 시간이 등록되지 않았습니다. 확인 후 등록해주시기 바랍니다.")
            return
        if left>7200:
            left = 86400 - left
            leftmin = left // 60
            leftsec = left - leftmin * 60
            await message.channel.send("아직 오크 로드 젠 시간이 등록되지 않았습니다. 확인 후 등록해주시기 바랍니다. 등록된 마지막 젠으로부터 "+ str(leftmin) + "분 "+str(leftsec)+"초 지났습니다.")
            return
        leftmin = left // 60
        leftsec = left - leftmin * 60
        await message.channel.send("오크 로드 젠까지 " + str(leftmin) + "분 "+str(leftsec)+"초 남았습니다.")
        return
    if message.content.startswith('고리?') or message.content.startswith('ㄱㄹ?'):
        global later073
        current1 = datetime.datetime.now()
        try:
            left = int((later073 - current1).seconds)
        except(NameError):
            await message.channel.send("아직 오크 로드 젠 시간이 등록되지 않았습니다. 확인 후 등록해주시기 바랍니다.")
            return
        if left>7200:
            left = 86400 - left
            leftmin = left // 60
            leftsec = left - leftmin * 60
            await message.channel.send("아직 오크 로드 젠 시간이 등록되지 않았습니다. 확인 후 등록해주시기 바랍니다. 등록된 마지막 젠으로부터 "+ str(leftmin) + "분 "+str(leftsec)+"초 지났습니다.")
            return
        leftmin = left // 60
        leftsec = left - leftmin * 60
        await message.channel.send("오크 로드 젠까지 " + str(leftmin) + "분 "+str(leftsec)+"초 남았습니다.")
        return        
    if message.content.startswith('드레?'):
        global later083
        current1 = datetime.datetime.now()
        try:
            left = int((later083 - current1).seconds)
        except(NameError):
            await message.channel.send("아직 드레이크 젠 시간이 등록되지 않았습니다. 확인 후 등록해주시기 바랍니다.")
            return
        if left>7200:
            left = 86400 - left
            leftmin = left // 60
            leftsec = left - leftmin * 60
            await message.channel.send("아직 드레이크 젠 시간이 등록되지 않았습니다. 확인 후 등록해주시기 바랍니다. 등록된 마지막 젠으로부터 "+ str(leftmin) + "분 "+str(leftsec)+"초 지났습니다.")
            return
        leftmin = left // 60
        leftsec = left - leftmin * 60
        await message.channel.send("드레이크 젠까지 " + str(leftmin) + "분 "+str(leftsec)+"초 남았습니다.")
        return  
    if message.content.startswith('에드가?') or message.content.startswith('ㅇㄷ?'):
        global later093
        current1 = datetime.datetime.now()
        try:
            left = int((later093 - current1).seconds)
        except(NameError):
            await message.channel.send("아직 에드가 젠 시간이 등록되지 않았습니다. 확인 후 등록해주시기 바랍니다.")
            return
        if left>7200:
            left = 86400 - left
            leftmin = left // 60
            leftsec = left - leftmin * 60
            await message.channel.send("아직 에드가 젠 시간이 등록되지 않았습니다. 확인 후 등록해주시기 바랍니다. 등록된 마지막 젠으로부터 "+ str(leftmin) + "분 "+str(leftsec)+"초 지났습니다.")
            return
        leftmin = left // 60
        leftsec = left - leftmin * 60
        await message.channel.send("에드가 젠까지 " + str(leftmin) + "분 "+str(leftsec)+"초 남았습니다.")
        return  
    if message.content.startswith('미스?') or message.content.startswith('ㅁㅅ?'):
        global later103
        current1 = datetime.datetime.now()
        try:
            left = int((later103 - current1).seconds)
        except(NameError):
            await message.channel.send("아직 미스트레스 젠 시간이 등록되지 않았습니다. 확인 후 등록해주시기 바랍니다.")
            return
        if left>7200:
            left = 86400 - left
            leftmin = left // 60
            leftsec = left - leftmin * 60
            await message.channel.send("아직 미스트레스 젠 시간이 등록되지 않았습니다. 확인 후 등록해주시기 바랍니다. 등록된 마지막 젠으로부터 "+ str(leftmin) + "분 "+str(leftsec)+"초 지났습니다.")
            return
        leftmin = left // 60
        leftsec = left - leftmin * 60
        await message.channel.send("미스트레스 젠까지 " + str(leftmin) + "분 "+str(leftsec)+"초 남았습니다.")
        return  
    if message.content.startswith('오시?') or message.content.startswith('ㅇㅅ?'):   
        global later113
        current1 = datetime.datetime.now()
        try:
            left = int((later113 - current1).seconds)
        except(NameError):
            await message.channel.send("아직 오시리스 젠 시간이 등록되지 않았습니다. 확인 후 등록해주시기 바랍니다.")
            return
        if left>7200:
            left = 86400 - left
            leftmin = left // 60
            leftsec = left - leftmin * 60
            await message.channel.send("아직 오시리스 젠 시간이 등록되지 않았습니다. 확인 후 등록해주시기 바랍니다. 등록된 마지막 젠으로부터 "+ str(leftmin) + "분 "+str(leftsec)+"초 지났습니다.")
            return
        leftmin = left // 60
        leftsec = left - leftmin * 60
        await message.channel.send("오시리스 젠까지 " + str(leftmin) + "분 "+str(leftsec)+"초 남았습니다.")
        return  
    if message.content.startswith('프리?') or message.content.startswith('ㅍㄹㅇㄴ?') or message.content.startswith('ㅇㄴ'): 
        global later123
        current1 = datetime.datetime.now()
        try:
            left = int((later123 - current1).seconds)
        except(NameError):
            await message.channel.send("아직 프리오니 젠 시간이 등록되지 않았습니다. 확인 후 등록해주시기 바랍니다.")
            return
        if left>7200:
            left = 86400 - left
            leftmin = left // 60
            leftsec = left - leftmin * 60
            await message.channel.send("아직 프리오니 젠 시간이 등록되지 않았습니다. 확인 후 등록해주시기 바랍니다. 등록된 마지막 젠으로부터 "+ str(leftmin) + "분 "+str(leftsec)+"초 지났습니다.")
            return
        leftmin = left // 60
        leftsec = left - leftmin * 60
        await message.channel.send("프리오니 젠까지 " + str(leftmin) + "분 "+str(leftsec)+"초 남았습니다.")
        return  
    if message.content.startswith('월야화?') or message.content.startswith('ㅇㅇㅎ?'):
        global later133
        current1 = datetime.datetime.now()
        try:
            left = int((later133 - current1).seconds)
        except(NameError):
            await message.channel.send("아직 월야화 젠 시간이 등록되지 않았습니다. 확인 후 등록해주시기 바랍니다.")
            return
        if left>7200:
            left = 86400 - left
            leftmin = left // 60
            leftsec = left - leftmin * 60
            await message.channel.send("아직 월야화 젠 시간이 등록되지 않았습니다. 확인 후 등록해주시기 바랍니다. 등록된 마지막 젠으로부터 "+ str(leftmin) + "분 "+str(leftsec)+"초 지났습니다.")
            return
        leftmin = left // 60
        leftsec = left - leftmin * 60
        await message.channel.send("월야화 젠까지 " + str(leftmin) + "분 "+str(leftsec)+"초 남았습니다.")
        return  
    if message.content.startswith('드라?') or message.content.startswith('ㄷㄹ?'):
        global later143
        current1 = datetime.datetime.now()
        try:
            left = int((later143 - current1).seconds)
        except(NameError):
            await message.channel.send("아직 드라큐라 젠 시간이 등록되지 않았습니다. 확인 후 등록해주시기 바랍니다.")
            return
        if left>7200:
            left = 86400 - left
            leftmin = left // 60
            leftsec = left - leftmin * 60
            await message.channel.send("아직 드라큐라 젠 시간이 등록되지 않았습니다. 확인 후 등록해주시기 바랍니다. 등록된 마지막 젠으로부터 "+ str(leftmin) + "분 "+str(leftsec)+"초 지났습니다.")
            return
        leftmin = left // 60
        leftsec = left - leftmin * 60
        await message.channel.send("드라큐라 젠까지 " + str(leftmin) + "분 "+str(leftsec)+"초 남았습니다.")
        return  
    if message.content.startswith('도플?') or message.content.startswith('ㄷㅍ?'):
        global later153
        current1 = datetime.datetime.now()
        try:
            left = int((later153 - current1).seconds)
        except(NameError):
            await message.channel.send("아직 도플갱어 젠 시간이 등록되지 않았습니다. 확인 후 등록해주시기 바랍니다.")
            return
        if left>7200:
            left = 86400 - left
            leftmin = left // 60
            leftsec = left - leftmin * 60
            await message.channel.send("아직 도플갱어 젠 시간이 등록되지 않았습니다. 확인 후 등록해주시기 바랍니다. 등록된 마지막 젠으로부터 "+ str(leftmin) + "분 "+str(leftsec)+"초 지났습니다.")
            return
        leftmin = left // 60
        leftsec = left - leftmin * 60
        await message.channel.send("도플갱어 젠까지 " + str(leftmin) + "분 "+str(leftsec)+"초 남았습니다.")
        return  
    if message.content.startswith('파라오?') or message.content.startswith('ㅍㄹㅇ?'):
        global later163
        current1 = datetime.datetime.now()
        try:
            left = int((later163 - current1).seconds)
        except(NameError):
            await message.channel.send("아직 파라오 젠 시간이 등록되지 않았습니다. 확인 후 등록해주시기 바랍니다.")
            return
        if left>7200:
            left = 86400 - left
            leftmin = left // 60
            leftsec = left - leftmin * 60
            await message.channel.send("아직 파라오 젠 시간이 등록되지 않았습니다. 확인 후 등록해주시기 바랍니다. 등록된 마지막 젠으로부터 "+ str(leftmin) + "분 "+str(leftsec)+"초 지났습니다.")
            return
        leftmin = left // 60
        leftsec = left - leftmin * 60
        await message.channel.send("파라오 젠까지 " + str(leftmin) + "분 "+str(leftsec)+"초 남았습니다.")
        return  
    if message.content.startswith('바포?') or message.content.startswith('ㅂㅍ?'):
        global later173
        current1 = datetime.datetime.now()
        try:
            left = int((later173 - current1).seconds)
        except(NameError):
            await message.channel.send("아직 바포메트 젠 시간이 등록되지 않았습니다. 확인 후 등록해주시기 바랍니다.")
            return
        if left>7200:
            left = 86400 - left
            leftmin = left // 60
            leftsec = left - leftmin * 60
            await message.channel.send("아직 바포메트 젠 시간이 등록되지 않았습니다. 확인 후 등록해주시기 바랍니다. 등록된 마지막 젠으로부터 "+ str(leftmin) + "분 "+str(leftsec)+"초 지났습니다.")
            return
        leftmin = left // 60
        leftsec = left - leftmin * 60
        await message.channel.send("바포메트 젠까지 " + str(leftmin) + "분 "+str(leftsec)+"초 남았습니다.")
        return  


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
            try:
                await member.add_roles(role)
                await message.channel.send(str(member)+"님에게 "+str(role)+" 역할을 부여했습니다.")
            except(AttributeError):
                await message.channel.send("존재하지 않는 역할입니다. 맞는 직업 또는 보스 명칭인지 확인해주세요. ")
        
            

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
        later011 = current1 + datetime.timedelta(seconds=min*60+sec-900)
        later012 = current1 + datetime.timedelta(seconds=min*60+sec-300)
        later013 = current1 + datetime.timedelta(seconds=min*60+sec)

        #print(tima11)
        #print(tima12)
        #print(tima13)
        on01 = 1
        await message.channel.send("엔젤링 젠 시간을 "+str(min)+"분 "+str(sec)+"초로 받았습니다. 15분과 5분 전, 리젠 시에 알려드겠습니다.")
        while on01 == 1:
            await asyncio.sleep(0.1) 
            current1 =  datetime.datetime.now()
            #print(current1)
            if current1 > later011 and tima11==1:
                commander = discord.utils.get(message.guild.roles, name="엔젤링")
                await message.channel.send("{} 젠까지 15분 남았습니다.".format(commander.mention))
                tima11=0
            if current1 > later012 and tima12==1:
                commander = discord.utils.get(message.guild.roles, name="엔젤링")
                await message.channel.send("{} 젠까지 5분 남았습니다.".format(commander.mention))
                tima12=0
            if current1 > later013 and tima13==1:
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
        later021 = current1 + datetime.timedelta(seconds=min*60+sec-900)
        later022 = current1 + datetime.timedelta(seconds=min*60+sec-300)
        later023 = current1 + datetime.timedelta(seconds=min*60+sec)

        #print(tima11)
        #print(tima12)
        #print(tima13)
        on02 = 1
        await message.channel.send("황금 도둑벌레 젠 시간을 "+str(min)+"분 "+str(sec)+"초로 받았습니다. 15분과 5분 전, 리젠 시에 알려드겠습니다.")
        while on02 == 1:
            await asyncio.sleep(0.1) 
            current1 =  datetime.datetime.now()
            #print(current1)
            if current1 > later021 and tima11==1:
                commander = discord.utils.get(message.guild.roles, name="황금 도둑벌레")
                await message.channel.send("{} 젠까지 15분 남았습니다.".format(commander.mention))
                tima11=0
            if current1 > later022 and tima12==1:
                commander = discord.utils.get(message.guild.roles, name="황금 도둑벌레")
                await message.channel.send("{} 젠까지 5분 남았습니다.".format(commander.mention))
                tima12=0
            if current1 > later023 and tima13==1:
                commander = discord.utils.get(message.guild.roles, name="황금 도둑벌레")
                await message.channel.send("{}가 지하수로 2층에 나타났습니다.".format(commander.mention))
                tima13=0
                break        
    if message.content.startswith('데빌링') or message.content.startswith('ㄷㅂㄹ'):
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
        later031 = current1 + datetime.timedelta(seconds=min*60+sec-900)
        later032 = current1 + datetime.timedelta(seconds=min*60+sec-300)
        later033 = current1 + datetime.timedelta(seconds=min*60+sec)

        #print(tima11)
        #print(tima12)
        #print(tima13)
        on03 = 1
        await message.channel.send("데빌링 젠 시간을 "+str(min)+"분 "+str(sec)+"초로 받았습니다. 15분과 5분 전, 리젠 시에 알려드겠습니다.")
        while on03 == 1:
            await asyncio.sleep(0.1) 
            current1 =  datetime.datetime.now()
            #print(current1)
            if current1 > later031 and tima11==1:
                commander = discord.utils.get(message.guild.roles, name="데빌링")
                await message.channel.send("{} 젠까지 15분 남았습니다.".format(commander.mention))
                tima11=0
            if current1 > later032 and tima12==1:
                commander = discord.utils.get(message.guild.roles, name="데빌링")
                await message.channel.send("{} 젠까지 5분 남았습니다.".format(commander.mention))
                tima12=0
            if current1 > later033 and tima13==1:
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
        later041 = current1 + datetime.timedelta(seconds=min*60+sec-900)
        later042 = current1 + datetime.timedelta(seconds=min*60+sec-300)
        later043 = current1 + datetime.timedelta(seconds=min*60+sec)

        #print(tima11)
        #print(tima12)
        #print(tima13)
        on04 = 1
        await message.channel.send("오크 히어로 젠 시간을 "+str(min)+"분 "+str(sec)+"초로 받았습니다. 15분과 5분 전, 리젠 시에 알려드겠습니다.")
        while on04 == 1:
            await asyncio.sleep(0.1) 
            current1 =  datetime.datetime.now()
            #print(current1)
            if current1 > later041 and tima11==1:
                commander = discord.utils.get(message.guild.roles, name="오크 히어로")
                await message.channel.send("{} 젠까지 15분 남았습니다.".format(commander.mention))
                tima11=0
            if current1 > later042 and tima12==1:
                commander = discord.utils.get(message.guild.roles, name="오크 히어로")
                await message.channel.send("{} 젠까지 5분 남았습니다.".format(commander.mention))
                tima12=0
            if current1 > later043 and tima13==1:
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
        later051 = current1 + datetime.timedelta(seconds=min*60+sec-900)
        later052 = current1 + datetime.timedelta(seconds=min*60+sec-300)
        later053 = current1 + datetime.timedelta(seconds=min*60+sec)

        #print(tima11)
        #print(tima12)
        #print(tima13)
        on05 = 1
        await message.channel.send("마야 젠 시간을 "+str(min)+"분 "+str(sec)+"초로 받았습니다. 15분과 5분 전, 리젠 시에 알려드겠습니다.")
        commander = discord.utils.get(message.guild.roles, name="마야")
        while on05 == 1:
            await asyncio.sleep(0.1) 
            current1 =  datetime.datetime.now()
            #print(current1)
            if current1 > later051 and tima11==1:
                await message.channel.send("{} 젠까지 15분 남았습니다.".format(commander.mention))
                tima11=0
            if current1 > later052 and tima12==1:
                await message.channel.send("{} 젠까지 5분 남았습니다.".format(commander.mention))
                tima12=0
            if current1 > later053 and tima13==1:
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
        later061 = current1 + datetime.timedelta(seconds=min*60+sec-900)
        later062 = current1 + datetime.timedelta(seconds=min*60+sec-300)
        later063 = current1 + datetime.timedelta(seconds=min*60+sec)

        #print(tima11)
        #print(tima12)
        #print(tima13)
        on06 = 1
        await message.channel.send("오크 로드 젠 시간을 "+str(min)+"분 "+str(sec)+"초로 받았습니다. 15분과 5분 전, 리젠 시에 알려드겠습니다.")
        commander = discord.utils.get(message.guild.roles, name="오크 로드")
        while on06 == 1:
            await asyncio.sleep(0.1) 
            current1 =  datetime.datetime.now()
            #print(current1)
            if current1 > later061 and tima11==1:
                await message.channel.send("{} 젠까지 15분 남았습니다.".format(commander.mention))
                tima11=0
            if current1 > later062 and tima12==1:
                await message.channel.send("{} 젠까지 5분 남았습니다.".format(commander.mention))
                tima12=0
            if current1 > later063 and tima13==1:
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
        later071 = current1 + datetime.timedelta(seconds=min*60+sec-900)
        later072 = current1 + datetime.timedelta(seconds=min*60+sec-300)
        later073 = current1 + datetime.timedelta(seconds=min*60+sec)

        #print(tima11)
        #print(tima12)
        #print(tima13)
        on07 = 1
        await message.channel.send("고블린 리더 젠 시간을 "+str(min)+"분 "+str(sec)+"초로 받았습니다. 15분과 5분 전, 리젠 시에 알려드겠습니다.")
        commander = discord.utils.get(message.guild.roles, name="고블린 리더")
        while on07 == 1:
            await asyncio.sleep(0.1) 
            current1 =  datetime.datetime.now()
            #print(current1)
            if current1 > later071 and tima11==1:
                await message.channel.send("{} 젠까지 15분 남았습니다.".format(commander.mention))
                tima11=0
            if current1 > later072 and tima12==1:
                await message.channel.send("{} 젠까지 5분 남았습니다.".format(commander.mention))
                tima12=0
            if current1 > later073 and tima13==1:
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
        later081 = current1 + datetime.timedelta(seconds=min*60+sec-900)
        later082 = current1 + datetime.timedelta(seconds=min*60+sec-300)
        later083 = current1 + datetime.timedelta(seconds=min*60+sec)

        #print(tima11)
        #print(tima12)
        #print(tima13)
        on08 = 1
        await message.channel.send("드레이크 젠 시간을 "+str(min)+"분 "+str(sec)+"초로 받았습니다. 15분과 5분 전, 리젠 시에 알려드겠습니다.")
        commander = discord.utils.get(message.guild.roles, name="드레이크")
        while on08 == 1:
            await asyncio.sleep(0.1) 
            current1 =  datetime.datetime.now()
            #print(current1)
            if current1 > later081 and tima11==1:
                await message.channel.send("{} 젠까지 15분 남았습니다.".format(commander.mention))
                tima11=0
            if current1 > later082 and tima12==1:
                await message.channel.send("{} 젠까지 5분 남았습니다.".format(commander.mention))
                tima12=0
            if current1 > later083 and tima13==1:
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
        later091 = current1 + datetime.timedelta(seconds=min*60+sec-900)
        later092 = current1 + datetime.timedelta(seconds=min*60+sec-300)
        later093 = current1 + datetime.timedelta(seconds=min*60+sec)

        #print(tima11)
        #print(tima12)
        #print(tima13)
        on09 = 1
        await message.channel.send("에드가 젠 시간을 "+str(min)+"분 "+str(sec)+"초로 받았습니다. 15분과 5분 전, 리젠 시에 알려드겠습니다.")
        commander = discord.utils.get(message.guild.roles, name="에드가")
        while on09 == 1:
            await asyncio.sleep(0.1) 
            current1 =  datetime.datetime.now()
            #print(current1)
            if current1 > later091 and tima11==1:
                await message.channel.send("{} 젠까지 15분 남았습니다.".format(commander.mention))
                tima11=0
            if current1 > later092 and tima12==1:
                await message.channel.send("{} 젠까지 5분 남았습니다.".format(commander.mention))
                tima12=0
            if current1 > later093 and tima13==1:
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
        later101 = current1 + datetime.timedelta(seconds=min*60+sec-900)
        later102 = current1 + datetime.timedelta(seconds=min*60+sec-300)
        later103 = current1 + datetime.timedelta(seconds=min*60+sec)

        #print(tima11)
        #print(tima12)
        #print(tima13)
        on10 = 1
        await message.channel.send("미스트레스 젠 시간을 "+str(min)+"분 "+str(sec)+"초로 받았습니다. 15분과 5분 전, 리젠 시에 알려드겠습니다.")
        commander = discord.utils.get(message.guild.roles, name="미스트레스")
        while on10 == 1:
            await asyncio.sleep(0.1) 
            current1 =  datetime.datetime.now()
            #print(current1)
            if current1 > later101 and tima11==1:
                await message.channel.send("{} 젠까지 15분 남았습니다.".format(commander.mention))
                tima11=0
            if current1 > later102 and tima12==1:
                await message.channel.send("{} 젠까지 5분 남았습니다.".format(commander.mention))
                tima12=0
            if current1 > later103 and tima13==1:
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
        later111 = current1 + datetime.timedelta(seconds=min*60+sec-900)
        later112 = current1 + datetime.timedelta(seconds=min*60+sec-300)
        later113 = current1 + datetime.timedelta(seconds=min*60+sec)

        #print(tima11)
        #print(tima12)
        #print(tima13)
        on11 = 1
        await message.channel.send("오시리스 젠 시간을 "+str(min)+"분 "+str(sec)+"초로 받았습니다. 15분과 5분 전, 리젠 시에 알려드겠습니다.")
        commander = discord.utils.get(message.guild.roles, name="오시리스")
        while on11 == 1:
            await asyncio.sleep(0.1) 
            current1 =  datetime.datetime.now()
            #print(current1)
            if current1 > later111 and tima11==1:
                await message.channel.send("{} 젠까지 15분 남았습니다.".format(commander.mention))
                tima11=0
            if current1 > later112 and tima12==1:
                await message.channel.send("{} 젠까지 5분 남았습니다.".format(commander.mention))
                tima12=0
            if current1 > later113 and tima13==1:
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
        later121 = current1 + datetime.timedelta(seconds=min*60+sec-900)
        later122 = current1 + datetime.timedelta(seconds=min*60+sec-300)
        later123 = current1 + datetime.timedelta(seconds=min*60+sec)

        #print(tima11)
        #print(tima12)
        #print(tima13)
        on12 = 1
        await message.channel.send("프리오니 젠 시간을 "+str(min)+"분 "+str(sec)+"초로 받았습니다. 15분과 5분 전, 리젠 시에 알려드겠습니다.")
        commander = discord.utils.get(message.guild.roles, name="프리오니")
        while on12 == 1:
            await asyncio.sleep(0.1) 
            current1 =  datetime.datetime.now()
            #print(current1)
            if current1 > later121 and tima11==1:
                await message.channel.send("{} 젠까지 15분 남았습니다.".format(commander.mention))
                tima11=0
            if current1 > later122 and tima12==1:
                await message.channel.send("{} 젠까지 5분 남았습니다.".format(commander.mention))
                tima12=0
            if current1 > later123 and tima13==1:
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
        later131 = current1 + datetime.timedelta(seconds=min*60+sec-900)
        later132 = current1 + datetime.timedelta(seconds=min*60+sec-300)
        later133 = current1 + datetime.timedelta(seconds=min*60+sec)

        #print(tima11)
        #print(tima12)
        #print(tima13)
        on13 = 1
        await message.channel.send("월야화 젠 시간을 "+str(min)+"분 "+str(sec)+"초로 받았습니다. 15분과 5분 전, 리젠 시에 알려드겠습니다.")
        commander = discord.utils.get(message.guild.roles, name="월야화")
        while on13 == 1:
            await asyncio.sleep(0.1) 
            current1 =  datetime.datetime.now()
            #print(current1)
            if current1 > later131 and tima11==1:
                await message.channel.send("{} 젠까지 15분 남았습니다.".format(commander.mention))
                tima11=0
            if current1 > later132 and tima12==1:
                await message.channel.send("{} 젠까지 5분 남았습니다.".format(commander.mention))
                tima12=0
            if current1 > later133 and tima13==1:
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
        later141 = current1 + datetime.timedelta(seconds=min*60+sec-900)
        later142 = current1 + datetime.timedelta(seconds=min*60+sec-300)
        later143 = current1 + datetime.timedelta(seconds=min*60+sec)

        #print(tima11)
        #print(tima12)
        #print(tima13)
        on14 = 1
        await message.channel.send("드라큐라 젠 시간을 "+str(min)+"분 "+str(sec)+"초로 받았습니다. 15분과 5분 전, 리젠 시에 알려드겠습니다.")
        while on14 == 1:
            await asyncio.sleep(0.1) 
            current1 =  datetime.datetime.now()
            #print(current1)
            if current1 > later141 and tima11==1:
                commander = discord.utils.get(message.guild.roles, name="드라큐라")
                await message.channel.send("{} 젠까지 15분 남았습니다.".format(commander.mention))
                tima11=0
            if current1 > later142 and tima12==1:
                commander = discord.utils.get(message.guild.roles, name="드라큐라")
                await message.channel.send("{} 젠까지 5분 남았습니다.".format(commander.mention))
                tima12=0
            if current1 > later143 and tima13==1:
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
        later151 = current1 + datetime.timedelta(seconds=min*60+sec-900)
        later152 = current1 + datetime.timedelta(seconds=min*60+sec-300)
        later153 = current1 + datetime.timedelta(seconds=min*60+sec)

        #print(tima11)
        #print(tima12)
        #print(tima13)
        on15 = 1
        await message.channel.send("도플갱어 젠 시간을 "+str(min)+"분 "+str(sec)+"초로 받았습니다. 15분과 5분 전, 리젠 시에 알려드겠습니다.")
        commander = discord.utils.get(message.guild.roles, name="도플갱어")
        while on15 == 1:
            await asyncio.sleep(0.1) 
            current1 =  datetime.datetime.now()
            #print(current1)
            if current1 > later151 and tima11==1:
                await message.channel.send("{} 젠까지 15분 남았습니다.".format(commander.mention))
                tima11=0
            if current1 > later152 and tima12==1:
                await message.channel.send("{} 젠까지 5분 남았습니다.".format(commander.mention))
                tima12=0
            if current1 > later153 and tima13==1:
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
        later161 = current1 + datetime.timedelta(seconds=min*60+sec-900)
        later162 = current1 + datetime.timedelta(seconds=min*60+sec-300)
        later163 = current1 + datetime.timedelta(seconds=min*60+sec)

        #print(tima11)
        #print(tima12)
        #print(tima13)
        on16 = 1
        await message.channel.send("파라오 젠 시간을 "+str(min)+"분 "+str(sec)+"초로 받았습니다. 15분과 5분 전, 리젠 시에 알려드겠습니다.")
        commander = discord.utils.get(message.guild.roles, name="파라오")
        while on16 == 1:
            await asyncio.sleep(0.1) 
            current1 =  datetime.datetime.now()
            #print(current1)
            if current1 > later161 and tima11==1:
                await message.channel.send("{} 젠까지 15분 남았습니다.".format(commander.mention))
                tima11=0
            if current1 > later162 and tima12==1:
                await message.channel.send("{} 젠까지 5분 남았습니다.".format(commander.mention))
                tima12=0
            if current1 > later163 and tima13==1:
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
        later171 = current1 + datetime.timedelta(seconds=min*60+sec-898)
        later172 = current1 + datetime.timedelta(seconds=min*60+sec-298)
        later173 = current1 + datetime.timedelta(seconds=min*60+sec-2)

        #print(tima11)
        #print(tima12)
        #print(tima13)
        on17 = 1
        commander = discord.utils.get(message.guild.roles, name="바포메트")
        await message.channel.send("바포메트 젠 시간을 "+str(min)+"분 "+str(sec)+"초로 받았습니다. 15분과 5분 전, 출몰 시에 알림을 보내드립니다.")
        while on17 == 1:
            await asyncio.sleep(0.1) 
            current1 =  datetime.datetime.now()
            #print(current1)
            if current1 > later171 and tima11==1:
                await message.channel.send("{} 젠까지 15분 남았습니다.".format(commander.mention))
                tima11=0
            if current1 > later172 and tima12==1:
                await message.channel.send("{} 젠까지 5분 남았습니다.".format(commander.mention))
                tima12=0
            if current1 > later173 and tima13==1:
                await message.channel.send("{}가 미궁 숲 1층에 나타났습니다.".format(commander.mention))
                tima13=0
                break
           
                
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)

