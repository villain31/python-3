def checkWinLose(playersList, villainsList):
    for i in range(len(playersList)):
        if(playersList[i] < villainsList[i]):
            print("LOSE")
            return
    print("WIN")
    return


def main():
    # Number of Test Cases
    T = int(input())
    villainsList = []
    playersList = []

    for test in range(T):
        # Number of Villains and Players FIXME: 'N' Not Required
        N = int(input())
        # List of Villains Strengths
        villains = (list(map(int, input().split())))
        # List of Players Energy
        players = (list(map(int, input().split())))
        villains.sort()
        players.sort()
        villainsList.append(villains)
        playersList.append(players)

    for test in range(T):
        # Checking Win/Lose
        checkWinLose(playersList[test], villainsList[test])


if __name__ == "__main__":
    main()
