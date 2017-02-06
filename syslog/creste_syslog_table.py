#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#Language Version: 2.6.5
# Last Modified: 2010-08-30 16:57:24

"""docstring
"""

__revision__ = '0.1'

engine = sqlalchemy.create_engine('oracle://itsm:itsm@192.168.8.86:1521/ora10', echo=True)
metadata = MetaData()
syslog_table = Table('sys_log',  metadata,
        Column('ID', Integer, Sequence('id_seq'), primary_key=True),  #'user_id_seq'
        Column('SERV', String(100)),
        Column('HOST', String(50)),
        Column('MESG', String(100)),
        Column('TIMES', DateTime),
        Column('TIME_STAMP', TIMESTAMP), #Time_stamp  flot second
        Column('FACILITY',  Integer),
        Column('SEVERITY',  Integer),
        )

metadata.create_all(engine)
