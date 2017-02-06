#!/bin/sh
P=$0
[ $(basename $P) = $P ] && P=$(type $P|awk '{print $NF}')
[ $(echo $P|cut -b1-1) = '/' ] || P=${PWD}/$P
ABSPATH=$(dirname $(echo ${P}|sed -e 's/[^\/]*\/\.\.\///g' -e 's/\.\///g'))
#echo 'p:'$ABSPATH

interval=5
#user anonymous anonymous
run()
{
cd $ABSPATH
cd shell
nohup startsys &
cd ../net
nohup startnet &
#cd ../mq
#nohup startmq &
#cd ../oracle
#nohup startora &
cd ..
}


run
#main
