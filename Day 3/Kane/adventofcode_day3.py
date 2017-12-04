import math

def find_item(list, item):
    return [[i, list[i].index(item)] for i in range(len(list)) if item in list[i]]

def spiral_grid():

    input = 312051
    grid_size = int(math.ceil(math.sqrt(input)))

    list = [[0 for _ in range(grid_size)] for _ in range(grid_size)]

    centre = int(math.floor(grid_size / 2))
    y = centre
    x = centre

    length = len(list) - 1

    count = 1

    for i in range(input):
        if(x == length and y != length):
            N = 0
            E = 0
            S = list[y + 1][x]
            W = list[y][x - 1]

        elif(x == length and y == 0):
            N = 0
            E = 0
            S = list[y + 1][x]
            W = 0

        elif(x != length and y == 0):
            N = 0
            E = list[y][x + 1]
            S = list[y + 1][x]
            W = 0

        elif (x == 0 and y == 0):
            N = 0
            E = list[y][x + 1]
            S = 0
            W = 0

        elif (x == 0 and y != 0):
            N = list[y - 1][x]
            E = list[y][x + 1]
            S = 0
            W = 0

        elif (x == 0 and y == length):
            N = list[y - 1][x]
            E = 0
            S = 0
            W = 0

        elif (x != 0 and y == length):
            N = list[y - 1][x]
            E = 0
            S = 0
            W = list[y][x - 1]

        else:
            N = list[y - 1][x]
            E = list[y][x + 1]
            S = list[y + 1][x]
            W = list[y][x - 1]

        if (N == 0 and E == 0 and S == 0 and W == 0):
            list[y][x] = count
            x = x + 1
        elif (N == 0 and E == 0 and S == 0 and W != 0):
            list[y][x] = count
            y = y - 1
        elif (N == 0 and E != 0 and S == 0 and W != 0):
            list[y][x] = count
            y = y - 1
        elif (N != 0 and E != 0 and S == 0 and W == 0):
            list[y][x] = count
            y = y + 1
        elif (N != 0 and E == 0 and S == 0 and W != 0):
            list[y][x] = count
            x = x + 1
        elif (N == 0 and E == 0 and S != 0 and W == 0):
            list[y][x] = count
            x = x - 1
        elif (N == 0 and E != 0 and S != 0 and W == 0):
            list[y][x] = count
            x = x - 1
        elif (N != 0 and E == 0 and S == 0 and W != 0):
            list[y][x] = count
            x = x + 1
        elif (N == 0 and E != 0 and S == 0 and W == 0):
            list[y][x] = count
            y = y + 1
        elif (N != 0 and E == 0 and S == 0 and W == 0):
            list[y][x] = count
            x = x + 1
        elif (N == 0 and E == 0 and S != 0 and W != 0):
            list[y][x] = count
            y = y - 1
        count = count + 1

    inputVal = find_item(list, input)
    start = [centre, centre]

    sums = []

    if(start[0] > inputVal[0][0]):
        sums.append(start[0] - inputVal[0][0])
    else:
        sums.append(inputVal[0][0] - start[0])

    if (start[1] > inputVal[0][1]):
        sums.append(start[1] - inputVal[0][1])
    else:
        sums.append(inputVal[0][1] - start[1])

    print sum(sums)

def spiral_grid_2():

    input = 312051
    grid_size = int(math.ceil(math.sqrt(input)))

    list = [[0 for _ in range(grid_size)] for _ in range(grid_size)]

    centre = int(math.floor(grid_size / 2))
    y = centre
    x = centre

    length = len(list) - 1

    count = 1

    for i in range(input):
        if(x == length and y != length):
            N = 0
            NE = 0
            E = 0
            SE = 0
            S = list[y + 1][x]
            SW = list[y + 1][x - 1]
            W = list[y][x - 1]
            NW = list[y - 1][x - 1]

        elif(x == length and y == 0):
            N = 0
            NE = 0
            E = 0
            SE = 0
            S = list[y + 1][x]
            SW = list[y + 1][x - 1]
            W = 0
            NW = 0

        elif(x != length and y == 0):
            N = 0
            NE = 0
            E = list[y][x + 1]
            SE = list[y + 1][x + 1]
            S = list[y + 1][x]
            SW = list[y + 1][x - 1]
            W = 0
            NW = 0

        elif (x == 0 and y == 0):
            N = 0
            NE = 0
            E = list[y][x + 1]
            SE = list[y + 1][x + 1]
            S = 0
            SW = 0
            W = 0
            NW = 0

        elif (x == 0 and y != length):
            N = list[y - 1][x]
            NE = list[y - 1][x + 1]
            E = list[y][x + 1]
            SE = list[y + 1][x + 1]
            S = 0
            SW = 0
            W = 0
            NW = 0

        elif (x == 0 and y == length):
            N = list[y - 1][x]
            NE = list[y - 1][x + 1]
            E = 0
            SE = 0
            S = 0
            SW = 0
            W = 0
            NW = 0

        elif (x == length and y == length):
            N = list[y - 1][x]
            NE = 0
            E = 0
            SE = 0
            S = 0
            SW = 0
            W = list[y][x - 1]
            NW = list[y - 1][x - 1]

        elif (x != 0 and y == length):
            N = list[y - 1][x]
            NE = list[y - 1][x + 1]
            E = 0
            SE = 0
            S = 0
            SW = 0
            W = list[y][x - 1]
            NW = list[y - 1][x - 1]

        else:
            N = list[y - 1][x]
            NE = list[y - 1][x + 1]
            E = list[y][x + 1]
            SE = list[y + 1][x + 1]
            S = list[y + 1][x]
            SW = list[y + 1][x - 1]
            W = list[y][x - 1]
            NW = list[y - 1][x - 1]

        if (N == 0 and E == 0 and S == 0 and W == 0):
            list[y][x] = count
            x = x + 1
        elif (N == 0 and E == 0 and S == 0 and W != 0):
            list[y][x] = N + NE + E + SE + S + SW + W + NW
            if(list[y][x] > input):
                exit
            else:
                y = y - 1
        elif (N == 0 and E != 0 and S == 0 and W != 0):
            list[y][x] = N + NE + E + SE + S + SW + W + NW
            if (list[y][x] > input):
                exit
            else:
                y = y - 1
        elif (N != 0 and E != 0 and S == 0 and W == 0):
            list[y][x] = N + NE + E + SE + S + SW + W + NW
            if (list[y][x] > input):
                exit
            else:
                y = y + 1
        elif (N != 0 and E == 0 and S == 0 and W != 0):
            list[y][x] = N + NE + E + SE + S + SW + W + NW
            if (list[y][x] > input):
                exit
            else:
                x = x + 1
        elif (N == 0 and E == 0 and S != 0 and W == 0):
            list[y][x] = N + NE + E + SE + S + SW + W + NW
            if (list[y][x] > input):
                exit
            else:
                x = x - 1
        elif (N == 0 and E != 0 and S != 0 and W == 0):
            list[y][x] = N + NE + E + SE + S + SW + W + NW
            if (list[y][x] > input):
                exit
            else:
                x = x - 1
        elif (N != 0 and E == 0 and S == 0 and W != 0):
            list[y][x] = N + NE + E + SE + S + SW + W + NW
            if (list[y][x] > input):
                exit
            else:
                x = x + 1
        elif (N == 0 and E != 0 and S == 0 and W == 0):
            list[y][x] = N + NE + E + SE + S + SW + W + NW
            if (list[y][x] > input):
                exit
            else:
                y = y + 1
        elif (N != 0 and E == 0 and S == 0 and W == 0):
            list[y][x] = N + NE + E + SE + S + SW + W + NW
            if (list[y][x] > input):
                exit
            else:
                x = x + 1
        elif (N == 0 and E == 0 and S != 0 and W != 0):
            list[y][x] = N + NE + E + SE + S + SW + W + NW
            if (list[y][x] > input):
                exit
            else:
                y = y - 1

    print list[y][x]

# spiral_grid()
spiral_grid_2()