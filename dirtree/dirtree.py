import os
import sys
sys.setrecursionlimit(10000000)
basedir = 'c:/'
searchpf='1115-connection.xlsx'
result=[]
errors={}

def errorhandl(func):
    def wrapper(*args,**kwargs):
        try:
            func(*args,**kwargs)
        except (FileNotFoundError, PermissionError,UnicodeEncodeError):
            type, value, traceback = sys.exc_info()
            errors[args] = ('Error opening %s: %s' % (value, type))
            pass
    return wrapper

@errorhandl
def mainiter(sordir):
    tre = {}
    for subitem in os.listdir(sordir):
        fullpath = os.path.join(sordir, subitem)
        print("searching in %s" %subitem)
        if os.path.isdir(fullpath):
            tre[subitem] = {sordir: 'dir'}
            if searchpf == subitem:
                print('found')
                result.append(fullpath)
        if os.path.isfile(fullpath):
            tre[subitem] = {sordir: 'fil'}
            if searchpf == subitem:
                print('found')
                result.append(fullpath)
    for ki, it in tre.items():
        for k, i in it.items():
            if i == 'dir':
                nloop=os.path.join(sordir, ki)
                mainiter(nloop)

mainiter(basedir)
print(result)
print(errors)