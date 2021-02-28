from functools import wraps
from time import time

def read(example):
    file = open("spiesse" + example + ".txt", "r")
    amount = 0
    wishes = []
    fruits = set()
    skewer = []
    skewers = []
    for i, line in enumerate(file.readlines()):
        if i == 0:
            amount = int(line)
        elif i == 1:
            wishes = line.replace("\n", "").split(" ")
            for j in wishes:
                fruits.add(j)
        elif i == 2:
            pass
        else:
            if i % 2 != 0:
                skewer = (list(map(int, line.split(" "))))
            else:
                skewers.append([])
                skewers[-1].append(skewer)
                skewers[-1].append(line.replace("\n", "").split(" "))
                for j in line.replace("\n", "").split(" "):
                    fruits.add(j)
    # Erstellen eines Spiesses mit allen Früchten
    if len(fruits) == amount:
        skewers.append([[i for i in range(1, amount+1)], list(fruits)])
    return wishes, skewers


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        t0 = time()
        result = f(*args, **kw)
        t1 = time()
        print("Zeit: " + str(round((t1-t0)*1000, 5)) + "ms")
        return result
    return wrap


@timing
def solve(wishes, queue):
    solved_fruits = []
    positions = []
    last_queue = []
    while wishes not in solved_fruits:
        if last_queue == queue:
            break
        last_queue = queue.copy()
        for i in range(len(queue)):
            if len(queue[i][0]) == 1:
                if queue[i][1][0] in wishes:
                    positions.append(queue[i][0][0])
                    solved_fruits.append(queue[i][1][0])
                queue = remove_fruit(queue, queue[i][0][0], queue[i][1][0])
            for j in range(i+1, len(queue)):
                intersection = [list(set(queue[i][0]) & set(queue[j][0])), list(set(queue[i][1]) & set(queue[j][1]))]
                if len(intersection[0]) < len(queue[i][0]) + len(queue[j][0]) and len(intersection[0]) != 0:
                    if len(intersection[0]) == 1:
                        if intersection[1][0] in wishes:
                            positions.append(intersection[0][0])
                            solved_fruits.append(intersection[1][0])
                        queue = remove_fruit(queue, intersection[0][0], intersection[1][0])
                        del queue[i][0][queue[i]]
                    else:
                        for x in range(len(intersection[0])):
                            p, f = intersection[0][x], intersection[1][x]
                            del queue[i][0][queue[i][0].index(p)]
                            del queue[i][1][queue[i][1].index(f)]
                            del queue[j][0][queue[j][0].index(p)]
                            del queue[j][1][queue[j][1].index(f)]
                        queue.append(intersection)

    return solved_fruits, positions, queue



def remove_fruit(q, p, f):
    for i in range(len(q)):
        if p in q[i][0]:
            del q[i][0][q[i][0].index(p)]
        if f in q[i][1]:
            del q[i][1][q[i][1].index(f)]
    return q


#print("Geben Sie hier die Nummer des Beispiels ein (0-7):")

print("Geben Sie hier die Nummer des Beispiels ein (0-7):")

#wishes, skewers = read(input())
for i in range(0, 8):
    print("spiesse"+ str(i) + ".txt:")
    wishes, skewers = read(str(i))

    result = solve(wishes, skewers)
    solved_fruits, positions, queue = result
    for j in range(len(solved_fruits)):
        print('\033[96m' + solved_fruits[j] + '\033[0m' + " ist in der " + '\033[96m' + str(positions[j]) + '\033[0m' + ". Schüssel")
    print()
    if len(solved_fruits) < len(wishes):
        for q in queue:
            if len(q[0]) != 0:
                count = 1
                for e in q[1]:
                    if e in wishes:
                        count = 0
                        break
                if count:
                    continue
                print("Diese Obstsorte(n):             ", end="")
                for i, f in enumerate(q[1]):
                    if f in wishes:
                        print('\033[96m' + f + '\033[0m', end=" ")
                print()
                print("sind/ist in diesen Schüsseln:   ", end="")
                for i, p in enumerate(q[0]):
                    print('\033[96m' + str(p) + '\033[0m', end=" ")
                print("\n")
