from collections import defaultdict


def read(example):
    spaces = list()
    words = defaultdict(list)
    file = open("raetsel" + example + ".txt", "r")
    for line, val in enumerate(file.readlines()):
        if line:
            for word in val.split():
                words[len(word)].append(word)
        else:
            length, pos = 0, 0
            add, character = "", ""
            for c in val:
                if c == " ":
                    spaces.append((length, pos, character, add))
                    length, pos = 0, 0
                    add, character = "", ""
                elif c in {".", ",", "!", "?", ";"}:
                    add = c
                else:
                    if c == "_":
                        length += 1
                        if not character:
                            pos += 1
                    elif c != "\n":
                        character = c
                        length += 1
            spaces.append((length, pos, character, add))
    return spaces, words


def solve(spaces, words):
    graph = defaultdict(list)
    res = [""]*len(spaces)
    rest, pos_list = list(), list()
    for i, val in enumerate(spaces):
        l, pos, c, a = val
        if len(words[l]) == 1:
            res[i] = words[l][0]
        elif c == "":
            rest.append((l, i))
        else:
            pos_list.append(i)
            for word in words[l]:
                if word[pos] == c:
                    graph[word].append(i)
                    graph[i].append(word)
    print(graph)
    while pos_list:
        j = 0
        for _ in range(len(pos_list)):
            p = pos_list[j]
            if len(set(graph[p])) == 1:
                res[p] = graph[p][0]
                words[len(graph[p][0])].remove(graph[p][0])
                x = graph[p][0]
                for s in set(graph[graph[p][0]]):
                    graph[s].remove(x)
                pos_list.remove(p)
            else:
                j += 1
    for l, pos in rest:
        res[pos] = words[l][0]
    return res


print('Geben Sie die Nummer eines Beispiels ein:')
spaces, words = read(input())
res = solve(spaces, words)

for position, word in enumerate(res):
    print(word + spaces[position][3], end=" ")
