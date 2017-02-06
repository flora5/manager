#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Language Version: 2.5.1
# Last Changed: 2009-12-30 17:04:32
"""docstring
"""

__author__ = "Maitreya Dutt Chao (leonardr@segfault.org)"
__version__ = "0.0.1"
__copyright__ = "Copyright (c) 2004-2008 Maitreya Dutt Chao"
__license__ = "New-style BSD"


from multiprocessing import Pool
import time

def f(x):
    time.sleep(5)
    return x*x

if __name__ == '__main__':
    pool = Pool(processes=4)              # start 4 worker processes
    result = pool.apply_async(f, [10])     # evaluate "f(10)" asynchronously
    print result.get(timeout=10)           # prints "100" unless your computer is *very* slow
    print pool.map(f, range(10))          # prints "[0, 1, 4,..., 81]"

#from multiprocessing import Pool
#p = Pool(5)
#def f(x):
#    return x*x
#
#print dir(p)
##p.map(f, [1,2,3])
#
#
#def test():
#    pass
#
#if __name__ == '__main__':
#    test()
#
