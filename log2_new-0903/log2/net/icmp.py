#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Language Version: 2.5.1
# Last Changed: 2010-01-07 15:35:23
"""docstring
"""

__author__ = "Maitreya Dutt Chao (leonardr@segfault.org)"
__version__ = "0.0.1"
__copyright__ = "Copyright (c) 2004-2008 Maitreya Dutt Chao"
__license__ = "New-style BSD"
aix1  = '''PING 192.168.0.111: (192.168.0.111): 56 data bytes

----192.168.0.111 PING Statistics----
10 packets transmitted, 0 packets received, 100% packet loss'''

aix2 = '''PING 192.168.1.18: (192.168.1.18): 56 data bytes

----192.168.1.18 PING Statistics----
10 packets transmitted, 10 packets received, 0% packet loss
round-trip min/avg/max = 0/0/0 ms'''

linux1 = '''PING 192.168.0.222 (192.168.0.222) 56(84) bytes of data.

--- 192.168.0.222 ping statistics ---
10 packets transmitted, 10 received, 0% packet loss, time 8998ms
rtt min/avg/max/mdev = 0.268/0.321/0.369/0.034 ms'''

linux2 = '''PING 192.168.0.221 (192.168.0.221) 56(84) bytes of data.

--- 192.168.0.221 ping statistics ---
10 packets transmitted, 0 received, +8 errors, 100% packet loss, time 9011ms
, pipe 3'''

def test():
    pass

if __name__ == '__main__':
    test()

