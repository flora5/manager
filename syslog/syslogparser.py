#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Language Version: 2.6.4
# Last Modified: 2010-08-30 17:12:13

"""docstring
"""

__author__ = "Maitreya Dutt Chao (leonardr@segfault.org)"
__version__ = "0.0.1"
__copyright__ = "Copyright (c) 2004-2008 Maitreya Dutt Chao"
__license__ = "New-style BSD"

import re
import yaml

class Logmesg(object):
    delimiter = '\s*'
    def __init__(self, configfile):
        self.p = []
        with open(configfile) as fd:
            logmsg = yaml.load(fd)
        for j in logmsg["LOGMSG"]:
            x = ''
            for k in j.split():
                x += '(?P<%s>%s)%s' % (k, logmsg[k], self.delimiter)
            self.p.append((re.compile(x), j.split()))
    def parse(self, mesg):
        d = {}
        for pp,jj in self.p:
            if pp.match(mesg):
                for j in jj:
                    d.update({j:pp.match(mesg).group(j)})
                PRI = d.get('PRI')
                PRI = int(PRI) if PRI else 13
                #if PRI > 191: PRI = 13   #23*8+7=191
                #d.update({'PRI':PRI, 'Facility':PRI>>3, 'Severity':PRI & 0x7, 'TIMESTAMP':parse_date(d.get('TIMESTAMP'))})
                d['PRI'] = str(PRI)
                d['Facility'] = str(PRI >> 3)
                d['Severity'] = str(PRI & 0x7)
                return d

d = {'SERV': 'kernel:', 'HOST': 'zhaowp-desktop', 'MESG': '[90088.460367] IN=eth1 OUT= MAC=ff:ff:ff:ff:ff:ff:00:1e:37:ce:24:75:08:00 SRC=10.3.2.13 DST=10.3.2.255 LEN=78 TOS=0x00 PREC=0x00 TTL=128 ID=5250 PROTO=UDP SPT=137 DPT=137 LEN=58', 'TIME': 'Oct 10 09:30:14'}
def escape(s):
    return  s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', '&quot;').replace("'", "&#39;")
def dict2xml(d):
    xml = ''
    for k,v in d.items():
        xml += '<%s>%s</%s>\n' % (k,escape(v),k)
    return xml

if __name__ == "__main__":
    data = r"Oct 10 09:30:14 zhaowp-desktop kernel: [90088.460367] IN=eth1 OUT= MAC=ff:ff:ff:ff:ff:ff:00:1e:37:ce:24:75:08:00 SRC=10.3.2.13 DST=10.3.2.255 LEN=78 TOS=0x00 PREC=0x00 TTL=128 ID=5250 PROTO=UDP SPT=137 DPT=137 LEN=58"
    ao = Logmesg('syslog.yml')
#    fd = open("messages")
    #data = fd.readline()
    for data in fd:
    #print 'yyyyyyyyyyyyyyyyy'
        xx = ao.parse(data)
        if not xx:
            print 'data:',data
            break
        print 'output:', xx
    #(?P<TIME>(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) [1 ]\d \d\d:\d\d:\d\d)(?P<HOST>\w+)(?P<SERV>.+?:\s)(?P<MESG>.+?)
 #   print dir(d)
  #  print dict2xml(d)

