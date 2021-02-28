

def read(example):
    file = open("eisbuden" + str(example) + ".txt", "r")

    line = file.readline()
    circumference, amount = tuple(map(int, line.split(" ")))
    line = file.readline()
    adresses = []
    for adress in line.split(" "):
        adresses.append(int(adress))
    return circumference, amount, adresses


def check_result():
    pass

print(read(1))
