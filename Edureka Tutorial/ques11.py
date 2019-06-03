def getMaxSum(listBoxes):
    for boxes in listBoxes:
        listIncNum = []
        maxSum = 0
        for box in boxes:
            flag = True
            tempListIncNum = []
            for i in range(len(box)):
                if(box[i] in listIncNum):
                    flag = False
                    break
                else:
                    if(box[i] not in tempListIncNum):
                        tempListIncNum.append(box[i])
            if(flag):
                listIncNum = listIncNum + tempListIncNum
                maxSum += int(box)
        print(maxSum)


def main():
    # Number of Test Cases
    T = int(input())
    listBoxes = []

    for test in range(T):
        # Number of Boxes TODO: 'N' Not Required
        N = int(input())
        # List of Box Numbers
        box = (list(map(int, input().split())))
        box.sort(reverse=True)
        box_1 = [str(item) for item in box]
        # box_1 = box
        listBoxes.append(box_1)

    # Checking Max Sum
    getMaxSum(listBoxes)


if __name__ == "__main__":
    main()
