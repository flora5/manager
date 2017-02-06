#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Language Version: 2.5.1
# Last Changed: 2009-08-14 14:37:26
"""
!               debug           mdir            qc              send
$               dir             mget            sendport        site
account         disconnect      mkdir           put             size
append          exit            mls             pwd             status
ascii           form            mode            quit            struct
bell            get             modtime         quote           system
binary          glob            mput            recv            sunique
bye             hash            newer           reget           tenex
case            help            nmap            rstatus         tick
cd              idle            nlist           rhelp           trace
cdup            image           ntrans          rename          type
chmod           lcd             open            reset           user
close           ls              prompt          restart         umask
cr              macdef          passive         rmdir           verbose
delete          mdelete         proxy           runique         ?
"""


__author__ = "Maitreya Dutt Chao (leonardr@segfault.org)"
__version__ = "0.0.1"
__copyright__ = "Copyright (c) 2004-2008 Maitreya Dutt Chao"
__license__ = "New-style BSD"

import sys
import os
import ftplib
class FTPHost(object):
    '''
    Connected to hxfz2.
    No proxy connection.
    Mode: stream; Type: binary; Form: non-print; Structure: file
    Verbose: on; Bell: off; Prompting: on; Globbing: on
    Store unique: off; Receive unique: off
    Case: off; CR stripping: on
    Quote control characters: on
    Ntrans: off
    Nmap: off
    Hash mark printing: off; Use of PORT cmds: on
    Tick counter printing: off
    '''
    def __init__(self, ip, port): #*args, **kwargs):
        self.ftp = ftplib.FTP()   # connect to host, default port
        self.ftp.connect(ip, port)
        #ftp.set_debuglevel(5)
        #ftp.login(v['USER'], v['PASSWD'])               # user anonymous, passwd anonymous@
        self._current_dir = os.getcwd()
        self.curdir, self.pardir, self.sep = '.', '..', '/'

    def login(self, user, passwd):
        self.ftp.login(user, passwd)

    def bin(self):
        pass
    def bye(self):
        self.ftp.quit()
    def cd(self):
        pass
    def close(self):
        pass
    def delete(self):
        pass
    def lcd(self, path):
        if os.path.exists(path):
            #os.chdir(path)
            self._current_dir = path
            return True
        else:
            return False

    def ls(self):
        return self.ftp.retrlines('LIST')     # list directory contents
    def mirror(self, dir):
        pass
    def open(self, host):
        pass
    def get(self, remote_file, local_file = None):
        if not local_file:
            local_file = os.path.abspath(os.path.basename(remote_file))
        #x.retrbinary(command, callback[, blocksize[, rest) : used to retrieve a file in binary mode.
        fd = open(local_file, 'wb')
        self.ftp.retrbinary('RETR ' + local_file, fd.write)
        fd.close()
        pass

    def put(self, local_file, remote_file = None):
        if not remote_file:
            remote_file = os.path.basename(local_file)
        fd = open(local_file, 'rb')
        self.ftp.storbinary("STOR " + remote_file, fd)
        fd.close()

import glob
import socket
hostname = socket.gethostname()
def test():
    #print 'host:', sys.argv[1]
    #print 'PORT:', sys.argv[2]
    #print 'user:', sys.argv[3]
    #print 'pass:', sys.argv[4]
    try:
        ftp = FTPHost(sys.argv[1], sys.argv[2])
        ftp.login(sys.argv[3], sys.argv[4])
        for f in glob.glob("upload/get*"):
            xx = os.path.split(f)[1]
            #print 'send:', sys.argv[5] + "/" + xx + "@" + hostname
            ftp.put(f, sys.argv[5] + "/" + xx + "@" + hostname)
        ftp.bye()
    except socket.error, e:
        print e
#ftp = FTPHost("localhost", 2121)
#ftp.login("zhaowp", "1234")
#print ftp.ls()

#ftp = FTP('hxfz2')   # connect to host, default port
#ftp.login('python', 'ufc123')               # user anonymous, passwd anonymous@
#print ftp.retrlines('LIST')     # list directory contents
#print dir(ftp)
#print dir(ftplib)
#x.retrbinary(command, callback[, blocksize[, rest) : used to retrieve a file in binary mode.
#print ftp.retrbinary('RETR README', open('README', 'wb').write)
#storbinary("STOR " + filename,f)
#ftp.quit()

if __name__ == '__main__':
    #ftp = FTPHost("hxfz2", "21")
    #    ftp.login("python", "ufc123")
    #    for f in glob.glob("upload/get*"):
    #    ftp.put(f, xx + "" + hostname)
    #    ftp.bye()
    test()

