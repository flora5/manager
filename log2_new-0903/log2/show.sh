#!/bin/sh

P=$0
[ $(basename $P) = $P ] && P=$(type $P|awk '{print $NF}')
[ $(echo $P|cut -b1-1) = '/' ] || P=${PWD}/$P
ABSPATH=$(dirname $(echo ${P}|sed -e 's/[^\/]*\/\.\.\///g' -e 's/\.\///g'))

if ls .pids/*pid >/dev/null 2>&1
then
for f in $ABSPATH/.pids/*.pid
do
#read pid < $f
pids=$pids','$(cat $f)
done
pids=$(echo $pids|sed 's/^,//')
ps -f -p "$pids"
fi
