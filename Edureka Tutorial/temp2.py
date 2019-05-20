def getMaxSumSubList(ticketsList):
    maxSumList = []
    for tickets in ticketsList:
        num1 = 0
        num2 = 0
        num1List = []
        num2List = []
        tempList = []
        for ticket in tickets:
            temp = num1
            num1 = max(num1, num2 + ticket)
            num2 = temp
            tempList = num1List
            if(temp != num1):
                num1List = num2List + [ticket]
            num2List = tempList
        maxSumList.append(num1)
        num1List.reverse()
        print(''.join(str(i) for i in num1List))
    

def main():
    T = int(input())
    ticketsList = []
    for t in range(T):
        N = int(input())
        ticket = []
        ticket = (list(map(int, input().split())))
        ticketsList.append(ticket)

    getMaxSumSubList(ticketsList)

main()


