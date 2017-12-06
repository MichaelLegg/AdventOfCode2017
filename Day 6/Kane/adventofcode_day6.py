def part1():
    with open('input.txt') as f:
        for line in f:
            line = map(int, line.split("\t"))

    states = []
    seen = False
    count = 0

    while(seen == False):
        largest = None
        idx = None

        for i in range(len(line)):
            for j in range(i + 1, len(line)):
                if line[i] > line[j]:
                    if line[i] > largest:
                        largest = line[i]
                        idx = i
                elif line[j] > line[i]:
                    if line[j] > largest:
                        largest = line[j]
                        idx = j

        last = len(line) - 1
        line[idx] = 0

        while(largest != 0):
            if(idx < last):
                idx += 1
                line[idx] += 1
                largest -= 1
            else:
                idx = 0
                line[idx] += 1
                largest -= 1

        if(line in states):
            seen = True
            count += 1
        else:
            temp = []
            for i in line:
                temp.append(i)
            states.append(temp)
            count += 1

    print count

part1()