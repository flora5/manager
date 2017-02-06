XPWD=$(type $0)
echo 'oo:'$XPWD
if [ $? -eq 0 ]
then
WRKDIR=$(dirname $(echo $XPWD|awk '{print $NF}'))
else
WRKDIR=$(dirname "$(pwd)/$(echo $0|sed 's/^\.\///')")
fi
echo 'xx:'$WRKDIR

for x in $(echo $PATH|sed 's/:/ /g')
do
echo $x
done
