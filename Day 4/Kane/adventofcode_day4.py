def noDupes():
    count = 0
    with open('input.txt') as f:
        for line in f:
            line = map(str, line.split(" "))
            bool = False
            for i in range(len(line)):
                for j in range(i+1,len(line)):
                    line[i] = line[i].rstrip('\n')
                    line[j] = line[j].rstrip('\n')
                    if(line[i] == line[j]):
                        bool = True
                        break
            if(bool == False):
                count += 1

    print count

noDupes()