#!/usr/local/bin/python2.7
#!-*- coding:utf-8 -*-

from subprocess import PIPE,Popen 
import datetime
import sys
import socket
import time
import diamond.collector

#from daemonize import daemonize

#dirname = path.dirname(__file__)
#lib_dir = path.abspath(dirname)
#sys.path.append(lib_dir)
 
MOUTHLIST = {
    'Jan':1,
    'Feb':2,
    'Mar':3,
    'Apr':4,
    'May':5,
    'Jun':6,
    'Jul':7,
    'Aug':8,
    'Sep':9,
    'Oct':10,
    'Nov':11,
    'Dec':12
}

def getNginxLog(ts):
    pf = '/home/web_access_20130821.log'
    now = datetime.datetime.now()
    curtime = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
    n = 1
    while True:
        lines = n * int(ts)
        log = Popen('tail -n %s %s' % (lines, pf), shell=True, stdout=PIPE)
        stdout, stderr = log.communicate()
        for i in stdout.split('\n'):
            try:
                lt = i.strip().split()[3][1:]
            except:
                continue
            day, mouth, other = lt.split('/')
            year, hour, minute, second = other.split(':')
            logtime = datetime.datetime(int(year), int(MOUTHLIST[mouth]), int(day), int(hour), int(minute), int(second))
            if curtime - logtime <= datetime.timedelta(seconds=60):
                n += 1
                break
            else:
                h = now - datetime.timedelta(seconds=60)
                sft = h.strftime('%s')
                return stdout, curtime, sft


def countLogCode():
    log, curtime, stf = getNginxLog(60)
    data = {}
    for i in log.split('\n'):
        try:
            lt = i.strip().split()[3][1:]
        except:
            continue
        day, mouth, other = lt.split('/')
        year, hour, minute, second = other.split(':')
        logtime = datetime.datetime(int(year), int(MOUTHLIST[mouth]), int(day), int(hour), int(minute), int(second))
        if curtime - logtime < datetime.timedelta(seconds=60):
            continue
        else:
            k = i.strip().split()[8]
            if k in data:
                v = data[k] + 1
                data[k] = v
            else:
                data[k] = 1
    return data, stf

class NginxLogCollector(diamond.collector.Collector):
    def collect(self):
        data, stf = countLogCode()
        for k, v in data.items():
            mn = "diamond_http.code_%s" % k
            self.publish(mn ,v)


