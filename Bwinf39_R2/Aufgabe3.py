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
    return circumference, amount, adresses


def get_dist(locations, addresses, circumference):
    distances = []
    for a in addresses:
        z1 = a
        z2 = a
        dist1 = 0
        dist2 = 0
        while z1 not in locations and z2 not in locations:
            z1 += 1
            z2 -= 1
            dist1 += 1
            dist2 += 1
            if z2 < 0:
                z2 = circumference-1
            if z1 > circumference-1:
                z1 = 0
        distances.append(min(dist1, dist2))
    return distances


def check_result(locations, addresses, circumference):
    initial = get_dist(locations, addresses, circumference)
    print(initial)
    for i in range(circumference):
        for j in range(circumference):
            for k in range(circumference):
                if i != j != k:
                    cur_dist = get_dist([i, j, k], addresses, circumference)
                    count = 0
                    for x in range(len(initial)):
                        if cur_dist[x] < initial[x]:
                            count += 1
                    if count > len(addresses)/2:
                        print(cur_dist, (i, j, k), count)

    return True


def dist_to_addresses(addresses, circumference):
    dist_to_addresses = [0] * circumference
    for p in range(circumference):
        for a in addresses:
            dist_to_addresses[p] -= min(abs(p-a), abs(p-(20+a)))

    #a = np.array(dist_to_addresses)
    #ind = np.argpartition(a, -3)[-3:]
    print(dist_to_addresses)
    ind = dist_to_addresses.index(max(dist_to_addresses))
    return ind


def dist_to_addresses2(addressses, circumference, spots):
    dist_to_addresses = [0] * circumference
    for p in range(circumference):
        for a in addresses:
            dist_to_addresses[p] -= min(abs(p-a), abs(p-(20+a)))

    #a = np.array(dist_to_addresses)
    #ind = np.argpartition(a, -3)[-3:]
    print(dist_to_addresses)
    ind = dist_to_addresses.index(max(dist_to_addresses))
    return ind


circumference, amount, addresses = read(6)
print(circumference, amount, addresses)
first_location = dist_to_addresses(addresses, circumference)
print(first_location)
