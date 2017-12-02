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

checksums()
