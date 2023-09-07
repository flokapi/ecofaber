

import json
import random
import time


def loadJson(fileName):
    with open(fileName) as f:
        return json.loads(f.read())


def saveJson(data, fileName):
    with open(fileName, 'w') as f:
        json.dump(data, f, sort_keys=True, indent=4)


def timeStamp():
    return int(time.time()*10**6)


def randShuffle(n):
    r = list(range(n))
    random.shuffle(r)
    return r

def shuffle(l):
    l = list(l)
    random.shuffle(l)
    return l