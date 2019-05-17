def cMS(tLs):
    maxLists = []
    for tL in tLs:
        maxList = []
        for t in range(len(tL)):
            maxx = []
            ind = []
            sum = tL[t][0]
            maxx.append(tL[t][0])
            ind.append(tL[t][1])
            ind.append(tL[t][1]-1)
            ind.append(tL[t][1]+1)
            for t1 in tL[t:]:
                if t1[1] not in ind:
                    sum = sum + t1[0]
                    maxx.append(t1[0])
                    ind.append(t1[1])
                    ind.append(t1[1]-1)
                    ind.append(t1[1]+1)
            maxList.append([sum, maxx])
        maxList.sort(reverse=True)
        print(maxList)
        maxLists.append(maxList[0][1])
    return(maxLists)


def main():
    T = int(input())
    tLs = []

    for test in range(T):
        N = int(input())
        tickets = (list(map(int, input().split())))
        tic2 = []

        for i in range(len(tickets)):
            tic2.append([tickets[i], i])
        tic2.sort(reverse=True)
        tic3 = [x for x in tic2 if x[0] > 0]
        tLs.append(tic3)

    #TODO: optimize
    maxLists = cMS(tLs)
    for maxList in maxLists:
        maxList.reverse()
        print(''.join(str(i) for i in maxList))


if __name__ == "__main__":
    main()
