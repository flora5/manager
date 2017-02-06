import yaml, sys
isrun = file('Conf/isrun.yaml', 'w')
#isRun = [0]
isRun = sys.argv[1]
is_run = yaml.dump(isRun, isrun)
isrun.close()

