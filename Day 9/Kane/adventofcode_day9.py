def parts1and2():
    input = "input.txt"

    with open(input) as f:
        for line in f:
            line = map(str, line.split(","))

            print line

parts1and2()