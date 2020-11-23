from collections import defaultdict


def read(example):  # Einlesen und Abspeichern
    spaces = list()
    words = defaultdict(list)
    file = open("raetsel" + example + ".txt", "r")
    for line, val in enumerate(file.readlines()):
        if line:  # Wörter einlesen
            for word in val.split():
                words[len(word)].append(word)
        else:  # Lücken einlesen
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


def solve(spaces, words):  # Hauptalgorithmus
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
                # An der richtigen Position muss der richtige Buchstabe sein
                if word[pos] == c:
                    graph[word].append(i)
                    graph[i].append(word)
    # Nach und nach enfernen von Knoten (Lücken) mit nur einer Verbindung
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
    for l, pos in rest:  # restliche Wörter werden eingesetzt
        res[pos] = words[l][0]
    return res


print('Geben Sie die Nummer eines Beispiels ein:')
spaces, words = read(input())  # Eingabe
res = solve(spaces, words)

for position, word in enumerate(res):  # Ausgabe
    print(word + spaces[position][3], end=" ")
