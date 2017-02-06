#!/bin/sh
#
#get_memory_prerformance
# 1.1.1.1 接口概念
# 物理层网络接口错误指标
#  1.1.1.2 输入
#  无
#   1.1.1.3 输出
#   total    系统总内存
#   used    用户内存
#    free    空闲内存


exists()
{
	type $1 2&>1 /dev/null
	retcode=$?
	return $retcode
}
AIX(){ 
	if ping -c 1 -w 1 $1 >/dev/null
	then
		echo $?
	else
		ping -c 5 -q $1 > /dev/null; echo $?;
	fi
}
Digital(){ :;}
FreeBSD(){ :;}
HP_UX(){ :;}
Irix(){ :;}
Linux(){ 
	if ping -c 1 -w 1 $1 >/dev/null
	then
		echo $?
	else
		ping -c 5 -q $1 > /dev/null; echo $?;
	fi
}
OS390(){ :;}
SCO_SV(){
	if ping -c 1 -w 1 $1 >/dev/null
	then
		echo $?
	else
		ping -c 5 -q $1 > /dev/null; echo $?;
	fi
}
SunOS(){ 
	if /usr/sbin/ping -c 1 -w 1 $1 >/dev/null
	then
		echo $?
	else
		ping -c 5 -q $1 > /dev/null; echo $?;
	fi
}
Tru64(){ :;}
UnixWare(){ ping -c 5 -q $1 > /dev/null; echo $?;}
#Win32
default(){ ping -c 5 -q $1 > /dev/null; echo $?;}

INTERVAL=10	# Defines the total number of sampling intervals
HOST=`hostname`
OS=`uname`	# Defines the UNIX flavor
SECS=30		# Defines the number of seconds for each sample
STATCOUNT=0	# Initialize a loop counter to 0, zero
#DATE=`date "+%Y-%m-%d %H:%M:%S"`

###################################################
##### SETUP THE ENVIRONMENT FOR EACH OS HERE ######
###################################################
$OS $1
#x=`$OS $*|tr "\n" " "`
#echo $x|sed "s/[0123456789:\-]* /${DATE} /"

# These "F-numbers" point to the correct field in the
# command output for each UNIX flavor.

       #echo " The Operating System is $OS "
##Linux
#exit
#case $OS in
#AIX)
#	$AIX
#       ;;
#HP-UX)
#	$HP_UX
#       ;;
#Linux)
#	echo $Linux
#	exec $Linux
#       ;;
#SCO_SV)
#	$SCO_SV
#       ;;
#SunOS)  
#	$SunOS
#       ;;
#UnixWare)
#	$UnixWare
#       ;;
#*)# echo " ERROR: $OS is not a supported operating system "
#	$default
#  # echo " ...EXITING... "
#   exit 1
#   ;;
#esac
#
####################################################
######### BEGIN GATHERING STATISTICS HERE ##########
####################################################

