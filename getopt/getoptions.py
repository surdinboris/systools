import sys
import getopt

cmds=sys.argv[1:]

opts, args=getopt.getopt(cmds, 'u:', ['namef=','namet','push'])

print('opts',opts)
print('args',args)