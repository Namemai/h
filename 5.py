'''
Fixed And Builded 2019 By Uwewww
อัพเดทล่าสุด ©2020 By mai™
'''
from sentinel import *
from thrift import transport, protocol, server
from sentinel.thrift.Thrift import *
from sentinel.thrift.TMultiplexedProcessor import *
from sentinel.thrift.TSerialization import *
from sentinel.thrift.TRecursive import *
from sentinel.thrift.protocol import TCompactProtocol
from sentinel.thrift.transport import THttpClient
from akad.ttypes import *
from time import sleep
from threading import Thread
import pytz, datetime, time, timeit, livejson, asyncio, random, sys, ast, re, os, json, subprocess, threading, string, codecs, requests, ctypes, urllib,traceback,platform
from datetime import timedelta, date
from datetime import datetime
# Sentinel™ Simple Bots
# Free To Use,All Credits Belong To Me,Uwewww
# Found Some Bugs Or Error? Feel Free To Report Bugs :)
# Login Option Below
# Email : LINE("email","Password")
# Auth Token : LINE("authtoken")
# Primary Token : LINE("primary",appName='IOS\t10.1.1\tIOS OS\t1')
programStart = time.time()
cl = LINE("primary",appName='IOS\t10.1.1\tIOS OS\t1')
print('==== UNIT หลัก READY ! ====')
ki = LINE("primary",appName='IOS\t10.1.1\tIOS OS\t1')
print('==== UNIT 1 READY ! ====')
kk = LINE("primary",appName='IOS\t10.1.1\tIOS OS\t1')
print('==== UNIT 2 READY ! ====')
kc = LINE("primary",appName='IOS\t10.1.1\tIOS OS\t1')
print('==== UNIT 3 READY ! ====')
km = LINE("primary",appName='IOS\t10.1.1\tIOS OS\t1')
print('==== UNIT 4 READY ! ====')
k5 = LINE("primary",appName='IOS\t10.1.1\tIOS OS\t1')
print('==== UNIT 5 READY ! ====')

mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = km.getProfile().mid
K5mid = k5.getProfile().mid
KAC = [ki,kk,kc,km,k5]

loop = asyncio.get_event_loop()
status = livejson.File('status.json', True, False, 4)
with open("settings.json","r",encoding="utf-8") as fp:
	settings = json.load(fp)
creator = status["creator"]
owner = status["owner"]
admin = status["admin"]
staff = status["staff"]
mybots = status["mybots"]
Bots = [mid,Amid,Bmid,Cmid,Dmid,K5mid]
Botslist = [cl,ki,kk,kc,km,k5]
resp0 = cl.getProfile().displayName
resp1 = ki.getProfile().displayName
resp2 = kk.getProfile().displayName
resp3 = kc.getProfile().displayName
resp4 = km.getProfile().displayName
resp5 = k5.getProfile().displayName

def backupData():
	try:
		backup = settings
		f = codecs.open('settings.json','w','utf-8')
		json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
		return True
	except:
		pass

def restartProgram():
	print('####==== ระบบเริ่มทำงาน ====####')
	backupData()
	time.sleep(1)
	python = sys.executable
	os.execl(python, python, *sys.argv)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    weeks, days = divmod(days,7)
    months, weeks = divmod(weeks,4)
    text = ""
    if months != 0: text += "%02d Months" % (months)
    if weeks != 0: text += " %02d Weeks" % (weeks)
    if days != 0: text += " %02d Days" % (days)
    if hours !=  0: text +=  " %02d Hours" % (hours)
    if mins != 0: text += " %02d Minutes" % (mins)
    if secs != 0: text += " %02d Seconds" % (secs)
    if text[0] == " ":
        text = text[1:]
    return text

def logError(text):
    cl.log("[ ERROR ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("logError.txt","a") as error:
        error.write("\n[ {} ] {}".format(str(time), text))

def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def kick(grup, target):
    try:
        ki.kickoutFromGroup(grup, [target])
    except:
        try:
            kk.kickoutFromGroup(grup, [target])
        except:
            try:
                kc.kickoutFromGroup(grup, [target])
            except:
                try:
                    km.kickoutFromGroup(grup, [target])
                except:
                    try:
                        k5.kickoutFromGroup(grup, [target])
                    except:
                        pass
