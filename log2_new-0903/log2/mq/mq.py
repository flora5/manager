#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Language Version: 2.5.1
# Last Changed: 2009-12-23 13:32:22
"""docstring
"""

__author__ = "Maitreya Dutt Chao (leonardr@segfault.org)"
__version__ = "0.0.1"
__copyright__ = "Copyright (c) 2004-2008 Maitreya Dutt Chao"
__license__ = "New-style BSD"

import re
import sys

class MQ(object):
    def __init__(self):
        self.m = re.compile(r'\w+\((?:\S*|[ ,]+)\)')
    def begin(self, txt):
        if ' DISPLAY ' in txt:
            return False
        return True
    def txt2dict(self, txt):
        d = {}
        for val in self.m.findall(txt):
            k, v = val[:-1].split(r'(', 1)
            d.update({k:v})
        return d

mq = MQ()
d = {}
for line in sys.stdin:
    if mq.begin(line):
        d.update(mq.txt2dict(line))
#print map(mq.txt2dict, filter(mq.begin,sys.stdin))
#print sys.argv[1],''.join(str(d).split())
if len(sys.argv) == 3:
    try:
        #d.update({'STATUS':eval(sys.argv[2].get('STATUS'))})
        d.update(eval(sys.argv[2]))
    except:
        pass
print ''.join(str(d).split())

def test():
    pass

if __name__ == '__main__':
    test()

