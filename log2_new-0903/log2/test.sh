#!/bin/sh
test -z "$PWD"  && PWD=$(pwd)
test -z "$PWD"  && echo 'xxxoo' || echo 'ooxx'
if [ $(basename $0) = $0 ]
then
    ABSPATH=$(type $0|awk '{print $NF}'|sed "s/^\.\//$(echo ${PWD}/|sed 's/\//\\\//g')/")
else
    ABSPATH="${PWD}/$(echo $0|sed 's/^\.\///')"
fi
ABSPATH=$(dirname $ABSPATH)
#echo $ABSPATH

interval=5
#user anonymous anonymous
run()
{
cd $ABSPATH
echo $ABSPATH
cd shell
pwd

}


run
#main
