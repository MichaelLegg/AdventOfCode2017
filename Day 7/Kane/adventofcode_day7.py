def part1():
    tree = {}
    with open("input.txt") as f:
        for line in f:
            line = line.rstrip('\n')
            line = line.replace(",", "")
            line = line.replace("-> ", "")
            line = line.replace("(", "")
            line = line.replace(")", "")
            line = map(str, line.split(" "))

            for i in range(1, len(line)):
                if len(line) > 2:
                    tree.setdefault(line[0], [])
                    tree[line[0]].append(line[i])
                else:
                    tree.update({line[0]:line[i]})

    for key in tree.keys():
        bool = False
        for v in tree.values():
            if type(v) is list:
                if key in v:
                    bool = True
                    break
        if (bool == False):
            root = key
            break

    return root

# def part2():
#     tree = {}
#     with open("input.txt") as f:
#         for line in f:
#             line = line.rstrip('\n')
#             line = line.replace(",", "")
#             line = line.replace("-> ", "")
#             line = line.replace("(", "")
#             line = line.replace(")", "")
#             line = map(str, line.split(" "))
#
#             for i in range(1, len(line)):
#                 if len(line) > 2:
#                     tree.setdefault(line[0], [])
#                     tree[line[0]].append(line[i])
#                 else:
#                     tree.update({line[0]: line[i]})
#
#     for v in tree.values():
#         if type(v) is list:
#             weightTotal = int(v[0])
#             for i in range(1, len(v)):
#                 if (type(tree[v[i]]) is not list):
#                     weightTotal += int(tree[v[i]])
#                 else:
#                     bool == False
#                     while(bool == False):
#                         for k in range(1, len(tree[v[i]])):
#                             weightTotal += int(tree[v[i]][0])
#                             # weightTotal += int(tree[v[i]][k])
#
#             print v, weightTotal

def traverse(tree, key):
    if type(tree[key]) is list:
        return (traverse(tree, key) + int(tree[key]))
    else:
        return key

def part2():
    tree = {}
    with open("input.txt") as f:
        for line in f:
            line = line.rstrip('\n')
            line = line.replace(",", "")
            line = line.replace("-> ", "")
            line = line.replace("(", "")
            line = line.replace(")", "")
            line = map(str, line.split(" "))

            for i in range(1, len(line)):
                if len(line) > 2:
                    tree.setdefault(line[0], [])
                    tree[line[0]].append(line[i])
                else:
                    tree.update({line[0]: line[i]})

    root = part1()
    print tree[root]

    traverse(tree, root)

# part1()
part2()