def parts1and2():
    input = "input.txt"

    with open(input) as f:
        for line in f:
            lengths = map(int, line.split(","))

    ints = []
    for i in range(256):
        ints.append(i)

    skip = 0
    idx = 0
    last = len(ints) - 1

    for i in lengths:
        if i != 1:
            if i + skip <= last:
                seqRange = range(ints[idx + skip], ints[i])
                reverse = list(reversed(seqRange))
                for i in reverse:
                    ints[idx] = i
                    idx += 1
            else:
                temp = []
                tempIdxs = []
                while(idx <= last):
                    temp.append(ints[idx])
                    tempIdxs.append(idx)
                    idx += 1
                    i -= 1

                idx = 0
                while(i != 0):
                    temp.append(ints[idx])
                    tempIdxs.append(idx)
                    idx += 1
                    i -= 1

                idx -= 1

                reverse = list(reversed(temp))

                for idx2, j in enumerate(range(len(reverse))):
                    ints[tempIdxs[idx2]] = reverse[j]

        skip += 1


    print ints[0] * ints[1]

parts1and2()