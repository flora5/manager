import yaml,  time
import pickle

"""
while 1:
    stream = file('Conf/cmdinfo.yaml', 'r')
    cmdinfo = yaml.load(stream)
    for item_name in cmdinfo.keys():
        if cmdinfo[item_name] != []:
            print "good"
        else:
            print "no mission now"
    time.sleep(1)

"""


stream = file('Conf/host.yaml', 'r')
counter = yaml.load(stream)  # now the counter is None
if counter ==None:
    print "good"



