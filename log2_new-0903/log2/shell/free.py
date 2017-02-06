#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Language Version: 2.5.1
# Last Changed: 2009-06-23 16:44:43
'''
SunOS 内存使用状态检测
'''

import ctypes
sc = ctypes.CDLL('/usr/lib/libC.so.5').sysconf
ps = sc(11) >> 10
total = sc(500) * ps
free = sc(501) * ps
used = total - free
print '-', total, used, free

