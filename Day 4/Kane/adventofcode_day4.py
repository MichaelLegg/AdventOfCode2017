def noDupes():
    with open('input.txt') as f:
        for line in f:
            line = map(int, line.split("\t"))

noDupes()