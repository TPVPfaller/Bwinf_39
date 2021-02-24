from collections import defaultdict
import time
from random import *

def read(example):
    file = open("spielstärken" + example + ".txt", "r")
    players = list()
    amount = 0
    for line, val in enumerate(file.readlines()):
        if line == 0:
            amount = val
        else:
            players.append(val)
        pass
    return amount, players

def solve(amount, players):
    # Liga


    # KO System

    # KO x5


    return res


print('Geben Sie die Nummer eines Beispiels ein:')
time1 = time.time()
example = input()
amount, players = read(example)
res = solve(amount, players)
print("Lösung:")

print('In ' + str(round((time.time() - time1), 5)) + ' Sekunden')
