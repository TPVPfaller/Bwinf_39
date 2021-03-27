import random
# Erweiterung: n Eisdielen


def read(example):
    file = open("eisbuden" + str(example) + ".txt", "r")

    line = file.readline()
    circumference, amount = tuple(map(int, line.split(" ")))
    line = file.readline()
    adresses = []
    for address in line.split(" "):
        adresses.append(int(address))
    return circumference, amount, adresses


def get_dist(locations, addresses, circumference):
    distances = []
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
        distances.append(dist)
    return distances


def check_result(locations, addresses, circumference):
    initial = get_dist(locations, addresses, circumference)
    #print(initial)
    for i in range(circumference):
        print(i)
        for j in range(i+1, circumference):
            for k in range(j+1, circumference):
                cur_dist = get_dist([i, j, k], addresses, circumference)
                #print(cur_dist)
                count = 0
                for x in range(len(addresses)):
                    if cur_dist[x] < initial[x]:
                        count += 1
                if count > len(addresses)/2:
                    print(cur_dist, count)
                    res = [i, j, k]
                    res.sort()
                    return res
    return locations


circumference, amount, addresses = read(5)
print(circumference, amount, addresses)
pos = [83, 128, 231]
pos = check_result(pos, addresses, circumference)
print(pos)
