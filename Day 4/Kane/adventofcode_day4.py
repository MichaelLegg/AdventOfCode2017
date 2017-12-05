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

def anagram():
    count = 0
    with open('input.txt') as f:
        for line in f:
            line = map(str, line.split(" "))
            bool = False
            for i in range(len(line)):
                for j in range(i + 1, len(line)):
                    line[i] = line[i].rstrip('\n')
                    line[j] = line[j].rstrip('\n')

                    wordi = []
                    wordj = []
                    for ch in line[i]:
                        wordi += ch

                    for ch in line[j]:
                        wordj += ch

                    wordi.sort()
                    wordj.sort()

                    isorted = ""
                    jsorted = ""

                    for ch in wordi:
                        isorted += ch

                    for ch in wordj:
                        jsorted += ch

                    if(isorted == jsorted):
                        bool = True
                        break
            if (bool == False):
                count += 1

    print count

# noDupes()
anagram()

