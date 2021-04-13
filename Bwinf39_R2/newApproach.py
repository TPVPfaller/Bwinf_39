from collections import defaultdict
import numpy as np
# Erweiterung: n Eisdielen


def read(example):
    file = open("eisbuden" + str(example) + ".txt", "r")

    line = file.readline()
    circumference, amount = tuple(map(int, line.split(" ")))
    line = file.readline()
    adresses = []
    for address in line.split(" "):
        adresses.append(int(address))
    file.close()
    return circumference, amount, adresses


def get_dist(locations):
    distances = defaultdict()
    for a in addresses:
        z1 = a
        z2 = a
        dist = 0
        while z1 not in locations and z2 not in locations:
            z1 += 1
            z2 -= 1
            dist += 1
            if z2 < 0:
                z2 = circumference-1
            if z1 > circumference-1:
                z1 = 0
        distances[a] = dist
    return distances


def solve(locations, margin):
    initial = get_dist(locations)





    return locations


circumference, amount, addresses = read(3)
res = solve([0, circumference/3, circumference/3*2], 1)
print(res)