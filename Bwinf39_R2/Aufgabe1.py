

def read(example):
    file = open("flohmarkt" + str(example) + ".txt", "r")
    amount = int(file.readline())
    shops = []
    for line in file.readlines():
        time1, time2, space = line.split(" ")
        width = space.rstrip("\n")
        space = int(width) * (int(time2)-int(time1))
        shops.append([space, int(width), int(time1) - 8, int(time2) - 8])
    return shops


def merge(queue):


    return queue


def solve(shops):
    res = []
    pos = 0
    while shops[0][3] - shops[0][2] == 10:
        shop = shops.pop(0)
        border[1] -= shop[1]
        res.append([pos, 0, shop[2], shop[3]])
        pos += shop[1]
    print(border)
    print(shops)
    queue = shops.copy()

    return res


shops = read(1)
border = [10, 1000]
shops.sort(reverse=True)
print(shops)
result = solve(shops)
print(result)