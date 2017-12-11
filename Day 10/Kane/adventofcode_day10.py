def parts1and2():
    input = "test.txt"

    with open(input) as f:
        for line in f:
            line.rstrip('\n')
            lengths = map(int, line.split(","))

    ints = []
    for i in range(5):
        ints.append(i)

    skip = 0
    idx = 0
    last = len(ints) - 1

    for j in lengths:
        print idx, j
        if j != 1:
            if idx + j <= last:
                seqRange = range(ints[idx], ints[j])
                reverse = list(reversed(seqRange))
                tempidx = idx
                for k in reverse:
                    ints[tempidx] = k
                    tempidx += 1
            else:
                temp = []
                tempIdxs = []
                tempidx = idx
                tempj = j
                while(tempidx <= last):
                    temp.append(ints[tempidx])
                    tempIdxs.append(tempidx)
                    tempidx += 1
                    tempj -= 1

                tempidx = 0
                while(tempj != 0):
                    temp.append(ints[tempidx])
                    tempIdxs.append(tempidx)
                    tempidx += 1
                    tempj -= 1

                reverse = list(reversed(temp))

                for idx2, p in enumerate(range(len(reverse))):
                    ints[tempIdxs[idx2]] = reverse[p]

        if idx + j <= last:
            idx += j
        else:
            idx = j

        skip += 1
        print ints

    print ints[0] * ints[1]

parts1and2()