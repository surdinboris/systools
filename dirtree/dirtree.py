import os
import sys
sys.setrecursionlimit(10000000)

basedir = 'c:/gitrep/'


def dirrec(sordir):
    tre = {}
    try:
        for subitem in os.listdir(sordir):

                if os.path.isdir(os.path.join(sordir,subitem)):
                    tre[subitem]={sordir:'dir'}

                if os.path.isfile(os.path.join(sordir,subitem)):
                    tre[subitem] = {sordir: 'fil'}
    except FileNotFoundError:
        pass

    for ki, it in tre.items():
        for k, i in it.items():
            if i == 'dir':
                dirrec(ki)
    print(tre)
dirrec(basedir)


