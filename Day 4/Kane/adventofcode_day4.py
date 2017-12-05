def noDupes():
    count = 0
    with open('test.txt') as f:
        for line in f:
            line = map(str, line.split(" "))
            print line
            bool = False
            for i in range(len(line)):
                for j in range(i+1,len(line)):
                    print i,j
                    if(line[i] == line[j]):
                        print line[i], line[j]
                        print count
                        bool = True
                        break
                if(bool == True):
                    # print line
                    break
            if(bool == False):
                count += 1

    print count

noDupes()