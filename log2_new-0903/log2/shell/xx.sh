#!/bin/sh
if [ $(basename $0) = $0 ]
then
    ABSPATH=$(type $0|awk '{print $NF}'|sed "s#^\.\/#$(echo ${PWD}/|sed 's!\/!\\\/!g')#")
else
    ABSPATH="${PWD}/$(echo $0|sed 's!^\.\/!!')"
fi
ABSPATH=$(dirname $ABSPATH)
echo $ABSPATH
