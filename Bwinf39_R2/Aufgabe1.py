from functools import wraps
from collections import defaultdict
import tkinter as tk
from time import time
from operator import itemgetter


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        t0 = time()
        result = f(*args, **kw)
        t1 = time()
        print("Durchlaufzeit: " + str(round((t1-t0)*1000, 5)) + "ms")
        print()
        return result
    return wrap


def read(example):
    file = open("flohmarkt" + str(example) + ".txt", "r")
    amount = int(file.readline())
    shops = []
    for line in file.readlines():
        time1, time2, space = line.split(" ")
        width = space.rstrip("\n")
        diff = (int(time2)-int(time1))
        shops.append([diff, int(width), int(time1) - 8, int(time2) - 8])
    return shops


class Draw:

    def __init__(self):
        root = tk.Tk()
        root.title("Aufgabe1")
        root.geometry("1620x300+0+0")
        self.color_index = 0
        self.canvas = tk.Canvas(root, bg="white", height=300, width=1620)
        self.canvas.create_rectangle(60, 10, 1560, 210)
        self.canvas.pack()

    def add_rectangle(self, r):
        colors = ['CadetBlue4', 'sandy brown', 'red', 'green', 'blue', 'cyan', 'yellow', 'magenta', 'ivory4',
                  'grey76', 'DarkOrange4', 'dark khaki', 'lawn green', 'purple2', 'coral1', 'firebrick4', 'plum1']
        print(colors[self.color_index] + ":", str(r[0])+"m, "+str(r[2])+"m, "+str(r[1]+8)+"-"+str(r[3]+r[1]+8)+" Uhr")
        self.canvas.create_rectangle(r[0]*1.5+60, r[1]*20+10, (r[0]+r[2])*1.5+60, (r[1]+r[3])*20+10, fill=colors[self.color_index], width=0)

        if self.color_index == len(colors)-1:
            self.color_index = 0
        else:
            self.color_index += 1

    def finish(self, space):
        self.canvas.create_text(120, 260, fill="black", font="Times 15 bold", text="Einnahmen: "+str(space)+"€")
        for i in range(11):
            self.canvas.create_text(40, 9 + i*20, fill="black", font="Times 10", text=str(i+8) + " Uhr")

        for i in range(11):
            self.canvas.create_text(i*150+63, 220, fill="black", font="Times 10", text=str(i*100) + " m")
        for i in range(1, 10):
            self.canvas.create_line(60, 10+(20*i), 1560, 10+(20*i))
        tk.mainloop()


# fills the gap two the lowest nearest tower
def close_gap(position, skyline, gap, points):
    if position[1] == 0:
        lowest = skyline[gap]
    else:
        if position[1] == 9:
            skyline[9] = skyline[8]
            points[9] = [skyline[8], 9]
            return
        if skyline[position[1]] == skyline[position[1]-1]:
            skyline[position[1]] = skyline[gap]
            points[position[1]] = [skyline[gap], position[1]]
            return
        lowest = min(skyline[position[1] - 1], skyline[gap])
    for i in range(position[1], gap):
        skyline[i] = lowest
        points[i] = [skyline[i], i]
    return


# returns a rectangle and its position
def feasible_rectangle(points, queue, skyline, feasible_position=0):
    if feasible_position == 10:
        return 0, 0
    position = 0
    p = points.copy()
    p.sort()    # getting Bottom left most points
    for e in p:
        if len(queue[e[1]]) != 0:
            if e[1] >= feasible_position:
                position = e
                break
    if position == 0:
        return 0, 0
    count = 0
    for r in queue[position[1]]:
        gap = 0
        for e in range(r[3] + 1, r[4]):
            if skyline[e] > position[0]:
                gap = e  # right side of gap
                break
        if not gap:
            if position[0] + r[2] > 1000:
                count += 1
                continue
            queue[position[1]].remove(r)
            return position, r
    # if not all rectangles exceed the limit 1000
    if count != len(queue[position[1]]):
        close_gap(position, skyline, gap, points)
    return feasible_rectangle(points, queue, skyline, feasible_position+1)

def greedy(rect_dict, skyline, res):
    space = skyline[0]*10
    points = [[skyline[0], i] for i in range(10)]

    while rect_dict:
        pos, rectangle = feasible_rectangle(points, rect_dict, skyline)
        if rectangle == 0:
            return space
        for i in range(rectangle[3], rectangle[4]):
            skyline[i] = (pos[0] + rectangle[2])
            points[i] = [skyline[i], i]
        space += rectangle[0]
        res.append([pos[0], pos[1], rectangle[2], rectangle[1]])
    return space


# branch and bound
@timing
def solve(shops):
    res = []
    border = 0
    while shops[0][0] == 10:
        shop = shops.pop(0)
        res.append([border, 0, shop[1], shop[0]])
        border += shop[1]
    skyline = [border] * 10
    rect_dict = defaultdict(list)
    for s in shops:
        s.insert(0, s[0]*s[1])
        rect_dict[s[3]].append(s)
    space = greedy(rect_dict, skyline, res)
    return res, space, rect_dict


print("Geben Sie hier die Nummer des Beispiels ein (1-7):")
choice = input()
shops = read(choice)
shops.sort(reverse=True)    # decreasing order
draw = Draw()

res, space, rect_dict = solve(shops)
count = 1
print("Nicht angenommene Voranmeldungen: ")
for k in rect_dict.values():
    if k:
        count = 0
        for r in k:
            print(str(r[2])+"m, "+str(r[3]+8)+"-"+str(r[4]+8)+" Uhr")
if count:
    print("/")
print()
print("Angenommene Voranmeldungen: ")
for r in res:
    draw.add_rectangle(r)
print()

print("Einnahmen:", str(space)+"€")
draw.finish(space)
