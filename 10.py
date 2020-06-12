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
k6 = LINE("primary",appName='IOS\t10.1.1\tIOS OS\t1')
print('==== UNIT 6 READY ! ====')
k7 = LINE("primary",appName='IOS\t10.1.1\tIOS OS\t1')
print('==== UNIT 7 READY ! ====')
print ('\n\nALL UNIT READY !')

mid = cl.getProfile().mid
K1mid = k1.getProfile().mid
K2mid = k2.getProfile().mid
K3mid = k3.getProfile().mid
K4mid = k4.getProfile().mid
K5mid = k5.getProfile().mid
K6mid = k6.getProfile().mid
K7mid = k7.getProfile().mid
K8mid = k8.getProfile().mid
K9mid = k9.getProfile().mid
K10mid = k10.getProfile().mid
KAC = [k1,k2,k3,k4,k5,k6,k7,k8,k9,k10]

loop = asyncio.get_event_loop()
status = livejson.File('status.json', True, False, 4)
with open("settings.json","r",encoding="utf-8") as fp:
	settings = json.load(fp)
creator = status["creator"]
owner = status["owner"]
admin = status["admin"]
staff = status["staff"]
mybots = status["mybots"]
Bots = [mid,K1mid,K2mid,K3mid,K4mid,K5mid,K6mid,K7mid,K8mid,K9mid,K10mid]
Botslist = [cl,k1,k2,k3,k4,k5,k6,k7,k8,k9,k10]
resp0 = cl.getProfile().displayName
resp1 = k1.getProfile().displayName
resp2 = k2.getProfile().displayName
resp3 = k3.getProfile().displayName
resp4 = k4.getProfile().displayName
resp5 = k5.getProfile().displayName
resp6 = k6.getProfile().displayName
resp7 = k7.getProfile().displayName
resp8 = k8.getProfile().displayName
resp9 = k9.getProfile().displayName
resp10 = k10.getProfile().displayName

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
        k1.kickoutFromGroup(grup, [target])
    except:
        try:
            k2.kickoutFromGroup(grup, [target])
        except:
            try:
                k3.kickoutFromGroup(grup, [target])
            except:
                try:
                    k4.kickoutFromGroup(grup, [target])
                except:
                    try:
                        k5.kickoutFromGroup(grup, [target])
                    except:
                        try:
                            k6.kickoutFromGroup(grup, [target])
                        except:
                            try:
                                k7.kickoutFromGroup(grup, [target])
                            except:
                                try:
                                    k8.kickoutFromGroup(grup, [target])
                                except:
                                    try:
                                        k9.kickoutFromGroup(grup, [target])
                                    except:
                                        try:
                                            k10.kickoutFromGroup(grup, [target])
                                        except:
                                            pass

def cancel(grup, target):
    try:
        k1.cancelGroupInvitation(grup, [target])
    except:
        try:
            k2.cancelGroupInvitation(grup, [target])
        except:
            try:
                k3.cancelGroupInvitation(grup, [target])
            except:
                try:
                    k4.cancelGroupInvitation(grup, [target])
                except:
                    try:
                        k5.cancelGroupInvitation(grup, [target])
                    except:
                        try:
                            k6.cancelGroupInvitation(grup, [target])
                        except:
                            try:
                                k7.cancelGroupInvitation(grup, [target])
                            except:
                                try:
                                    k8.cancelGroupInvitation(grup, [target])
                                except:
                                    try:
                                        k9.cancelGroupInvitation(grup, [target])
                                    except:
                                        try:
                                            k10.cancelGroupInvitation(grup, [target])
                                        except:
                                            pass

def invite(grup, target):
    try:
        k1.findAndAddContactsByMid(target)
        k1.inviteIntoGroup(grup, [target])
    except:
        try:
            k2.findAndAddContactsByMid(target)
            k2.inviteIntoGroup(grup, [target])
        except:
            try:
                k3.findAndAddContactsByMid(target)
                k3.inviteIntoGroup(grup, [target])
            except:
                try:
                    k4.findAndAddContactsByMid(target)
                    k4.inviteIntoGroup(grup, [target])
                except:
                    try:
                        k5.findAndAddContactsByMid(target)
                        k5.inviteIntoGroup(grup, [target])
                    except:
                        try:
                            k6.findAndAddContactsByMid(target)
                            k6.inviteIntoGroup(grup, [target])
                        except:
                            try:
                                k7.findAndAddContactsByMid(target)
                                k7.inviteIntoGroup(grup, [target])
                            except:
                                try:
                                    k8.findAndAddContactsByMid(target)
                                    k8.inviteIntoGroup(grup, [target])
                                except:
                                    try:
                                        k9.findAndAddContactsByMid(target)
                                        k9.inviteIntoGroup(grup, [target])
                                    except:
                                        try:
                                            k10.findAndAddContactsByMid(target)
                                            k10.inviteIntoGroup(grup, [target])
                                        except:
                                            try:
                                                cl.findAndAddContactsByMid(["u46972f7c43e399c93cf49fad40ae7262"])
                                                cl.kickoutFromGroup(grup, [target])
                                                cl.inviteIntoGroup(grup, ["u46972f7c43e399c93cf49fad40ae7262"])
                                            except:
                                                pass

def backup(grup, target):
    try:
        k1.inviteIntoGroup(grup, [K2mid,K3mid,K4mid,K5mid,K6mid,K7mid,K8mid,K9mid,K10mid,mid])
        if target == K2mid:
            k2.acceptGroupInvitation(grup)
        if target == K3mid:
            k3.acceptGroupInvitation(grup)
        if target == K4mid:
            k4.acceptGroupInvitation(grup)
        if target == K5mid:
            k5.acceptGroupInvitation(grup)
        if target == K6mid:
            k6.acceptGroupInvitation(grup)
        if target == K7mid:
            k7.acceptGroupInvitation(grup)
        if target == K8mid:
            k8.acceptGroupInvitation(grup)
        if target == K9mid:
            k9.acceptGroupInvitation(grup)
        if target == K10mid:
            k10.acceptGroupInvitation(grup)
        if target == mid:
            cl.acceptGroupInvitation(grup)
    except:
        try:
            k2.inviteIntoGroup(grup, [K1mid,K3mid,K4mid,K5mid,K6mid,K7mid,K8mid,K9mid,K10mid,mid])
            if target == K1mid:
                k1.acceptGroupInvitation(grup)
            if target == K3mid:
                k3.acceptGroupInvitation(grup)
            if target == K4mid:
                k4.acceptGroupInvitation(grup)
            if target == K5mid:
                k5.acceptGroupInvitation(grup)
            if target == K6mid:
                k6.acceptGroupInvitation(grup)
            if target == K7mid:
                k7.acceptGroupInvitation(grup)
            if target == K8mid:
                k8.acceptGroupInvitation(grup)
            if target == K9mid:
                k9.acceptGroupInvitation(grup)
            if target == K10mid:
                k10.acceptGroupInvitation(grup)
            if target == mid:
                cl.acceptGroupInvitation(grup)
        except:
            try:
                k3.inviteIntoGroup(grup, [K1mid,K2mid,K4mid,K5mid,K6mid,K7mid,K8mid,K9mid,K10mid,mid])
                if target == K1mid:
                    k1.acceptGroupInvitation(grup)
                if target == K2mid:
                    k2.acceptGroupInvitation(grup)
                if target == K4mid:
                    k4.acceptGroupInvitation(grup)
                if target == K5mid:
                    k5.acceptGroupInvitation(grup)
                if target == K6mid:
                    k6.acceptGroupInvitation(grup)
                if target == K7mid:
                    k7.acceptGroupInvitation(grup)
                if target == K8mid:
                    k8.acceptGroupInvitation(grup)
                if target == K9mid:
                    k9.acceptGroupInvitation(grup)
                if target == K10mid:
                    k10.acceptGroupInvitation(grup)
                if target == mid:
                    cl.acceptGroupInvitation(grup)
            except:
                try:
                    k4.inviteIntoGroup(grup, [K1mid,K2mid,K3mid,K5mid,K6mid,K7mid,K8mid,K9mid,K10mid,mid])
                    if target == K1mid:
                        k1.acceptGroupInvitation(grup)
                    if target == K2mid:
                        k2.acceptGroupInvitation(grup)
                    if target == K3mid:
                        k3.acceptGroupInvitation(grup)
                    if target == K5mid:
                        k5.acceptGroupInvitation(grup)
                    if target == K6mid:
                        k6.acceptGroupInvitation(grup)
                    if target == K7mid:
                        k7.acceptGroupInvitation(grup)
                    if target == K8mid:
                        k8.acceptGroupInvitation(grup)
                    if target == K9mid:
                        k9.acceptGroupInvitation(grup)
                    if target == K10mid:
                        k10.acceptGroupInvitation(grup)
                    if target == mid:
                        cl.acceptGroupInvitation(grup)
                except:
                    try:
                        k5.inviteIntoGroup(grup, [K1mid,K2mid,K3mid,K4mid,K6mid,K7mid,K8mid,K9mid,K10mid,mid])
                        if target == K1mid:
                            k1.acceptGroupInvitation(grup)
                        if target == K2mid:
                            k2.acceptGroupInvitation(grup)
                        if target == K3mid:
                            k3.acceptGroupInvitation(grup)
                        if target == K4mid:
                            k4.acceptGroupInvitation(grup)
                        if target == K6mid:
                            k6.acceptGroupInvitation(grup)
                        if target == K7mid:
                            k7.acceptGroupInvitation(grup)
                        if target == K8mid:
                            k8.acceptGroupInvitation(grup)
                        if target == K9mid:
                            k9.acceptGroupInvitation(grup)
                        if target == K10mid:
                            k10.acceptGroupInvitation(grup)
                        if target == mid:
                            cl.acceptGroupInvitation(grup)
                    except:
                        try:
                            k6.inviteIntoGroup(grup, [K1mid,K2mid,K3mid,K4mid,K5mid,K7mid,K8mid,K9mid,K10mid,mid])
                            if target == K1mid:
                                k1.acceptGroupInvitation(grup)
                            if target == K2mid:
                                k2.acceptGroupInvitation(grup)
                            if target == K3mid:
                                k3.acceptGroupInvitation(grup)
                            if target == K4mid:
                                k4.acceptGroupInvitation(grup)
                            if target == K5mid:
                                k5.acceptGroupInvitation(grup)
                            if target == K7mid:
                                k7.acceptGroupInvitation(grup)
                            if target == K8mid:
                                k8.acceptGroupInvitation(grup)
                            if target == K9mid:
                                k9.acceptGroupInvitation(grup)
                            if target == K10mid:
                                k10.acceptGroupInvitation(grup)
                            if target == mid:
                                cl.acceptGroupInvitation(grup)
                        except:
                            try:
                                k7.inviteIntoGroup(grup, [K1mid,K2mid,K3mid,K4mid,K5mid,K6mid,K8mid,K9mid,K10mid,mid])
                                if target == K1mid:
                                    k1.acceptGroupInvitation(grup)
                                if target == K2mid:
                                    k2.acceptGroupInvitation(grup)
                                if target == K3mid:
                                    k3.acceptGroupInvitation(grup)
                                if target == K4mid:
                                    k4.acceptGroupInvitation(grup)
                                if target == K5mid:
                                    k5.acceptGroupInvitation(grup)
                                if target == K6mid:
                                    k6.acceptGroupInvitation(grup)
                                if target == K8mid:
                                    k8.acceptGroupInvitation(grup)
                                if target == K9mid:
                                    k9.acceptGroupInvitation(grup)
                                if target == K10mid:
                                    k10.acceptGroupInvitation(grup)
                                if target == mid:
                                    cl.acceptGroupInvitation(grup)
                            except:
                                try:
                                    k8.inviteIntoGroup(grup, [K1mid,K2mid,K3mid,K4mid,K5mid,K6mid,K7mid,K9mid,K10mid,mid])
                                    if target == K1mid:
                                        k1.acceptGroupInvitation(grup)
                                    if target == K2mid:
                                        k2.acceptGroupInvitation(grup)
                                    if target == K3mid:
                                        k3.acceptGroupInvitation(grup)
                                    if target == K4mid:
                                        k4.acceptGroupInvitation(grup)
                                    if target == K5mid:
                                        k5.acceptGroupInvitation(grup)
                                    if target == K6mid:
                                        k6.acceptGroupInvitation(grup)
                                    if target == K7mid:
                                        k7.acceptGroupInvitation(grup)
                                    if target == K9mid:
                                        k9.acceptGroupInvitation(grup)
                                    if target == K10mid:
                                        k10.acceptGroupInvitation(grup)
                                    if target == mid:
                                        cl.acceptGroupInvitation(grup)
                                except:
                                    try:
                                        k9.inviteIntoGroup(grup, [K1mid,K2mid,K3mid,K4mid,K5mid,K6mid,K7mid,K8mid,K10mid,mid])
                                        if target == K1mid:
                                            k1.acceptGroupInvitation(grup)
                                        if target == K2mid:
                                            k2.acceptGroupInvitation(grup)
                                        if target == K3mid:
                                            k3.acceptGroupInvitation(grup)
                                        if target == K4mid:
                                            k4.acceptGroupInvitation(grup)
                                        if target == K5mid:
                                            k5.acceptGroupInvitation(grup)
                                        if target == K6mid:
                                            k6.acceptGroupInvitation(grup)
                                        if target == K7mid:
                                            k7.acceptGroupInvitation(grup)
                                        if target == K8mid:
                                            k8.acceptGroupInvitation(grup)
                                        if target == K10mid:
                                            k10.acceptGroupInvitation(grup)

                                        if target == mid:
                                            cl.acceptGroupInvitation(grup)
                                    except:
                                        try:
                                            k10.inviteIntoGroup(grup, [K1mid,K2mid,K3mid,K4mid,K5mid,K6mid,K7mid,K8mid,K9mid,mid])
                                            if target == K1mid:
                                                k1.acceptGroupInvitation(grup)
                                            if target == K2mid:
                                                k2.acceptGroupInvitation(grup)
                                            if target == K3mid:
                                                k3.acceptGroupInvitation(grup)
                                            if target == K4mid:
                                                k4.acceptGroupInvitation(grup)
                                            if target == K5mid:
                                                k5.acceptGroupInvitation(grup)
                                            if target == K6mid:
                                                k6.acceptGroupInvitation(grup)
                                            if target == K7mid:
                                                k7.acceptGroupInvitation(grup)
                                            if target == K8mid:
                                                k8.acceptGroupInvitation(grup)
                                            if target == K9mid:
                                                k9.acceptGroupInvitation(grup)
                                            if target == mid:
                                                cl.acceptGroupInvitation(grup)
                                        except:
                                            pass

def lockqr(grup):
    try:
        G = k1.getGroup(grup)
        G.preventedJoinByTicket = True
        k1.updateGroup(G)
    except:
        try:
            G = k2.getGroup(grup)
            G.preventedJoinByTicket = True
            k2.updateGroup(G)
        except:
            try:
                G = k3.getGroup(grup)
                G.preventedJoinByTicket = True
                k3.updateGroup(G)
            except:
                try:
                    G = k4.getGroup(grup)
                    G.preventedJoinByTicket = True
                    k4.updateGroup(G)
                except:
                    try:
                        G = k5.getGroup(grup)
                        G.preventedJoinByTicket = True
                        k5.updateGroup(G)
                    except:
                        try:
                            G = k6.getGroup(grup)
                            G.preventedJoinByTicket = True
                            k6.updateGroup(G)
                        except:
                            try:
                                G = k7.getGroup(grup)
                                G.preventedJoinByTicket = True
                                k7.updateGroup(G)
                            except:
                                try:
                                    G = k8.getGroup(grup)
                                    G.preventedJoinByTicket = True
                                    k8.updateGroup(G)
                                except:
                                    try:
                                        G = k9.getGroup(grup)
                                        G.preventedJoinByTicket = True
                                        k9.updateGroup(G)
                                    except:
                                        try:
                                            G = k10.getGroup(grup)
                                            G.preventedJoinByTicket = True
                                            k10.updateGroup(G)
                                        except:
                                            pass

def blacklist(target):
	try:
		if target in creator or target in owner or target in admin or target in staff or target in mybots or target in Bots:
			pass
		else:
			status["blacklist"].append(target)
	except:
		pass

def logspeed():
	get_profile_time_start = time.time()
	get_profile = k1.getProfile()
	get_profile_time = time.time() - get_profile_time_start
	get_profile_took = time.time() - get_profile_time_start
	return "「 Bots Speed 」\n • Took : %.3fms\n • Taken: %.5f" % (get_profile_took,get_profile_time)
	get_profile_time_start = time.time()
	get_profile = k2.getProfile()
	get_profile_time = time.time() - get_profile_time_start
	get_profile_took = time.time() - get_profile_time_start
	return "「 Bots Speed 」\n • Took : %.3fms\n • Taken: %.5f" % (get_profile_took,get_profile_time)
	get_profile_time_start = time.time()
	get_profile = k3.getProfile()
	get_profile_time = time.time() - get_profile_time_start
	get_profile_took = time.time() - get_profile_time_start
	return "「 Bots Speed 」\n • Took : %.3fms\n • Taken: %.5f" % (get_profile_took,get_profile_time)
	get_profile_time_start = time.time()
	get_profile = k4.getProfile()
	get_profile_time = time.time() - get_profile_time_start
	get_profile_took = time.time() - get_profile_time_start
	return "「 Bots Speed 」\n • Took : %.3fms\n • Taken: %.5f" % (get_profile_took,get_profile_time)
	get_profile_time_start = time.time()
	get_profile = k5.getProfile()
	get_profile_time = time.time() - get_profile_time_start
	get_profile_took = time.time() - get_profile_time_start
	return "「 Bots Speed 」\n • Took : %.3fms\n • Taken: %.5f" % (get_profile_took,get_profile_time)
	get_profile_time_start = time.time()
	get_profile = k6.getProfile()
	get_profile_time = time.time() - get_profile_time_start
	get_profile_took = time.time() - get_profile_time_start
	return "「 Bots Speed 」\n • Took : %.3fms\n • Taken: %.5f" % (get_profile_took,get_profile_time)
	get_profile_time_start = time.time()
	get_profile = k7.getProfile()
	get_profile_time = time.time() - get_profile_time_start
	get_profile_took = time.time() - get_profile_time_start
	return "「 Bots Speed 」\n • Took : %.3fms\n • Taken: %.5f" % (get_profile_took,get_profile_time)
	get_profile_time_start = time.time()
	get_profile = k8.getProfile()
	get_profile_time = time.time() - get_profile_time_start
	get_profile_took = time.time() - get_profile_time_start
	return "「 Bots Speed 」\n • Took : %.3fms\n • Taken: %.5f" % (get_profile_took,get_profile_time)
	get_profile_time_start = time.time()
	get_profile = k9.getProfile()
	get_profile_time = time.time() - get_profile_time_start
	get_profile_took = time.time() - get_profile_time_start
	return "「 Bots Speed 」\n • Took : %.3fms\n • Taken: %.5f" % (get_profile_took,get_profile_time)
	get_profile_time_start = time.time()
	get_profile = k10.getProfile()
	get_profile_time = time.time() - get_profile_time_start
	get_profile_took = time.time() - get_profile_time_start
	return "「 Bots Speed 」\n • Took : %.3fms\n • Taken: %.5f" % (get_profile_took,get_profile_time)

def command(text):
	vyna = text.lower()
	if settings['setKey']['status']:
		if vyna.startswith(settings['setKey']['key']):
			cmd = vyna.replace(settings['setKey']['key'],'')
		else:
			cmd = 'Undefined command'
	else:
		cmd = text.lower()
	return cmd

def removeCmd(text, key=''):
	if key == '':
		setKey = '' if not settings['setKey']['status'] else settings['setKey']['key']
	else:
		setKey = key
	text_ = text[len(setKey):]
	sep = text_.split(' ')
	return text_[len(sep[0] + ' '):]

def commands():
	key = '' if not settings['setKey']['status'] else settings['setKey']['key']
	with open('help.txt', 'r') as f:
		text = f.read()
	helpMessage = text.format(key=key.title())
	return helpMessage

def RECEIVE_MESSAGE(op):
	global cmd
	global text
	global groupParam
	msg = op.message
	text = msg.text
	reply = msg.id
	receiver = msg.to
	sender = msg._from
	if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
		if msg.toType == 0:
			if sender != cl.profile.mid:
				to = sender
			else:
				to = receiver
		if msg.toType == 1:
			to = receiver
		if msg.toType == 2:
			to = receiver
		if msg.contentType == 1:
			if sender in creator or sender in owner:
				if mid in settings["sentinelPict"]:
					path0 = cl.downloadObjectMsg(msg.id)
					del settings["sentinelPict"][mid]
					cl.updateProfilePicture(path0)
					cl.sendReplyMessage(reply,receiver,"「 Profile Picture 」\nSuccess Change Profile Picture")
				if K1mid in settings["sentinelPict"]:
					path1 = k1.downloadObjectMsg(msg.id)
					del settings["sentinelPict"][K1mid]
					k1.updateProfilePicture(path1)
					k1.sendReplyMessage(reply,receiver,"「 Profile Picture 」\nSuccess Change Profile Picture")
				if K2mid in settings["sentinelPict"]:
					path2 = k2.downloadObjectMsg(msg.id)
					del settings["sentinelPict"][K2mid]
					k2.updateProfilePicture(path2)
					k2.sendReplyMessage(reply,receiver,"「 Profile Picture 」\nSuccess Change Profile Picture")
				if K3mid in settings["sentinelPict"]:
					path3 = k3.downloadObjectMsg(msg.id)
					del settings["sentinelPict"][K3mid]
					k3.updateProfilePicture(path3)
					k3.sendReplyMessage(reply,receiver,"「 Profile Picture 」\nSuccess Change Profile Picture")
				if K4mid in settings["sentinelPict"]:
					path4 = k4.downloadObjectMsg(msg.id)
					del settings["sentinelPict"][K4mid]
					k4.updateProfilePicture(path4)
					k4.sendReplyMessage(reply,receiver,"「 Profile Picture 」\nSuccess Change Profile Picture")
				if K5mid in settings["sentinelPict"]:
					path5 = k5.downloadObjectMsg(msg.id)
					del settings["sentinelPict"][K5mid]
					k5.updateProfilePicture(path5)
					k5.sendReplyMessage(reply,receiver,"「 Profile Picture 」\nSuccess Change Profile Picture")
				if K6mid in settings["sentinelPict"]:
					path6 = k6.downloadObjectMsg(msg.id)
					del settings["sentinelPict"][K6mid]
					k6.updateProfilePicture(path6)
					k6.sendReplyMessage(reply,receiver,"「 Profile Picture 」\nSuccess Change Profile Picture")
				if K7mid in settings["sentinelPict"]:
					path7 = k7.downloadObjectMsg(msg.id)
					del settings["sentinelPict"][K7mid]
					k7.updateProfilePicture(path7)
					k7.sendReplyMessage(reply,receiver,"「 Profile Picture 」\nSuccess Change Profile Picture")
				if K8mid in settings["sentinelPict"]:
					path8 = k8.downloadObjectMsg(msg.id)
					del settings["sentinelPict"][K8mid]
					k8.updateProfilePicture(path8)
					k8.sendReplyMessage(reply,receiver,"「 Profile Picture 」\nSuccess Change Profile Picture")
				if K9mid in settings["sentinelPict"]:
					path9 = k9.downloadObjectMsg(msg.id)
					del settings["sentinelPict"][K9mid]
					k9.updateProfilePicture(path9)
					k9.sendReplyMessage(reply,receiver,"「 Profile Picture 」\nSuccess Change Profile Picture")
				if K10mid in settings["sentinelPict"]:
					path10 = k10.downloadObjectMsg(msg.id)
					del settings["sentinelPict"][K10mid]
					k10.updateProfilePicture(path10)
					k10.sendReplyMessage(reply,receiver,"「 Profile Picture 」\nSuccess Change Profile Picture")
		if msg.contentType == 0:
			if text is None:
				return
			else:
				sentinel = command(text)
				uwew = " ".join(sentinel.split())
			for uwew in sentinel.split(' & '):
				if uwew == "help":
					if sender in creator or sender in owner or sender in admin or sender in staff:
						cl.sendReplyMessage(reply,receiver,commands())
				elif uwew == "รี":
					if sender in creator or sender in owner or sender in admin or sender in staff:
						cl.sendReplyMessage(reply,receiver,"「 Please Wait... 」")
						settings["restartPoint"] = receiver
						restartProgram()
				elif uwew == "ลบแชท":
					if sender in creator or sender in owner or sender in admin or sender in staff:
						for a in Botslist:
							a.removeAllMessages(op.param2)
						for u in Botslist:
							u.sendReplyMessage(reply,receiver,"「 All Chat Cleared 」")
				elif uwew == "b":
					if sender in creator or sender in owner or sender in admin or sender in staff:
						k1.sendReplyMessage(reply,receiver,"「 {} อยู่ค่ะเจ้านาย..」".format(resp1))
						k2.sendReplyMessage(reply,receiver,"「 {} อยู่ค่ะเจ้านาย..」".format(resp2))
						k3.sendReplyMessage(reply,receiver,"「 {} อยู่ค่ะเจ้านาย..」".format(resp3))
						k4.sendReplyMessage(reply,receiver,"「 {} อยู่ค่ะเจ้านาย..」".format(resp4))
						k5.sendReplyMessage(reply,receiver,"「 {} อยู่ค่ะเจ้านาย..」".format(resp5))
						k6.sendReplyMessage(reply,receiver,"「 {} อยู่ค่ะเจ้านาย..」".format(resp6))
						k7.sendReplyMessage(reply,receiver,"「 {} อยู่ค่ะเจ้านาย..」".format(resp7))
						k8.sendReplyMessage(reply,receiver,"「 {} อยู่ค่ะเจ้านาย..」".format(resp8))
						k9.sendReplyMessage(reply,receiver,"「 {} อยู่ค่ะเจ้านาย..」".format(resp9))
						k10.sendReplyMessage(reply,receiver,"「 {} อยู่ค่ะเจ้านาย..」".format(resp10))
				elif uwew == "sp":
					if sender in creator or sender in owner or sender in admin or sender in staff:
						k1.sendReplyMessage(reply,receiver,logspeed())
						k2.sendReplyMessage(reply,receiver,logspeed())
						k3.sendReplyMessage(reply,receiver,logspeed())
						k4.sendReplyMessage(reply,receiver,logspeed())
						k5.sendReplyMessage(reply,receiver,logspeed())
						k6.sendReplyMessage(reply,receiver,logspeed())
						k7.sendReplyMessage(reply,receiver,logspeed())
						k8.sendReplyMessage(reply,receiver,logspeed())
						k9.sendReplyMessage(reply,receiver,logspeed())
						k10.sendReplyMessage(reply,receiver,logspeed())
				elif uwew == "bye":
					if sender in creator or sender in owner or sender in admin or sender in staff:
						for bot in Botslist:
							bot.leaveGroup(receiver)
				elif uwew == "ivb":
					if sender in creator or sender in owner or sender in admin or sender in staff:
						try:
							cl.inviteIntoGroup(receiver, [K1mid,K2mid,K3mid,K4mid,K5mid,K6mid,K7mid,K8mid,K9mid,K10mid])
							k1.acceptGroupInvitation(receiver)
							k2.acceptGroupInvitation(receiver)
							k3.acceptGroupInvitation(receiver)
							k4.acceptGroupInvitation(receiver)
							k5.acceptGroupInvitation(receiver)
							k6.acceptGroupInvitation(receiver)
							k7.acceptGroupInvitation(receiver)
							k8.acceptGroupInvitation(receiver)
							k9.acceptGroupInvitation(receiver)
							k10.acceptGroupInvitation(receiver)
						except TalkException as talk_error:
							if talk_error.code == 35:
								G = cl.getGroup(receiver)
								G.preventedJoinByTicket = False
								cl.updateGroup(G)
								links = cl.reissueGroupTicket(receiver)
								for bot in KAC:
									bot.acceptGroupInvitationByTicketV2(receiver,links)
								G = cl.getGroup(receiver)
								G.preventedJoinByTicket = True
								cl.updateGroup(G)
				elif uwew == "blacklist" or uwew == "bc":
					if sender in creator or sender in owner or sender in admin or sender in staff:
						if len(status["blacklist"]) > 0:
							h = [a for a in status["blacklist"]]
							k = len(h)//20
							for aa in range(k+1):
								if aa == 0:dd = '「Blacklist」';no=aa
								else:dd = '';no=aa*20
								msgas = dd
								for a in h[aa*20:(aa+1)*20]:
									no+=1
									if no == len(h):msgas+='\n{}. @!'.format(no)
									else:msgas += '\n{}. @!'.format(no)
								sendMention(to, msgas, h[aa*20:(aa+1)*20])
						else:
							cl.sendReplyMessage(reply,receiver,"「 Blacklist User -_- 」")
				elif uwew == "cb":
					if sender in creator or sender in owner or sender in admin or sender in staff:
						if len(status["blacklist"]) > 0:
							cl.sendReplyMessage(reply,receiver, "「ล้างดำ {} คน」".format(len(status["blacklist"])))
							status["blacklist"].clear()
						else:
							cl.sendReplyMessage(reply,receiver,"「 Blacklist User -_- 」")
				elif uwew == "squad list":
					if sender in creator or sender in owner or sender in admin or sender in staff:
						ma = ""
						a = 0
						for anu in mybots:
							a = a + 1
							end = '\n'
							ma += '┣ ' + str(a) + ". " +cl.getContact(anu).displayName + "\n"
						cl.sendReplyMessage(reply,receiver, "┏━ sᴇɴᴛɪɴᴇʟ™\n┣━━━━ List Bots\n"+ma+"┗━「%s」Bots" %(str(len(mybots))))
				elif uwew == "view bots":
					if sender in creator or sender in owner or sender in admin or sender in staff:
						ma = ""
						a = 0
						for anu in Bots:
							a = a + 1
							end = '\n'
							ma += '┣ ' + str(a) + ". " +cl.getContact(anu).displayName + "\n"
						cl.sendReplyMessage(reply,receiver, "┏━ sᴇɴᴛɪɴᴇʟ™\n┣━━━━ List Bots\n"+ma+"┗━ Total「%s」Bots" %(str(len(Bots))))
				elif uwew == "view access":
					if sender in creator or sender in owner or sender in admin or sender in staff:
						ma = ""
						mb = ""
						mc = ""
						md = ""
						a = 0
						b = 0
						c = 0
						d = 0
						for anu in creator:
							a = a + 1
							end = '\n'
							ma += '┣ ' + str(a) + ". " +cl.getContact(anu).displayName + "\n"
						for anu in owner:
							b = b + 1
							end = '\n'
							mb += '┣ ' + str(b) + ". " +cl.getContact(anu).displayName + "\n"
						for anu in admin:
							c = c + 1
							end = '\n'
							mc += '┣ ' + str(c) + ". " +cl.getContact(anu).displayName + "\n"
						for anu in staff:
							d = d + 1
							end = '\n'
							md += '┣ ' + str(d) + ". " +cl.getContact(anu).displayName + "\n"
						cl.sendReplyMessage(msg.id, to, "┏╸sᴇɴᴛɪɴᴇʟ™\n┣━━━━ List Access\n┣━━━━ Creator\n"+ma+"┣━━━━ Owner\n"+mb+"┣━━━━ Admin\n"+mc+"┣━━━━ Staff\n"+md+"┗━ Total「%s」Access" %(str(len(creator)+len(owner)+len(admin)+len(staff))))
				elif uwew.startswith("add owner"):
					if sender in creator:
						key = eval(msg.contentMetadata["MENTION"])
						key["MENTIONEES"][0]["M"]
						targets = []
						for x in key["MENTIONEES"]:
							targets.append(x["M"])
						for anunya in Botslist:
							for itunya in targets:
								try:
									anunya.findAndAddContactsByMid(itunya)
								except:
									pass
						for target in targets:
							try:
								status["owner"].append(target)
								sendMention(to,"「 Add Owner 」\nUser @! Added To Owner Access ^_^",[target])
							except:
								pass
					else:
						cl.sendReplyMessage(reply,receiver,"「 Add Owner 」\nCreator Permission -_-")
				elif uwew.startswith("del owner"):
					if sender in creator:
						key = eval(msg.contentMetadata["MENTION"])
						key["MENTIONEES"][0]["M"]
						targets = []
						for x in key["MENTIONEES"]:
							targets.append(x["M"])
						for target in targets:
							try:
								status["owner"].remove(target)
								sendMention(to,"「 Delete Owner 」\nUser @! Deleted From Owner Access ^_^",[target])
							except:
								pass
					else:
						cl.sendReplyMessage(reply,receiver,"「 Delete Owner 」\nCreator Permission -_-")
				elif uwew.startswith("add admin"):
					if sender in creator or sender in owner:
						key = eval(msg.contentMetadata["MENTION"])
						key["MENTIONEES"][0]["M"]
						targets = []
						for x in key["MENTIONEES"]:
							targets.append(x["M"])
						for anunya in Botslist:
							for itunya in targets:
								try:
									anunya.findAndAddContactsByMid(itunya)
								except:
									pass
						for target in targets:
							try:
								status["admin"].append(target)
								sendMention(to,"「 Add Admin 」\nUser @! Added To Admin Access ^_^",[target])
							except:
								pass
					else:
						cl.sendReplyMessage(reply,receiver,"「 Add Admin 」\nOwner Permission -_-")
				elif uwew.startswith("del admin"):
					if sender in creator or sender in owner:
						key = eval(msg.contentMetadata["MENTION"])
						key["MENTIONEES"][0]["M"]
						targets = []
						for x in key["MENTIONEES"]:
							targets.append(x["M"])
						for target in targets:
							try:
								status["admin"].remove(target)
								sendMention(to,"「 Delete Admin 」\nUser @! Deleted From Admin Access ^_^",[target])
							except:
								pass
					else:
						cl.sendReplyMessage(reply,receiver,"「 Delete Admin 」\nOwner Permission -_-")
				elif uwew.startswith("add staff"):
					if sender in creator or sender in owner or sender in admin:
						key = eval(msg.contentMetadata["MENTION"])
						key["MENTIONEES"][0]["M"]
						targets = []
						for x in key["MENTIONEES"]:
							targets.append(x["M"])
						for anunya in Botslist:
							for itunya in targets:
								try:
									anunya.findAndAddContactsByMid(itunya)
								except:
									pass
						for target in targets:
							try:
								status["staff"].append(target)
								sendMention(to,"「 Add Staff 」\nUser @! Added To Staff Access ^_^",[target])
							except:
								pass
					else:
						cl.sendReplyMessage(reply,receiver,"「 Add Staff 」\nOwner/Admin Permission -_-")
				elif uwew.startswith("del staff"):
					if sender in creator or sender in owner or sender in admin:
						key = eval(msg.contentMetadata["MENTION"])
						key["MENTIONEES"][0]["M"]
						targets = []
						for x in key["MENTIONEES"]:
							targets.append(x["M"])
						for target in targets:
							try:
								status["staff"].remove(target)
								sendMention(to,"「 Delete Staff 」\nUser @! Deleted From Staff Access ^_^",[target])
							except:
								pass
					else:
						cl.sendReplyMessage(reply,receiver,"「 Delete Staff 」\nOwner/Admin Permission -_-")
				elif uwew.startswith("add squad"):
					if sender in creator or sender in owner:
						key = eval(msg.contentMetadata["MENTION"])
						key["MENTIONEES"][0]["M"]
						targets = []
						for x in key["MENTIONEES"]:
							targets.append(x["M"])
						for anunya in Botslist:
							for itunya in targets:
								try:
									anunya.findAndAddContactsByMid(itunya)
								except:
									pass
						for target in targets:
							try:
								status["mybots"].append(target)
								sendMention(to,"「 Add Squad 」\nUser @!",[target])
							except:
								pass
					else:
						cl.sendReplyMessage(reply,receiver,"「 Add Squad 」\nOwner Permission -_-")
				elif uwew.startswith("del squad"):
					if sender in creator or sender in owner:
						key = eval(msg.contentMetadata["MENTION"])
						key["MENTIONEES"][0]["M"]
						targets = []
						for x in key["MENTIONEES"]:
							targets.append(x["M"])
						for target in targets:
							try:
								status["mybots"].remove(target)
								sendMention(to,"「 Delete Squad 」\nUser @! Deleted From Squad List ^_^",[target])
							except:
								pass
					else:
						cl.sendReplyMessage(reply,receiver,"「 Delete Squad 」\nOwner Permission -_-")
				elif uwew.startswith("add ban"):
					if sender in creator or sender in owner:
						key = eval(msg.contentMetadata["MENTION"])
						key["MENTIONEES"][0]["M"]
						targets = []
						for x in key["MENTIONEES"]:
							targets.append(x["M"])
						for target in targets:
							try:
								status["blacklist"].append(target)
								sendMention(to,"「 Add Blacklist 」\nUser @! Added To Blacklist User",[target])
							except:
								pass
					else:
						cl.sendReplyMessage(reply,receiver,"「 Add Blacklist 」\nOwner Permission -_-")
				elif uwew.startswith("del ban"):
					if sender in creator or sender in owner:
						key = eval(msg.contentMetadata["MENTION"])
						key["MENTIONEES"][0]["M"]
						targets = []
						for x in key["MENTIONEES"]:
							targets.append(x["M"])
						for target in targets:
							try:
								status["blacklist"].remove(target)
								sendMention(to,"「 Delete Blacklist 」\nUser @! Deleted From Blacklist User",[target])
							except:
								pass
					else:
						cl.sendReplyMessage(reply,receiver,"「 Delete Blacklist 」\nOwner Permission -_-")
				elif uwew.startswith("lock "):
					if sender in creator or sender in owner or sender in admin or sender in staff:
						spl = uwew.replace("lock ","")
						if spl == "on":
							if receiver in status["lock"]:
								uwew = "Group Already Locked -_-"
							else:
								status["lock"].append(receiver)
								uwew = "Owkayy,Group Locked Now~"
							cl.sendReplyMessage(reply,receiver,"「 Lock Group 」\n" + uwew)
						if spl == "off":
							if receiver in status["lock"]:
								status["lock"].remove(receiver)
								uwew = "Owkayy,Group Unlocked Now~"
							else:
								uwew = "Group Already Unlocked -_-"
							cl.sendReplyMessage(reply,receiver,"「 Lock Group 」\n" + uwew)
				elif uwew.startswith("cek"):
					if sender in creator or sender in owner or sender in admin or sender in staff:
						try:k1.inviteIntoGroup(to, [K1mid]);has = "OK"
						except:has = "NOT"
						try:k1.kickoutFromGroup(to, [K1mid]);has1 = "OK"
						except:has1 = "NOT"
						if has == "OK":sil = "OK.✔"
						else:sil = "Down!"
						if has1 == "OK":sil1 = "OK.✔"
						else:sil1 = "Down!"
						k1.sendReplyMessage(reply, receiver, "「 Bots Status 」\n • Invite : {}\n • Kick : {}".format(sil1,sil))
						try:k2.inviteIntoGroup(to, [K2mid]);has = "OK"
						except:has = "NOT"
						try:k2.kickoutFromGroup(to, [K2mid]);has1 = "OK"
						except:has1 = "NOT"
						if has == "OK":sil = "OK.✔"
						else:sil = "Down!"
						if has1 == "OK":sil1 = "OK.✔"
						else:sil1 = "Down!"
						k2.sendReplyMessage(reply, receiver, "「 Bots Status 」\n • Invite : {}\n • Kick : {}".format(sil1,sil))
						try:k3.inviteIntoGroup(to, [K3mid]);has = "OK"
						except:has = "NOT"
						try:k3.kickoutFromGroup(to, [K3mid]);has1 = "OK"
						except:has1 = "NOT"
						if has == "OK":sil = "OK.✔"
						else:sil = "Down!"
						if has1 == "OK":sil1 = "OK.✔"
						else:sil1 = "Down!"
						k3.sendReplyMessage(reply, receiver, "「 Bots Status 」\n • Invite : {}\n • Kick : {}".format(sil1,sil))
						try:k4.inviteIntoGroup(to, [K4mid]);has = "OK"
						except:has = "NOT"
						try:k4.kickoutFromGroup(to, [K4mid]);has1 = "OK"
						except:has1 = "NOT"
						if has == "OK":sil = "OK.✔"
						else:sil = "Down!"
						if has1 == "OK":sil1 = "OK.✔"
						else:sil1 = "Down!"
						k4.sendReplyMessage(reply, receiver, "「 Bots Status 」\n • Invite : {}\n • Kick : {}".format(sil1,sil))
						try:k5.inviteIntoGroup(to, [K5mid]);has = "OK"
						except:has = "NOT"
						try:k5.kickoutFromGroup(to, [K5mid]);has1 = "OK"
						except:has1 = "NOT"
						if has == "OK":sil = "OK.✔"
						else:sil = "Down!"
						if has1 == "OK":sil1 = "OK.✔"
						else:sil1 = "Down!"
						k5.sendReplyMessage(reply, receiver, "「 Bots Status 」\n • Invite : {}\n • Kick : {}".format(sil1,sil))
						try:k6.inviteIntoGroup(to, [K6mid]);has = "OK"
						except:has = "NOT"
						try:k6.kickoutFromGroup(to, [K6mid]);has1 = "OK"
						except:has1 = "NOT"
						if has == "OK":sil = "OK.✔"
						else:sil = "Down!"
						if has1 == "OK":sil1 = "OK.✔"
						else:sil1 = "Down!"
						k6.sendReplyMessage(reply, receiver, "「 Bots Status 」\n • Invite : {}\n • Kick : {}".format(sil1,sil))
						try:k7.inviteIntoGroup(to, [K7mid]);has = "OK"
						except:has = "NOT"
						try:k7.kickoutFromGroup(to, [K7mid]);has1 = "OK"
						except:has1 = "NOT"
						if has == "OK":sil = "OK.✔"
						else:sil = "Down!"
						if has1 == "OK":sil1 = "OK.✔"
						else:sil1 = "Down!"
						k7.sendReplyMessage(reply, receiver, "「 Bots Status 」\n • Invite : {}\n • Kick : {}".format(sil1,sil))
						try:k8.inviteIntoGroup(to, [K8mid]);has = "OK"
						except:has = "NOT"
						try:k8.kickoutFromGroup(to, [K8mid]);has1 = "OK"
						except:has1 = "NOT"
						if has == "OK":sil = "OK.✔"
						else:sil = "Down!"
						if has1 == "OK":sil1 = "OK.✔"
						else:sil1 = "Down!"
						k8.sendReplyMessage(reply, receiver, "「 Bots Status 」\n • Invite : {}\n • Kick : {}".format(sil1,sil))
						try:k9.inviteIntoGroup(to, [K9mid]);has = "OK"
						except:has = "NOT"
						try:k9.kickoutFromGroup(to, [K9mid]);has1 = "OK"
						except:has1 = "NOT"
						if has == "OK":sil = "OK.✔"
						else:sil = "Down!"
						if has1 == "OK":sil1 = "OK.✔"
						else:sil1 = "Down!"
						k9.sendReplyMessage(reply, receiver, "「 Bots Status 」\n • Invite : {}\n • Kick : {}".format(sil1,sil))
						try:k10.inviteIntoGroup(to, [K10mid]);has = "OK"
						except:has = "NOT"
						try:k10.kickoutFromGroup(to, [K10mid]);has1 = "OK"
						except:has1 = "NOT"
						if has == "OK":sil = "OK.✔"
						else:sil = "Down!"
						if has1 == "OK":sil1 = "OK.✔"
						else:sil1 = "Down!"
						k10.sendReplyMessage(reply, receiver, "「 Bots Status 」\n • Invite : {}\n • Kick : {}".format(sil1,sil))
				elif uwew.startswith("ชื่อ0 "):
					if sender in creator or sender in owner:
						sep = text.split(" ")
						name = text.replace(sep[0] + " ","")
						if len(name) <= 99999999:
							dname0 = cl.getProfile()
							dname0.displayName = name
							cl.updateProfile(dname0)
							cl.sendReplyMessage(reply,receiver,"「 Display Name 」\nDisplay Name Changed To {}".format(str(name)))
					else:
						cl.sendReplyMessage(reply,receiver,"「 Display Name 」\nAccess Limited For Owner Only -_-")
				elif uwew.startswith("ชื่อ1 "):
					if sender in creator or sender in owner:
						sep = text.split(" ")
						name = text.replace(sep[0] + " ","")
						if len(name) <= 99999999:
							dname1 = k1.getProfile()
							dname1.displayName = name
							k1.updateProfile(dname1)
							k1.sendReplyMessage(reply,receiver,"「 Display Name 」\nDisplay Name Changed To {}".format(str(name)))
					else:
						k1.sendReplyMessage(reply,receiver,"「 Display Name 」\nAccess Limited For Owner Only -_-")
				elif uwew.startswith("ชื่อ2 "):
					if sender in creator or sender in owner:
						sep = text.split(" ")
						name = text.replace(sep[0] + " ","")
						if len(name) <= 99999999:
							dname2 = k2.getProfile()
							dname2.displayName = name
							k2.updateProfile(dname2)
							k2.sendReplyMessage(reply,receiver,"「 Display Name 」\nDisplay Name Changed To {}".format(str(name)))
					else:
						k2.sendReplyMessage(reply,receiver,"「 Display Name 」\nAccess Limited For Owner Only -_-")
				elif uwew.startswith("ชื่อ3 "):
					if sender in creator or sender in owner:
						sep = text.split(" ")
						name = text.replace(sep[0] + " ","")
						if len(name) <= 99999999:
							dname3 = k3.getProfile()
							dname3.displayName = name
							k3.updateProfile(dname3)
							k3.sendReplyMessage(reply,receiver,"「 Display Name 」\nDisplay Name Changed To {}".format(str(name)))
					else:
						k3.sendReplyMessage(reply,receiver,"「 Display Name 」\nAccess Limited For Owner Only -_-")
				elif uwew.startswith("ชื่อ4 "):
					if sender in creator or sender in owner:
						sep = text.split(" ")
						name = text.replace(sep[0] + " ","")
						if len(name) <= 99999999:
							dname4 = k4.getProfile()
							dname4.displayName = name
							k4.updateProfile(dname4)
							k4.sendReplyMessage(reply,receiver,"「 Display Name 」\nDisplay Name Changed To {}".format(str(name)))
					else:
						k4.sendReplyMessage(reply,receiver,"「 Display Name 」\nAccess Limited For Owner Only -_-")
				elif uwew.startswith("ชื่อ5 "):
					if sender in creator or sender in owner:
						sep = text.split(" ")
						name = text.replace(sep[0] + " ","")
						if len(name) <= 99999999:
							dname5 = k5.getProfile()
							dname5.displayName = name
							k5.updateProfile(dname5)
							k5.sendReplyMessage(reply,receiver,"「 Display Name 」\nDisplay Name Changed To {}".format(str(name)))
					else:
						k5.sendReplyMessage(reply,receiver,"「 Display Name 」\nAccess Limited For Owner Only -_-")
				elif uwew.startswith("ชื่อ6 "):
					if sender in creator or sender in owner:
						sep = text.split(" ")
						name = text.replace(sep[0] + " ","")
						if len(name) <= 99999999:
							dname6 = k6.getProfile()
							dname6.displayName = name
							k6.updateProfile(dname6)
							k6.sendReplyMessage(reply,receiver,"「 Display Name 」\nDisplay Name Changed To {}".format(str(name)))
					else:
						k6.sendReplyMessage(reply,receiver,"「 Display Name 」\nAccess Limited For Owner Only -_-")
				elif uwew.startswith("ชื่อ7 "):
					if sender in creator or sender in owner:
						sep = text.split(" ")
						name = text.replace(sep[0] + " ","")
						if len(name) <= 99999999:
							dname7 = k7.getProfile()
							dname7.displayName = name
							k7.updateProfile(dname7)
							k7.sendReplyMessage(reply,receiver,"「 Display Name 」\nDisplay Name Changed To {}".format(str(name)))
					else:
						k7.sendReplyMessage(reply,receiver,"「 Display Name 」\nAccess Limited For Owner Only -_-")
				elif uwew.startswith("ชื่อ8 "):
					if sender in creator or sender in owner:
						sep = text.split(" ")
						name = text.replace(sep[0] + " ","")
						if len(name) <= 99999999:
							dname8 = k8.getProfile()
							dname8.displayName = name
							k8.updateProfile(dname8)
							k8.sendReplyMessage(reply,receiver,"「 Display Name 」\nDisplay Name Changed To {}".format(str(name)))
					else:
						k8.sendReplyMessage(reply,receiver,"「 Display Name 」\nAccess Limited For Owner Only -_-")
				elif uwew.startswith("ชื่อ9 "):
					if sender in creator or sender in owner:
						sep = text.split(" ")
						name = text.replace(sep[0] + " ","")
						if len(name) <= 99999999:
							dname9 = k9.getProfile()
							dname9.displayName = name
							k9.updateProfile(dname9)
							k9.sendReplyMessage(reply,receiver,"「 Display Name 」\nDisplay Name Changed To {}".format(str(name)))
					else:
						k9.sendReplyMessage(reply,receiver,"「 Display Name 」\nAccess Limited For Owner Only -_-")
				elif uwew.startswith("ชื่อ10 "):
					if sender in creator or sender in owner:
						sep = text.split(" ")
						name = text.replace(sep[0] + " ","")
						if len(name) <= 99999999:
							dname10 = k10.getProfile()
							dname10.displayName = name
							k10.updateProfile(dname10)
							k10.sendReplyMessage(reply,receiver,"「 Display Name 」\nDisplay Name Changed To {}".format(str(name)))
					else:
						k10.sendReplyMessage(reply,receiver,"「 Display Name 」\nAccess Limited For Owner Only -_-")
				elif uwew.startswith("ชื่อทั้งหมด "):
					if sender in creator or sender in owner:
						sep = text.split(" ")
						name = text.replace(sep[0] + " ","")
						if len(name) <= 99999999:
							dname0 = cl.getProfile()
							dname0.displayName = name
							cl.updateProfile(dname0)
							cl.sendReplyMessage(reply,receiver,"「 Display Name 」\nDisplay Name Changed To {}".format(str(name)))
							dname1 = k1.getProfile()
							dname1.displayName = name
							k1.updateProfile(dname1)
							k1.sendReplyMessage(reply,receiver,"「 Display Name 」\nDisplay Name Changed To {}".format(str(name)))
							dname2 = k2.getProfile()
							dname2.displayName = name
							k2.updateProfile(dname2)
							k2.sendReplyMessage(reply,receiver,"「 Display Name 」\nDisplay Name Changed To {}".format(str(name)))
							dname3 = k3.getProfile()
							dname3.displayName = name
							k3.updateProfile(dname3)
							k3.sendReplyMessage(reply,receiver,"「 Display Name 」\nDisplay Name Changed To {}".format(str(name)))
							dname4 = k4.getProfile()
							dname4.displayName = name
							k4.updateProfile(dname4)
							k4.sendReplyMessage(reply,receiver,"「 Display Name 」\nDisplay Name Changed To {}".format(str(name)))
							dname5 = k5.getProfile()
							dname5.displayName = name
							k5.updateProfile(dname5)
							k5.sendReplyMessage(reply,receiver,"「 Display Name 」\nDisplay Name Changed To {}".format(str(name)))
							dname6 = k6.getProfile()
							dname6.displayName = name
							k6.updateProfile(dname6)
							k6.sendReplyMessage(reply,receiver,"「 Display Name 」\nDisplay Name Changed To {}".format(str(name)))
							dname7 = k7.getProfile()
							dname7.displayName = name
							k7.updateProfile(dname7)
							k7.sendReplyMessage(reply,receiver,"「 Display Name 」\nDisplay Name Changed To {}".format(str(name)))
							dname8 = k8.getProfile()
							dname8.displayName = name
							k8.updateProfile(dname8)
							k8.sendReplyMessage(reply,receiver,"「 Display Name 」\nDisplay Name Changed To {}".format(str(name)))
							dname9 = k9.getProfile()
							dname9.displayName = name
							k9.updateProfile(dname9)
							k9.sendReplyMessage(reply,receiver,"「 Display Name 」\nDisplay Name Changed To {}".format(str(name)))
							dname10 = k10.getProfile()
							dname10.displayName = name
							k10.updateProfile(dname10)
							k10.sendReplyMessage(reply,receiver,"「 Display Name 」\nDisplay Name Changed To {}".format(str(name)))
					else:
						for a in Botslist:
							a.sendReplyMessage(reply,receiver,"「 Display Name 」\nAccess Limited For Owner Only -_-")
				elif uwew.startswith("ตัส0 "):
					if sender in creator or sender in owner:
						sep = text.split(" ")
						name = text.replace(sep[0] + " ","")
						if len(name) <= 99999999:
							bio0 = cl.getProfile()
							bio0.statusMessage = name
							cl.updateProfile(bio0)
							cl.sendReplyMessage(reply,receiver,"「 Status Message 」\nStatus Message Changed To {}".format(str(name)))
					else:
						cl.sendReplyMessage(reply,receiver,"「 Status Message 」\nAccess Limited For Owner Only -_-")
				elif uwew.startswith("ตัส1 "):
					if sender in creator or sender in owner:
						sep = text.split(" ")
						name = text.replace(sep[0] + " ","")
						if len(name) <= 99999999:
							bio1 = k1.getProfile()
							bio1.statusMessage = name
							k1.updateProfile(bio1)
							k1.sendReplyMessage(reply,receiver,"「 Status Message 」\nStatus Message Changed To {}".format(str(name)))
					else:
						k1.sendReplyMessage(reply,receiver,"「 Status Message 」\nAccess Limited For Owner Only -_-")
				elif uwew.startswith("ตัส2 "):
					if sender in creator or sender in owner:
						sep = text.split(" ")
						name = text.replace(sep[0] + " ","")
						if len(name) <= 99999999:
							bio2 = k2.getProfile()
							bio2.statusMessage = name
							k2.updateProfile(bio2)
							k2.sendReplyMessage(reply,receiver,"「 Status Message 」\nStatus Message Changed To {}".format(str(name)))
					else:
						k2.sendReplyMessage(reply,receiver,"「 Status Message 」\nAccess Limited For Owner Only -_-")
				elif uwew.startswith("ตัส3 "):
					if sender in creator or sender in owner:
						sep = text.split(" ")
						name = text.replace(sep[0] + " ","")
						if len(name) <= 99999999:
							bio3 = k3.getProfile()
							bio3.statusMessage = name
							k3.updateProfile(bio3)
							k3.sendReplyMessage(reply,receiver,"「 Status Message 」\nStatus Message Changed To {}".format(str(name)))
					else:
						k3.sendReplyMessage(reply,receiver,"「 Status Message 」\nAccess Limited For Owner Only -_-")
				elif uwew.startswith("ตัส4 "):
					if sender in creator or sender in owner:
						sep = text.split(" ")
						name = text.replace(sep[0] + " ","")
						if len(name) <= 99999999:
							bio4 = k4.getProfile()
							bio4.statusMessage = name
							k4.updateProfile(bio4)
							k4.sendReplyMessage(reply,receiver,"「 Status Message 」\nStatus Message Changed To {}".format(str(name)))
					else:
						k4.sendReplyMessage(reply,receiver,"「 Status Message 」\nAccess Limited For Owner Only -_-")
				elif uwew.startswith("ตัส5 "):
					if sender in creator or sender in owner:
						sep = text.split(" ")
						name = text.replace(sep[0] + " ","")
						if len(name) <= 99999999:
							bio5 = k5.getProfile()
							bio5.statusMessage = name
							k5.updateProfile(bio5)
							k5.sendReplyMessage(reply,receiver,"「 Status Message 」\nStatus Message Changed To {}".format(str(name)))
					else:
						k5.sendReplyMessage(reply,receiver,"「 Status Message 」\nAccess Limited For Owner Only -_-")
				elif uwew.startswith("ตัส6 "):
					if sender in creator or sender in owner:
						sep = text.split(" ")
						name = text.replace(sep[0] + " ","")
						if len(name) <= 99999999:
							bio6 = k6.getProfile()
							bio6.statusMessage = name
							k6.updateProfile(bio6)
							k6.sendReplyMessage(reply,receiver,"「 Status Message 」\nStatus Message Changed To {}".format(str(name)))
					else:
						k6.sendReplyMessage(reply,receiver,"「 Status Message 」\nAccess Limited For Owner Only -_-")
				elif uwew.startswith("ตัส7 "):
					if sender in creator or sender in owner:
						sep = text.split(" ")
						name = text.replace(sep[0] + " ","")
						if len(name) <= 99999999:
							bio7 = k7.getProfile()
							bio7.statusMessage = name
							k7.updateProfile(bio7)
							k7.sendReplyMessage(reply,receiver,"「 Status Message 」\nStatus Message Changed To {}".format(str(name)))
					else:
						k7.sendReplyMessage(reply,receiver,"「 Status Message 」\nAccess Limited For Owner Only -_-")
				elif uwew.startswith("ตัส8 "):
					if sender in creator or sender in owner:
						sep = text.split(" ")
						name = text.replace(sep[0] + " ","")
						if len(name) <= 99999999:
							bio8 = k8.getProfile()
							bio8.statusMessage = name
							k8.updateProfile(bio8)
							k8.sendReplyMessage(reply,receiver,"「 Status Message 」\nStatus Message Changed To {}".format(str(name)))
					else:
						k8.sendReplyMessage(reply,receiver,"「 Status Message 」\nAccess Limited For Owner Only -_-")
				elif uwew.startswith("ตัส9 "):
					if sender in creator or sender in owner:
						sep = text.split(" ")
						name = text.replace(sep[0] + " ","")
						if len(name) <= 99999999:
							bio9 = k9.getProfile()
							bio9.statusMessage = name
							k9.updateProfile(bio9)
							k9.sendReplyMessage(reply,receiver,"「 Status Message 」\nStatus Message Changed To {}".format(str(name)))
					else:
						k9.sendReplyMessage(reply,receiver,"「 Status Message 」\nAccess Limited For Owner Only -_-")
				elif uwew.startswith("ตัส10 "):
					if sender in creator or sender in owner:
						sep = text.split(" ")
						name = text.replace(sep[0] + " ","")
						if len(name) <= 99999999:
							bio10 = k10.getProfile()
							bio10.statusMessage = name
							k10.updateProfile(bio10)
							k10.sendReplyMessage(reply,receiver,"「 Status Message 」\nStatus Message Changed To {}".format(str(name)))
					else:
						k10.sendReplyMessage(reply,receiver,"「 Status Message 」\nAccess Limited For Owner Only -_-")
				elif uwew.startswith("ตัสทั้งหมด "):
					if sender in creator or sender in owner:
						sep = text.split(" ")
						name = text.replace(sep[0] + " ","")
						if len(name) <= 99999999:
							bio0 = cl.getProfile()
							bio0.statusMessage = name
							cl.updateProfile(bio0)
							cl.sendReplyMessage(reply,receiver,"「 Status Message 」\nStatus Message Changed To {}".format(str(name)))
							bio1 = k1.getProfile()
							bio1.statusMessage = name
							k1.updateProfile(bio1)
							k1.sendReplyMessage(reply,receiver,"「 Status Message 」\nStatus Message Changed To {}".format(str(name)))
							bio2 = k2.getProfile()
							bio2.statusMessage = name
							k2.updateProfile(bio2)
							k2.sendReplyMessage(reply,receiver,"「 Status Message 」\nStatus Message Changed To {}".format(str(name)))
							bio3 = k3.getProfile()
							bio3.statusMessage = name
							k3.updateProfile(bio3)
							k3.sendReplyMessage(reply,receiver,"「 Status Message 」\nStatus Message Changed To {}".format(str(name)))
							bio4 = k4.getProfile()
							bio4.statusMessage = name
							k4.updateProfile(bio4)
							k4.sendReplyMessage(reply,receiver,"「 Status Message 」\nStatus Message Changed To {}".format(str(name)))
							bio5 = k5.getProfile()
							bio5.statusMessage = name
							k5.updateProfile(bio5)
							k5.sendReplyMessage(reply,receiver,"「 Status Message 」\nStatus Message Changed To {}".format(str(name)))
							bio6 = k6.getProfile()
							bio6.statusMessage = name
							k6.updateProfile(bio6)
							k6.sendReplyMessage(reply,receiver,"「 Status Message 」\nStatus Message Changed To {}".format(str(name)))
							bio7 = k7.getProfile()
							bio7.statusMessage = name
							k7.updateProfile(bio7)
							k7.sendReplyMessage(reply,receiver,"「 Status Message 」\nStatus Message Changed To {}".format(str(name)))
							bio8 = k8.getProfile()
							bio8.statusMessage = name
							k8.updateProfile(bio8)
							k8.sendReplyMessage(reply,receiver,"「 Status Message 」\nStatus Message Changed To {}".format(str(name)))
							bio9 = k9.getProfile()
							bio9.statusMessage = name
							k9.updateProfile(bio9)
							k9.sendReplyMessage(reply,receiver,"「 Status Message 」\nStatus Message Changed To {}".format(str(name)))
							bio10 = k10.getProfile()
							bio10.statusMessage = name
							k10.updateProfile(bio10)
							k10.sendReplyMessage(reply,receiver,"「 Status Message 」\nStatus Message Changed To {}".format(str(name)))
					else:
						for a in Botslist:
							a.sendReplyMessage(reply,receiver,"「 Status Message 」\nAccess Limited For Owner Only -_-")
				elif uwew.startswith("อัพ"):
					if sender in creator or sender in owner:
						spl = uwew.replace("อัพ","")
						if spl == "0":
							settings["sentinelPict"][mid] = True
							cl.sendReplyMessage(reply,receiver,"「 Profile Picture 」\nPlease Send Picture You Want To Use")
						if spl == "1":
							settings["sentinelPict"][K1mid] = True
							k1.sendReplyMessage(reply,receiver,"「 Profile Picture 」\nPlease Send Picture You Want To Use")
						if spl == "2":
							settings["sentinelPict"][K2mid] = True
							k2.sendReplyMessage(reply,receiver,"「 Profile Picture 」\nPlease Send Picture You Want To Use")
						if spl == "3":
							settings["sentinelPict"][K3mid] = True
							k3.sendReplyMessage(reply,receiver,"「 Profile Picture 」\nPlease Send Picture You Want To Use")
						if spl == "4":
							settings["sentinelPict"][K4mid] = True
							k4.sendReplyMessage(reply,receiver,"「 Profile Picture 」\nPlease Send Picture You Want To Use")
						if spl == "5":
							settings["sentinelPict"][K5mid] = True
							k5.sendReplyMessage(reply,receiver,"「 Profile Picture 」\nPlease Send Picture You Want To Use")
						if spl == "6":
							settings["sentinelPict"][K6mid] = True
							k6.sendReplyMessage(reply,receiver,"「 Profile Picture 」\nPlease Send Picture You Want To Use")
						if spl == "7":
							settings["sentinelPict"][K7mid] = True
							k7.sendReplyMessage(reply,receiver,"「 Profile Picture 」\nPlease Send Picture You Want To Use")
						if spl == "8":
							settings["sentinelPict"][K8mid] = True
							k8.sendReplyMessage(reply,receiver,"「 Profile Picture 」\nPlease Send Picture You Want To Use")
						if spl == "9":
							settings["sentinelPict"][K9mid] = True
							k9.sendReplyMessage(reply,receiver,"「 Profile Picture 」\nPlease Send Picture You Want To Use")
						if spl == "10":
							settings["sentinelPict"][K10mid] = True
							k10.sendReplyMessage(reply,receiver,"「 Profile Picture 」\nPlease Send Picture You Want To Use")
						if spl == "รูป":
							settings["sentinelPict"][mid] = True
							settings["sentinelPict"][K1mid] = True
							settings["sentinelPict"][K2mid] = True
							settings["sentinelPict"][K3mid] = True
							settings["sentinelPict"][K4mid] = True
							settings["sentinelPict"][K5mid] = True
							settings["sentinelPict"][K6mid] = True
							settings["sentinelPict"][K7mid] = True
							settings["sentinelPict"][K8mid] = True
							settings["sentinelPict"][K9mid] = True
							settings["sentinelPict"][K10mid] = True
							for a in Botslist:
								a.sendReplyMessage(reply,receiver,"「 Profile Picture 」\nPlease Send Picture You Want To Use")
					else:
						cl.sendReplyMessage(reply,receiver,"「 Profile Picture 」\nAccess Limited For Owner Only -_-")
				elif uwew.startswith("bk"):
					if sender in creator or sender in owner or sender in admin or sender in staff:
						key = eval(msg.contentMetadata["MENTION"])
						key["MENTIONEES"][0]["M"]
						targets = []
						for x in key["MENTIONEES"]:
							targets.append(x["M"])
						for target in targets:
							if target in creator or target in owner or target in admin or target in staff or target in Bots or target in mybots:
								pass
							else:
								try:
									hihi = threading.Thread(target=blacklist, args=(target,)).start()
									huhu = threading.Thread(target=kick, args=(receiver, target)).start()
								except:
									pass

async def cerberusRun():
	if settings["restartPoint"] is not None:
		res = "「 รีระบบเรียบร้อย ^_^ 」"
		targets = cl.getGroupIdsJoined()
		for target in targets:
			try:
				cl.sendMessage(target, res)
			except TalkException:
				pass
			settings["restartPoint"] = None
	while 1:
		try:
			en = cl.poll.fetchOperations(cl.revision, 50)
			for op in en:
				if op.type != 0:
					cl.revision = max(cl.revision, op.revision)
					if op.type == 11:
						if op.param1 in status["lock"]:
							if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
								pass
							else:
								t = threading.Thread(target=blacklist, args=(op.param2,)).start()
								try:
									t1 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
									t2 = threading.Thread(target=lockqr, args=(op.param1,)).start()
								except:
									pass
						if op.param2 in status["blacklist"]:
							if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
								pass
							else:
								try:
									t3 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
									t4 = threading.Thread(target=lockqr, args=(op.param1,)).start()
								except:
									pass
						if op.param3 in status["blacklist"]:
							if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
								pass
							else:
								try:
									t5 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
									t6 = threading.Thread(target=lockqr, args=(op.param1,)).start()
								except:
									pass
					if op.type == 13:
						if op.param1 in status["lock"]:
							if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
								pass
							else:
								t7 = threading.Thread(target=blacklist, args=(op.param2,)).start()
								try:
									t8 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
									t9 = threading.Thread(target=cancel, args=(op.param1, op.param3)).start()
								except:
									pass
						if op.param2 in status["blacklist"]:
							if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
								pass
							else:
								try:
									t10 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
									t11 = threading.Thread(target=cancel, args=(op.param1, op.param3)).start()
								except:
									pass
						if op.param3 in status["blacklist"]:
							if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
								pass
							else:
								try:
									t12 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
									t13 = threading.Thread(target=cancel, args=(op.param1, op.param3)).start()
								except:
									pass
						if mid in op.param3:
							if settings["autoJoin"] == True:
								if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
									cl.acceptGroupInvitation(op.param1)
								else:
									cl.acceptGroupInvitation(op.param1)
									sendMention(op.param1,"Sorry @!,\nI Will Leave Because You Doesn't Have Access -_-",[op.param2])
									cl.leaveGroup(op.param1)
						if K1mid in op.param3:
							if settings["autoJoin"] == True:
								if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
									k1.acceptGroupInvitation(op.param1)
								else:
									k1.acceptGroupInvitation(op.param1)
									sendMention(op.param1,"Sorry @!,\nI Will Leave Because You Doesn't Have Access -_-",[op.param2])
									k1.leaveGroup(op.param1)
						if K2mid in op.param3:
							if settings["autoJoin"] == True:
								if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
									k2.acceptGroupInvitation(op.param1)
								else:
									k2.acceptGroupInvitation(op.param1)
									sendMention(op.param1,"Sorry @!,\nI Will Leave Because You Doesn't Have Access -_-",[op.param2])
									k2.leaveGroup(op.param1)
						if K3mid in op.param3:
							if settings["autoJoin"] == True:
								if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
									k3.acceptGroupInvitation(op.param1)
								else:
									k3.acceptGroupInvitation(op.param1)
									sendMention(op.param1,"Sorry @!,\nI Will Leave Because You Doesn't Have Access -_-",[op.param2])
									k3.leaveGroup(op.param1)
						if K4mid in op.param3:
							if settings["autoJoin"] == True:
								if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
									k4.acceptGroupInvitation(op.param1)
								else:
									k4.acceptGroupInvitation(op.param1)
									sendMention(op.param1,"Sorry @!,\nI Will Leave Because You Doesn't Have Access -_-",[op.param2])
									k4.leaveGroup(op.param1)
						if K5mid in op.param3:
							if settings["autoJoin"] == True:
								if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
									k5.acceptGroupInvitation(op.param1)
								else:
									k5.acceptGroupInvitation(op.param1)
									sendMention(op.param1,"Sorry @!,\nI Will Leave Because You Doesn't Have Access -_-",[op.param2])
									k5.leaveGroup(op.param1)
						if K6mid in op.param3:
							if settings["autoJoin"] == True:
								if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
									k6.acceptGroupInvitation(op.param1)
								else:
									k6.acceptGroupInvitation(op.param1)
									sendMention(op.param1,"Sorry @!,\nI Will Leave Because You Doesn't Have Access -_-",[op.param2])
									k6.leaveGroup(op.param1)
						if K7mid in op.param3:
							if settings["autoJoin"] == True:
								if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
									k7.acceptGroupInvitation(op.param1)
								else:
									k7.acceptGroupInvitation(op.param1)
									sendMention(op.param1,"Sorry @!,\nI Will Leave Because You Doesn't Have Access -_-",[op.param2])
									k7.leaveGroup(op.param1)
						if K8mid in op.param3:
							if settings["autoJoin"] == True:
								if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
									k8.acceptGroupInvitation(op.param1)
								else:
									k8.acceptGroupInvitation(op.param1)
									sendMention(op.param1,"Sorry @!,\nI Will Leave Because You Doesn't Have Access -_-",[op.param2])
									k8.leaveGroup(op.param1)
						if K9mid in op.param3:
							if settings["autoJoin"] == True:
								if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
									k9.acceptGroupInvitation(op.param1)
								else:
									k9.acceptGroupInvitation(op.param1)
									sendMention(op.param1,"Sorry @!,\nI Will Leave Because You Doesn't Have Access -_-",[op.param2])
									k9.leaveGroup(op.param1)
						if K10mid in op.param3:
							if settings["autoJoin"] == True:
								if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
									k10.acceptGroupInvitation(op.param1)
								else:
									k10.acceptGroupInvitation(op.param1)
									sendMention(op.param1,"Sorry @!,\nI Will Leave Because You Doesn't Have Access -_-",[op.param2])
									k10.leaveGroup(op.param1)
					if op.type == 17:
						if op.param1 in status["lock"]:
							if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
								pass
							else:
								try:
									t14 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
									t15 = threading.Thread(target=blacklist, args=(op.param2,)).start()
								except:
									pass
						if op.param2 in status["blacklist"]:
							if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
								pass
							else:
								try:
									t16 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
								except:
									pass
					if op.type == 19:
						if op.param1 in status["lock"]:
							if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
								pass
							else:
								t17 = threading.Thread(target=blacklist, args=(op.param2,)).start()
								try:
									t18 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
								except:
									pass
						if op.param3 in mid:
							if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
								pass
							else:
								t19 = threading.Thread(target=blacklist, args=(op.param2,)).start()
								try:
									t20 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
									t21 = threading.Thread(target=backup, args=(op.param1, op.param3)).start()
									t22 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
								except:
									pass
						if op.param3 in K1mid:
							if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
								pass
							else:
								t23 = threading.Thread(target=blacklist, args=(op.param2,)).start()
								try:
									t24 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
									t25 = threading.Thread(target=backup, args=(op.param1, op.param3)).start()
									t26 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
								except:
									pass
						if op.param3 in K2mid:
							if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
								pass
							else:
								t27 = threading.Thread(target=blacklist, args=(op.param2,)).start()
								try:
									t28 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
									t29 = threading.Thread(target=backup, args=(op.param1, op.param3)).start()
									t30 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
								except:
									pass
						if op.param3 in K3mid:
							if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
								pass
							else:
								t31 = threading.Thread(target=blacklist, args=(op.param2,)).start()
								try:
									t32 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
									t33 = threading.Thread(target=backup, args=(op.param1, op.param3)).start()
									t34 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
								except:
									pass
						if op.param3 in K4mid:
							if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
								pass
							else:
								t35 = threading.Thread(target=blacklist, args=(op.param2,)).start()
								try:
									t36 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
									t37 = threading.Thread(target=backup, args=(op.param1, op.param3)).start()
									t38 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
								except:
									pass
						if op.param3 in K5mid:
							if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
								pass
							else:
								t39 = threading.Thread(target=blacklist, args=(op.param2,)).start()
								try:
									t40 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
									t41 = threading.Thread(target=backup, args=(op.param1, op.param3)).start()
									t42 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
								except:
									pass
						if op.param3 in K6mid:
							if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
								pass
							else:
								t43 = threading.Thread(target=blacklist, args=(op.param2,)).start()
								try:
									t44 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
									t45 = threading.Thread(target=backup, args=(op.param1, op.param3)).start()
									t46 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
								except:
									pass
						if op.param3 in K7mid:
							if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
								pass
							else:
								t47 = threading.Thread(target=blacklist, args=(op.param2,)).start()
								try:
									t48 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
									t49 = threading.Thread(target=backup, args=(op.param1, op.param3)).start()
									t50 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
								except:
									pass
						if op.param3 in K8mid:
							if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
								pass
							else:
								t51 = threading.Thread(target=blacklist, args=(op.param2,)).start()
								try:
									t52 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
									t53 = threading.Thread(target=backup, args=(op.param1, op.param3)).start()
									t54 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
								except:
									pass
						if op.param3 in K9mid:
							if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
								pass
							else:
								t55 = threading.Thread(target=blacklist, args=(op.param2,)).start()
								try:
									t56 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
									t57 = threading.Thread(target=backup, args=(op.param1, op.param3)).start()
									t58 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
								except:
									pass
						if op.param3 in K10mid:
							if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
								pass
							else:
								t59 = threading.Thread(target=blacklist, args=(op.param2,)).start()
								try:
									t60 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
									t61 = threading.Thread(target=backup, args=(op.param1, op.param3)).start()
									t62 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
								except:
									pass
					if op.type == 32:
						if op.param1 in status["lock"]:
							if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
								pass
							else:
								t63 = threading.Thread(target=blacklist, args=(op.param2,)).start()
								try:
									t64 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
								except:
									pass
						if op.param3 in mid:
							if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
								pass
							else:
								t65 = threading.Thread(target=blacklist, args=(op.param2,)).start()
								try:
									t66 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
									t67 = threading.Thread(target=backup, args=(op.param1, op.param3)).start()
								except:
									pass
						if op.param3 in K1mid:
							if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
								pass
							else:
								t68 = threading.Thread(target=blacklist, args=(op.param2,)).start()
								try:
									t69 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
									t70 = threading.Thread(target=backup, args=(op.param1, op.param3)).start()
								except:
									pass
						if op.param3 in K2mid:
							if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
								pass
							else:
								t71 = threading.Thread(target=blacklist, args=(op.param2,)).start()
								try:
									t72 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
									t73 = threading.Thread(target=backup, args=(op.param1, op.param3)).start()
								except:
									pass
						if op.param3 in K3mid:
							if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
								pass
							else:
								t74 = threading.Thread(target=blacklist, args=(op.param2,)).start()
								try:
									t75 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
									t76 = threading.Thread(target=backup, args=(op.param1, op.param3)).start()
								except:
									pass
						if op.param3 in K4mid:
							if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
								pass
							else:
								t77 = threading.Thread(target=blacklist, args=(op.param2,)).start()
								try:
									t78 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
									t79 = threading.Thread(target=backup, args=(op.param1, op.param3)).start()
								except:
									pass
						if op.param3 in K5mid:
							if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
								pass
							else:
								t80 = threading.Thread(target=blacklist, args=(op.param2,)).start()
								try:
									t81 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
									t82 = threading.Thread(target=backup, args=(op.param1, op.param3)).start()
								except:
									pass
						if op.param3 in K6mid:
							if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
								pass
							else:
								t83 = threading.Thread(target=blacklist, args=(op.param2,)).start()
								try:
									t84 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
									t85 = threading.Thread(target=backup, args=(op.param1, op.param3)).start()
								except:
									pass
						if op.param3 in K7mid:
							if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
								pass
							else:
								t86 = threading.Thread(target=blacklist, args=(op.param2,)).start()
								try:
									t87 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
									t88 = threading.Thread(target=backup, args=(op.param1, op.param3)).start()
								except:
									pass
						if op.param3 in K8mid:
							if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
								pass
							else:
								t89 = threading.Thread(target=blacklist, args=(op.param2,)).start()
								try:
									t90 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
									t91 = threading.Thread(target=backup, args=(op.param1, op.param3)).start()
								except:
									pass
						if op.param3 in K9mid:
							if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
								pass
							else:
								t92 = threading.Thread(target=blacklist, args=(op.param2,)).start()
								try:
									t93 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
									t94 = threading.Thread(target=backup, args=(op.param1, op.param3)).start()
								except:
									pass
						if op.param3 in K10mid:
							if op.param2 in creator or op.param2 in owner or op.param2 in admin or op.param2 in staff or op.param2 in Bots or op.param2 in mybots:
								pass
							else:
								t95 = threading.Thread(target=blacklist, args=(op.param2,)).start()
								try:
									t96 = threading.Thread(target=kick, args=(op.param1, op.param2)).start()
									t97 = threading.Thread(target=backup, args=(op.param1, op.param3)).start()
								except:
									pass
					if op.type == 26:
						RECEIVE_MESSAGE(op)
		except Exception as error:
			error = traceback.format_exc()
			if "EOFError" in error:
				pass
			elif "log_out" in error.lower():
				backupData()
				time.sleep(11)
				python = sys.executable
				os.execl(python, python, *sys.argv)
			elif "ShouldSyncException" in error:
				backupData()
				logError(error)
				time.sleep(11)
				python3 = sys.executable
				os.execl(python3, python3, *sys.argv)
			elif "TalkException(code=8, reason='LOG_OUT', parameterMap=None)" in error:
				backupData()
				logError(error)
				time.sleep(11)
				python = sys.executable
				os.execl(python, python, *sys.argv)
			elif "TalkException(code=20, reason='[UNCAUGHT_INTERNAL_ERROR] [UNCAUGHT_INTERNAL_ERROR] Login from secondary user blocked by userHash + clientType 8cb91561b450b38ccf0119fc4f5e37a3MA', parameterMap=None)" in error:
				backupData()
				logError(error)
				time.sleep(11)
				python = sys.executable
				os.execl(python, python, *sys.argv)
			else:
				traceback.print_exc()
				logError(error)
if __name__ == '__main__':
	print('####==== ระบบเริ่มทำงาน ====####')
	threading.Thread(target=loop.run_until_complete(cerberusRun())).start()
