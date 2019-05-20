import random


def findMaxSumList(tickets):

    for i, e in enumerate(tickets):
        tickets[i] = [tickets[i], i]

    tickets.sort(key=lambda x: x[0])
    tickets = list(filter(lambda x: x[0] > 0, tickets))

    # TODO: Logic

    return tickets


def main():
    ticketsList = []

    # T = int(input())
    T = random.randint(1, 10)

    for t in range(T):

        # N = int(input())
        N = random.randint(1, 10000)

        # tickets = (list(map(int, input().split())))
        tickets = []
        for i in range(0, N):
            x = random.randint(-1000, 1000)
            tickets.append(x)

        ticketsList.append(findMaxSumList(tickets))
    print(ticketsList)
