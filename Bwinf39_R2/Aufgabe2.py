

def read(example):
    file = open("spiesse" + example + ".txt", "r")
    wishes = []
    bowls = []
    fruits = []
    for i, line in enumerate(file.readlines()):
        if i == 0:
            pass
        elif i == 1:
            wishes = line.replace("\n", "").split(" ")
        elif i == 2:
            pass
        else:
            if i % 2 != 0:
                bowls.append(list(map(int, line.split(" "))))
            else:
                fruits.append(line.replace("\n", "").split(" "))

    return wishes, bowls, fruits


print(read("1"))
