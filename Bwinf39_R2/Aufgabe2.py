from functools import wraps
from time import time


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        t0 = time()
        result = f(*args, **kw)
        t1 = time()
        print("Durchlaufzeit: " + str(round((t1-t0)*1000000, 5)) + "ms")
        return result
    return wrap


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
    # Erstellen eines Spiesses mit allen Früchten (Wenn diese bekannt sind) aus allen Schüsseln
    if len(fruits) == amount:
        skewers.append([[i for i in range(1, amount + 1)], list(fruits)])
    return wishes, skewers


def solve(skewers):
    solved_fruits = []
    positions = []
    last_skewers = []
    # Wird beendet wenn die Obstsorten bestimmt wurden oder es keine weiteren Kombinationsmöglichkeiten gibt

    count = 0
    while wishes not in solved_fruits:
        if last_skewers == skewers:
            break
        last_skewers = skewers.copy()
        count += 1
        for i in range(len(skewers)):
            # Spiesse mit nur einer Schüssel sind genau zuordenbar
            if len(skewers[i][0]) == 1:
                if skewers[i][1][0] in wishes:
                    positions.append(skewers[i][0][0])
                    solved_fruits.append(skewers[i][1][0])
                skewers = remove_fruit(skewers, skewers[i][0][0], skewers[i][1][0])
                continue
            for j in range(i+1, len(skewers)):

                # Schnittmenge aus den Obstsorten und den dazugehörigen Schüsseln
                intersection = [list(set(skewers[i][0]) & set(skewers[j][0])), list(set(skewers[i][1]) & set(skewers[j][1]))]
                if len(intersection[0]) < len(skewers[i][0]) + len(skewers[j][0]) and len(intersection[0]) != 0:
                    if len(intersection[0]) == 1:   # Schüssel genau zuordenbar
                        if intersection[1][0] in wishes:
                            positions.append(intersection[0][0])
                            solved_fruits.append(intersection[1][0])
                        skewers = remove_fruit(skewers, intersection[0][0], intersection[1][0])
                    else:   # Schnittmenge wird als neuer Spieß dem Queue hinzugefügt und aus den beiden anderen gelöscht
                        for x in range(len(intersection[0])):
                            p, f = intersection[0][x], intersection[1][x]
                            skewers[i][0].remove(p)
                            skewers[i][1].remove(f)
                            skewers[j][0].remove(p)
                            skewers[j][1].remove(f)
                        skewers.append(intersection)

    return solved_fruits, positions, skewers


# Entfernt eine Obstsorte aus dem Queue
def remove_fruit(q, p, f):
    for i in range(len(q)):
        if p in q[i][0]:
            del q[i][0][q[i][0].index(p)]
        if f in q[i][1]:
            del q[i][1][q[i][1].index(f)]
    return q


def print_output():
    for j in range(len(solved_fruits)):
        print('\033[96m' + solved_fruits[j] + '\033[0m' + " ==> " + '\033[96m' + str(
            positions[j]) + '\033[0m')
    print()
    if len(solved_fruits) < len(wishes):
        for q in remaining:
            if len(q[0]) != 0:
                count = 1
                for e in q[1]:
                    if e in wishes:
                        count = 0
                        break
                if count:
                    continue
                print("Diese Obstsorte(n):             ", end="")
                for f in q[1]:
                    if f in wishes:
                        print('\033[96m' + f + '\033[0m', end=" ")
                print()
                print("sind/ist in diesen Schüsseln:   ", end="")
                for p in q[0]:
                    print('\033[96m' + str(p) + '\033[0m', end=" ")
                print("\n")


print("Geben Sie hier die Nummer eines Beispiels ein (0-7 oder 'a' um alle auszugeben):")
choice = input()
if choice == 'a':
    for i in range(0, 8):
        print("spiesse"+ str(i) + ".txt:")
        wishes, skewers = read(str(i))
        solved_fruits, positions, remaining = solve(skewers)
        print_output()
else:
    wishes, skewers = read(choice)
    solved_fruits, positions, remaining = solve(skewers)
    print_output()