def parts1and2():

    reg = {}
    regHighest = {}


    input = "input.txt"

    with open(input) as f:
        for line in f:
            line = line.rstrip("\n")
            line = map(str, line.split(" "))

            reg.update({line[0]: 0})
            regHighest.update({line[0]: 0})

    with open(input) as f:
        for line in f:
            line = line.rstrip("\n")
            line = map(str, line.split(" "))

            if line[5] == '>':
                if reg[line[4]] > int(line[6]):
                    if line[1] == 'inc':
                        reg[line[0]] += int(line[2])
                    else:
                        reg[line[0]] -= int(line[2])
            elif line[5] == '<':
                if reg[line[4]] < int(line[6]):
                    if line[1] == 'inc':
                        reg[line[0]] += int(line[2])
                    else:
                        reg[line[0]] -= int(line[2])
            elif line[5] == '>=':
                if reg[line[4]] >= int(line[6]):
                    if line[1] == 'inc':
                        reg[line[0]] += int(line[2])
                    else:
                        reg[line[0]] -= int(line[2])
            elif line[5] == '==':
                if reg[line[4]] == int(line[6]):
                    if line[1] == 'inc':
                        reg[line[0]] += int(line[2])
                    else:
                        reg[line[0]] -= int(line[2])
            elif line[5] == '<=':
                if reg[line[4]] <= int(line[6]):
                    if line[1] == 'inc':
                        reg[line[0]] += int(line[2])
                    else:
                        reg[line[0]] -= int(line[2])
            elif line[5] == '!=':
                if reg[line[4]] != int(line[6]):
                    if line[1] == 'inc':
                        reg[line[0]] += int(line[2])
                    else:
                        reg[line[0]] -= int(line[2])

            if reg[line[0]] > regHighest[line[0]]:
                regHighest[line[0]] = reg[line[0]]

    print reg[max(reg, key=reg.get)]
    print regHighest[max(reg, key=regHighest.get)]

parts1and2()