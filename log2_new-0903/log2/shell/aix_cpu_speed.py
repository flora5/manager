#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Language Version: 2.6.4
# Last Modified: 2010-07-02 08:36:56

"""
Determining microprocessor speed
FROM: http://publib.boulder.ibm.com/infocenter/pseries/v5r3/index.jsp?topic=/com.ibm.aix.prftungd/doc/prftungd/deter_cpu_speed.htm
"""

__author__ = "Maitreya Dutt Chao (leonardr@segfault.org)"
__version__ = "0.0.1"
__copyright__ = "Copyright (c) 2004-2008 Maitreya Dutt Chao"
__license__ = "New-style BSD"

#When using AIX® 5.1 and subsequent releases, the following code returns the processor speed in hertz (Hz):
#lsattr -E -l proc0 | grep "Processor Speed"
#When using earlier releases than AIX 5.1:
import os
#xxyyyyyymmss = os.uname()
#(the numbers to use to determine microprocessor speed)
xxyyyyyymmss =  '00C97AC04C00'
Unique_CPU_ID = xxyyyyyymmss[2:8]
Model_ID = xxyyyyyymmss[8:10]
Submodel = xxyyyyyymmss[10:12]
#print Model_ID
#('AIX', 'aix', '3', '5', '00C97AC04C00')
#Model ID    Machine Type            Processor Speed          Architecture
mmtable = {'02':('7015-930',25,'Power'),
 '10':('7013-530',25,               'Power'),
 '10':('7016-730',25,               'Power'),
 '11':('7013-540',30,               'Power'),
 '14':('7013-540',30,               'Power'),
 '18':('7013-53H',33,               'Power'),
 '1C':('7013-550',41.6,             'Power'),
 '20':('7015-930',25,               'Power'),
 '2E':('7015-950',41,               'Power'),
 '30':('7013-520',20,               'Power'),
 '31':('7012-320',20,               'Power'),
 '34':('7013-52H',25,               'Power'),
 '35':('7012-32H',25,               'Power'),
 '37':('7012-340',33,               'Power'),
 '38':('7012-350',41,               'Power'),
 '41':('7011-220',33,               'RSC'),
 '43':('7008-M20',33,               'Power'),
 '43':('7008-M2A',33,               'Power'),
 '46':('7011-250',66,               'PowerPC'),
 '47':('7011-230',45,               'RSC'),
 '48':('7009-C10',80,               'PowerPC'),
 '4C':('        ',                  'See Note 1.'),
 '57':('7012-390',67,               'Power2'),
 '57':('7030-3BT',67,               'Power2'),
 '57':('9076-SP2 Thin',67,          'Power2'),
 '58':('7012-380',59,               'Power2'),
 '58':('7030-3AT',59,               'Power2'),
 '59':('7012-39H',67,               'Power2'),
 '59':('9076-SP2 Thin w/L2',67,     'Power2'),
 '5C':('7013-560',50                ,'Power'),
 '63':('7015-970',50                ,'Power'),
 '63':('7015-97B',50                ,'Power'),
 '64':('7015-980',62.5              ,'Power'),
 '64':('7015-98B',62.5              ,'Power'),
 '66':('7013-580',62.5              ,'Power'),
 '67':('7013-570',50                ,'Power'),
 '67':('7015-R10',50                ,'Power'),
 '70':('7013-590',66                ,'Power2'),
 '70':('9076-SP2 Wide',66           ,'Power2'),
 '71':('7013-58H',55                ,'Power2'),
 '72':('7013-59H',66                ,'Power2'),
 '72':('7015-R20',66                ,'Power2'),
 '72':('9076-SP2 Wide',66           ,'Power2'),
 '75':('7012-370',62                ,'Power'),
 '75':('7012-375',62                ,'Power'),
 '75':('9076-SP1 Thin',62           ,'Power'),
 '76':('7012-360',50                ,'Power'),
 '76':('7012-365',50                ,'Power'),
 '77':('7012-350',41                ,'Power'),
 '77':('7012-355',41                ,'Power'),
 '77':('7013-55L',41.6              ,'Power'),
 '79':('7013-591',77                ,'Power2'),
 '79':('9076-SP2 Wide',77           ,'Power2'),
 '80':('7015-990',71.5              ,'Power2'),
 '81':('7015-R24',71.5              ,'Power2'),
 '89':('7013-595',135               ,'P2SC'),
 '89':('9076-SP2 Wide',135          ,'P2SC'),
 '94':('7012-397',160               ,'P2SC'),
 '94':('9076-SP2 Thin',160          ,'P2SC'),
 'A0':('7013-J30',75                ,'PowerPC'),
 'A1':('7013-J40',112               ,'PowerPC'),
 'A3':('7015-R30','See Note 2.'     ,'PowerPC'),
 'A4':('7015-R40','See Note 2.'     ,'PowerPC'),
 'A4':('7015-R50','See Note 2.'     ,'PowerPC'),
 'A4':('9076-SP2 High','See Note 2.','PowerPC'),
 'A6':('7012-G30','See Note 2.'     ,'PowerPC'),
 'A7':('7012-G40','See Note 2.'     ,'PowerPC'),
 'C0':('7024-E20','See Note 3.'     ,'PowerPC'),
 'C0':('7024-E30','See Note 3.'     ,'PowerPC'),
 'C4':('7025-F30','See Note 3.'     ,'PowerPC'),
 'F0':('7007-N40',50                ,'ThinkPad')}

if Model_ID == '4C':
    mmtable.update({'4C': ''})
if Model_ID == '4C':
    mmtable.update({'4C': ''})
if Model_ID == '4C':
    mmtable.update({'4C': ''})
if Model_ID == '4C':
    mmtable.update({'4C': ''})
if Model_ID == '4C':
    mmtable.update({'4C': ''})
if Model_ID == '4C':
    mmtable.update({'4C': ''})
if Model_ID == '4C':
    mmtable.update({'4C': ''})
#note1=
#uname -M           Machine Type    Processor Speed    Processor Architecture
#IBM,7017-S70         7017-S70          125                RS64
#IBM,7017-S7A         7017-S7A          262                RD64-II
#IBM,7017-S80         7017-S80          450                RS-III
#IBM,7025-F40         7025-F40          166/233            PowerPC
#IBM,7025-F50         7025-F50          See Note 4.        PowerPC
#IBM,7026-H10         7026-H10          166/233            PowerPC
#IBM,7026-H50         7026-H50          See Note 4.        PowerPC
#IBM,7026-H70         7026-H70          340                RS64-II
#IBM,7042/7043 (ED)   7043-140          166/200/233/332    PowerPC
#IBM,7042/7043 (ED)   7043-150          375                PowerPC
#IBM,7042/7043 (ED)   7043-240          166/233            PowerPC
#IBM,7043-260         7043-260          200                Power3
#IBM,7248             7248-100          100                PowerPersonal
#IBM,7248             7248-120          120                PowerPersonal
#IBM,7248             7248-132          132                PowerPersonal
#IBM,9076-270      9076-SP Silver Node  See Note 4.        PowerPC

#note2=
## lscfg -vl cpucard0 | grep FRU
#FRU Number    Processor Type    Processor Speed
#     E1D           PowerPC 601       75
#     C1D           PowerPC 601       75
#     C4D           PowerPC 604       112
#     E4D           PowerPC 604       112
#     X4D           PowerPC 604e      200

#note3=
## lscfg -vp | pg
#
#Look for the following stanza:
#
#procF0                              CPU Card
#
#Part Number.................093H5280
#EC Level....................00E76527
#Serial Number...............17700008
#FRU Number..................093H2431
#Displayable Message.........CPU Card
#Device Specific.(PL)........
#Device Specific.(ZA)........PS=166,PB=066,PCI=033,NP=001,CL=02,PBH
#                                         Z=64467000,PM=2.5,L2=1024
#Device Specific.(RM)........10031997 140951 VIC97276
#ROS Level and ID............03071997 135048
#
#In the section Device Specific.(ZA), the section PS= is the processor speed expressed in MHz.

#note4=
## lscfg -vp | more
#
#Look for the following stanza:
#
#Orca M5 CPU:
#Part Number.................08L1010
#EC Level....................E78405
#Serial Number...............L209034579
#FRU Number..................93H8945
#Manufacture ID..............IBM980
#Version.....................RS6K
#Displayable Message.........OrcaM5 CPU DD1.3
#Product Specific.(ZC).......PS=0013c9eb00,PB=0009e4f580,SB=0004f27
#                                         ac0,NP=02,PF=461,PV=05,KV=01,CL=1
#
#In the line containing Product Specific.(ZC), the entry PS= is the processor speed in hexadecimal notation. To convert this to an actual speed, use the following conversions:
#
#0009E4F580 = 166 MHz
#0013C9EB00 = 332 MHz
#
#The value PF= indicates the processor configuration.
#
#251 = 1 way 166 MHz
#261 = 2 way 166 MHz
#451 = 1 way 332 MHz
#461 = 2 way 332 MHz


if __name__ == "__main__":
    print mmtable
#
