#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#Language Version: 2.6.5
# Last Modified: 2010-08-30 16:57:24

"""docstring
"""

__revision__ = '0.1'

import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, Sequence
import sys, time


engine = sqlalchemy.create_engine('oracle://itsm:itsm@192.168.8.86:1521/ora10', echo=True)
metadata = MetaData()
syslog_table = Table('trap',  metadata,
        Column('ID', Integer, Sequence('id_seq'), primary_key=True),  #'user_id_seq'
        Column('TRAP', String(100)),
        Column('HOST', String(50)),
        )

metadata.create_all(engine)



def save_trap(trap, host):
    ins = trap.insert().values(trap= trap, host= host)
    conn = engine.connecti()
    conn.execute(trap.insert(), [
            {'trap': trap,  'host': host}, 
            ])

