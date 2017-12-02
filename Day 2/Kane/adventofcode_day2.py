def checksums():
    sums = []

    with open('input.txt') as f:
        for line in f:
            line = map(int, line.split("\t"))
            line.sort()
            smallest = line[0]
            largest = line[len(line) - 1]
            diff = largest - smallest
            sums.append(diff)

    print sum(sums)

def modulo():
    sums = []

    with open('input.txt') as f:
        for line in f:
            line = map(int, line.split("\t"))
            last = len(line) - 1
            for idx, i in enumerate(line):
                length = len(line) - idx
                count = 1
                while(count <= length):
                    if(idx != last):
                        if(i > line[idx+1]):
                            if (i % line[idx + 1] == 0):
                                sums.append(i / line[idx+1])
                                break
                            else:
                                count = count + 1
                                idx = idx + 1
                        else:
                            if (line[idx + 1] % i == 0):
                                sums.append(line[idx + 1] / i)
                                break
                            else:
                                count = count + 1
                                idx = idx + 1
                    else:
                        break
    print sum(sums)

# checksums()
modulo()