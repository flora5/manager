#!/bin/sh
P=$0
[ $(basename $P) = $P ] && P=$(type $P|awk '{print $NF}')
[ $(echo $P|cut -b1-1) = '/' ] || P=${PWD}/$P
ABSPATH=$(dirname $(echo ${P}|sed -e 's/[^\/]*\/\.\.\///g' -e 's/\.\///g'))

for f in $ABSPATH/.pids/*.pid
do
echo 'Stoping '$f
kill -2 $(cat $f)

sleep 1
if [ -f $f ]
then
    echo "Stop $f failed, try to force stop it."
    kill -9 $(cat $f)
    rm $f
else
    echo "Stop $f successed."
fi

done
echo 'Stoped all'

