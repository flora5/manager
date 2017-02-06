#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Language Version: 2.5.1
# Last Changed: 2009-08-24 09:29:04
"""docstring
"""

__author__ = "Maitreya Dutt Chao (leonardr@segfault.org)"
__version__ = "0.0.1"
__copyright__ = "Copyright (c) 2004-2008 Maitreya Dutt Chao"
__license__ = "New-style BSD"

from ctypes import *

class _anoninfo(Structure):
    _fields_ = [
    ('ani_max', c_ulong),
    ('ani_free', c_ulong),
    ('ani_resv', c_ulong),
            ]

def test():
    libc = CDLL("/usr/lib/libC.so.5")
    anon = _anoninfo()
    pagesizes = libc.sysconf(11)
    if libc.swapctl(5, byref(anon)) == -1:
        print '-',0,0,0
    else:
        total = anon.ani_max * pagesizes;
        used  = anon.ani_resv * pagesizes;
        free  = total - used;
    print '-',total>>10,used>>10,free>>10

if __name__ == '__main__':
    test()

