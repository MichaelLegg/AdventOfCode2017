def grid():

    list = [[0 for _ in range(11)] for _ in range(11)]

    y = 5
    x = 5

    count = 1

    for i in range(121):
        if(x + 1 < 10 and y + 1 < 10):
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
        else:
            if (x == 0 and y != 0):
                list[y][x] = count
                x = x - 1

            elif (x == 10):
                list[y][x] = count
                y = y - 1

            elif (x == 0 and y != 10):
                list[y][x] = count
                y = y + 1

            elif (y == 10):
                list[y][x] = count
                x = x - 1
        count = count + 1

    for row in list:
        print row

grid()