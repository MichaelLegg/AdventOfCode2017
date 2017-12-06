def maze_p1():
    ints = []
    with open('input.txt') as f:
        for i in f:
            ints.append(int(i.rstrip('\n')))

    exit = True
    idx = 0
    last = len(ints) - 1
    count = 0

    while(exit):
        if(idx >= 0 and idx <= last):
            if(ints[idx] > 0):
                temp = ints[idx]
                ints[idx] += 1
                idx += temp
                count += 1
            elif(ints[idx] < 0):
                temp = ints[idx]
                ints[idx] += 1
                idx += temp
                count += 1
            else:
                ints[idx] += 1
                count += 1
        else:
            exit = False

    print count

def maze_p2():
    ints = []
    with open('input.txt') as f:
        for i in f:
            ints.append(int(i.rstrip('\n')))

    exit = True
    idx = 0
    last = len(ints) - 1
    count = 0

    while(exit):
        if(idx >= 0 and idx <= last):
            if(ints[idx] > 0):
                if(ints[idx] >= 3):
                    temp = ints[idx]
                    ints[idx] -= 1
                    idx += temp
                    count += 1
                else:
                    temp = ints[idx]
                    ints[idx] += 1
                    idx += temp
                    count += 1
            elif(ints[idx] < 0):
                temp = ints[idx]
                ints[idx] += 1
                idx += temp
                count += 1
            else:
                ints[idx] += 1
                count += 1
        else:
            exit = False

    print count

# maze_p1()
maze_p2()