#!/bin/sh
#
# concept:登录用户列表
# input:
# output: 
exists()
{
	type $1 2&>1 /dev/null
	retcode=$?
	return $retcode
}

HEAD="USER     TTY   FROM   LOGIN@   IDLE   JCPU   PCPU WHAT"
#AIX(){ LANG='en_US';w -h|awk '{print $1,$2,$3=" - "$3,$4,$5,$6="-",$7="-"}';}
AIX(){ LANG='en_US';w -h|awk '{print $1,$2,$3=" - "$3,$4,$5,$6="-",$7="-"}';}
Digital(){ :;}
FreeBSD(){ :;}
HP_UX(){ :;}
Irix(){ :;}
Linux(){ HEAD_NF=$(w|awk 'NR==2{print NF}')
    w -h|awk '{
    if(HNF==7)print $1,$2" - "$3,$4,$5,$6,$7"&#10;"$8"&#10;"$9"&#10;"$10"&#10;"$11
    else print $1,$2,$3,$4,$5,$6,$7,$8"&#10;"$9"&#10;"$10"&#10;"$11}' HNF=$HEAD_NF;
    }
OS390(){ :;}
SCO_SV(){ w -h|awk '{print $1,$2" - ",$3,$4,$5,$6,$7"$#10;"$8}';}
SunOS(){
	LC_TIME='en_US.UTF-8'
	w -h|awk '{
	if(NF == 4)print $1,$2,"-",$3,"- - -",$4;
	if(NF == 5)print $1,$2,"-",$3,"- - -",$5;
	if(NF == 6)print $1,$2,"-",$3,$4,$5,"-",$6;
	if(NF == 7)print $1,$2,"-",$3,$4,$5,$6,$7;
	if(NF >= 8)print $1,$2,"-",$3,$4,$5,$6,$7"&#10;"$8"&#10;"$9"&#10;"$10"&#10;"$11"&#10;"$12;
	}'
}
Tru64(){ :;}
UnixWare(){ w -h|awk '{print $1,$2" - ",$3,$4,$5,$6,$7"$#10;"$8}';}
#Win32
default(){ df -k|tail +2|sed 's/%//g';}

INTERVAL=10	# Defines the total number of sampling intervals
#HOST=`hostname`
OS=`uname`	# Defines the UNIX flavor
SECS=30		# Defines the number of seconds for each sample
STATCOUNT=0	# Initialize a loop counter to 0, zero
#DATE=`date "+%Y-%m-%d %H:%M:%S"`

###################################################
##### SETUP THE ENVIRONMENT FOR EACH OS HERE ######
###################################################
#echo $OS
date "+%H:%M:%S"
$OS $*
#x=`$OS $*|tr "\n" " "`
#echo $x|sed "s/[0123456789:\-]* /${DATE} /"
#$OS $*|tr "\n" " "|sed "s/[0123456789:\-]* /${DATE} /"

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
