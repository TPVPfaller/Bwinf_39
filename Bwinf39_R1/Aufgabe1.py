from collections import defaultdict


def read(example):
    file = open("raetsel" + example + ".txt", "r")
    words = ""
    spaces = ""
    for line, val in enumerate(file.readlines()):
        if line == 1:
            words = val
            break
        else:
            spaces = val

    word = ""
    list2 = defaultdict(list)
    for x in words:
        if x == " ":
            list2[len(word)].append(word)
            word = ""
        else:
            word += x
    list2[len(word)].append(word)
    count = 0
    length = 0
    add = ""
    character = ""
    list1 = list(tuple())
    for x in spaces:
        if x == " ":
            list1.append((length, count, character, add))
            count = 0
            length = 0
            character = ""
            add = ""
        elif x == "_":
            length += 1
            if character == "":
                count += 1
        else:
            if character == "" and x not in {".", ",", "!", "?", "(", ")", ";", "-", "\n"}:
                character = x
                length += 1
            elif x != "\n":
                add += x
    list1.append((length, count, character, add))
    return list1, list2


def solve(spaces, words):
    graph = defaultdict(list)
    res = [""]*len(spaces)
    rest = list()
    i = 0
    pos_list = []
    for l, pos, c, a in spaces:
        if c == "":
            if len(words[l]) == 1:
                res[i] = words[l][0]#next(iter(words[l]))
            else:
                rest.append((l, i))
        else:
            pos_list.append(i)
            for word in words[l]:
                if word[pos] == c:
                    graph[word].append(i)
                    graph[i].append(word)
        i += 1
    while pos_list:
        j = 0
        for y in range(len(pos_list)):
            i = pos_list[j]
            if len(set(graph[i])) == 1:
                res[i] = graph[i][0]
                words[len(graph[i][0])].remove(graph[i][0])
                x = graph[i][0]
                for s in set(graph[graph[i][0]]):
                    graph[s].remove(x)
                pos_list.remove(i)
            else:
                j += 1
    for l, i in rest:
        res[i] = words[l][0]

    return res


print('Geben Sie die Nummer eines Beispiels ein:')
example = input()
spaces, words = read(example)
res = solve(spaces, words)
for i, word in enumerate(res):
    print(word + spaces[i][3], end=" ")