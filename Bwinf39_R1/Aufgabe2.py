



def read(example):
    file = open("raetsel" + example + ".txt", "r")
    symbols = 0
    amount = 0
    pieces = []
    for line, val in enumerate(file.readlines()):
        if line == 0:
            symbols = val
        elif line == 1:
            amount = val
        else:
            if line % 2 == 0:

