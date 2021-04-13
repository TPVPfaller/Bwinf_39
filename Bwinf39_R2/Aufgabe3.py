from collections import defaultdict

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


# wenn die Anzahl der Verkürzungen > die Anzahl an Verlängerungen ==> Verschieben
def solve():
    locations = [0, round(circumference/3), round((circumference/3) * 2)]
    print(circumference, locations)
    cancel = 0
    while not cancel:
        old_dist = get_dist(locations)
        old_locations = locations.copy()
        print("old_dist", old_dist)

        for i in range(len(old_locations)):
            print("1:    ", locations)
            if (locations[i] + 1) == circumference:
                locations[i] = 0
            else:
                locations[i] += 1

            print("1: ", locations)
            dist = get_dist(locations)
            print(dist)
            count = 0
            sum1 = 0
            sum2 = 0
            for d in dist.keys():
                sum1 += dist[d]
                sum2 += old_dist[d]
                if dist[d] < old_dist[d]:
                    count += 1
                elif dist[d] > old_dist[d]:
                    print(d)
                    count -= 1
            print(sum1, sum2)
            print("count1", count, dist)
            if count <= 0:
                print("2:     ", locations)
                if (locations[i] - 2) < 0:
                    locations[i] = circumference + (locations[i] - 2)
                else:
                    locations[i] -= 2
                dist = get_dist(locations)
                count = 0
                sum1 = 0
                sum2 = 0
                print("2: ", locations)
                for d in dist.keys():
                    sum1 += dist[d]
                    sum2 += old_dist[d]
                    if dist[d] < old_dist[d]:
                        count += 1
                    elif dist[d] > old_dist[d]:
                        print(d)
                        count -= 1
                print(sum1, sum2)
                print("count2", count, dist)
                if count <= 0:
                    print(count)
                    if (locations[i] + 1) == circumference:
                        locations[i] = 0
                    else:
                        locations[i] += 1
                    continue
            print(dist, locations)
            old_dist = get_dist(locations)
        print(old_locations, locations)
        if old_locations == locations:
            return locations

    print("No stable position possible.")
    return []


circumference, amount, addresses = read(5)
res = solve()
print(res)