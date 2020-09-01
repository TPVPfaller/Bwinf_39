from collections import defaultdict

def read(example):
    file = open("raetsel" + example + ".txt", "r")
    words = ""
    spaces = ""
    for line, val in enumerate(file.readlines()):
        print(val)
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
    print(list2)

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
    print(list1)

    return list1, list2


def solve(spaces, words):
    graph = defaultdict(list)
    count_rest = 0
    res = [""]*len(spaces)
    rest = list()
    i = 0
    word_list = []
    for l, pos, c, a in spaces:
        if c == "":
            if len(words[l]) == 1:
                res[i] = words[l][0]
            else:
                rest.append((l, i-count_rest))
                count_rest += 1
        else:
            w = ""
            count = 0
            for word in words[l]:
                if word[pos] == c:
                    if count == 0:
                        w = word
                    else:
                        word_list.append(word)
                        graph[word].append(i)
                        graph[i].append(word)
                    count += 1
            if count == 1:
                res[i] = w
            else:
                word_list.append(w)
                graph[w].append(i)
                graph[i].append(w)
        i += 1
    print(graph)
    print(words)
    print(word_list)
    while word_list:

        for word in word_list:
            if len(graph[word]) == 1:
                print(word)
                print(graph[word])
                res[graph[word][0]] = word
                x = graph[word][0]
                for s in graph[graph[word][0]]:
                    print(graph[s])
                    graph[s].remove(x)
                word_list.remove(word)
    print(words)
    print(rest)
    for l, i in rest:
        print(words[l][0])
        res[i] = words[l][0]

    return res


print('Geben Sie die Nummer eines Beispiels ein:')
example = input()
spaces, words = read(example)
res = solve(spaces, words)
print(res)