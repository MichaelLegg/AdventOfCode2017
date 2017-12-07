def parts1and2():
    tree = {}
    with open("input.txt") as f:
        for line in f:
            line = line.rstrip('\n')
            line = map(str, line.split(" "))

            line2 = []
            for i in line:
                line2.append(i)

            for i in range(len(line)):
                if (line[i] == '->'):
                    del line2[i]
                elif (',' in line[i]):
                    line2[i].replace(',', '')

            print line2

parts1and2()