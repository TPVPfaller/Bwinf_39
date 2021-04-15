from functools import wraps
from collections import defaultdict
import tkinter as tk
import time


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
        root.geometry("1600x400+0+0")
        self.color_index = 0
        self.canvas = tk.Canvas(root, bg="white", height=110, width=1510)
        self.canvas.create_rectangle(10, 10, 1500, 100)
        self.canvas.pack()

    def add_rectangle(self, r):
        colors = ['CadetBlue4', 'turquoise1', 'salmon', 'red', 'green', 'blue', 'cyan', 'yellow', 'magenta', 'ivory4',
                  'VioletRed3', 'DarkOrange3', 'lawn green', 'chocolate2', 'purple2', 'coral1', 'firebrick3']
        self.canvas.create_rectangle(r[0]*1.5+10, r[1]+10, (r[0]+r[2])*1.5+10, (r[1]+r[3])*10, fill=colors[self.color_index], width=0)

        if self.color_index == len(colors)-1:
            self.color_index = 0
        else:
            self.color_index += 1

    def finish(self):
        tk.mainloop()


# this algorithm defines the upper bound
def greedy(queue):
    space = 0



    return space


# branch and bound
def solve(shops):
    res = []
    border = 0
    while shops[0][0] == 10:
        shop = shops.pop(0)
        res.append([border, 0, shop[1], shop[0]])
        border += shop[1]
    print(shops)

    skyline = [border] * 10
    print(skyline)
    queue = defaultdict(list)
    for s in shops:
        queue[s[2]].append(s)
    print(queue)
    upper_bound = greedy(queue)
    # create candidate solutions
    while queue:
        queue

    return res


shops = read(1)
shops.sort(reverse=True)    # decreasing order
print(shops)
result = solve(shops)
print(result)
draw = Draw()
for r in result:
    draw.add_rectangle(r)

draw.finish()
