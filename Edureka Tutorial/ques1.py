def cWL(pL, vL):
    for i in range(len(pL)):
        if(pL[i] < vL[i]):
            print("LOSE")
            return
    print("WIN")
    return


def main():
    T = int(input())
    vL = []
    pL = []

# TODO: check range(T)
    for test in range(T):
        N = int(input())
        v = (list(map(int, input().split())))
        p = (list(map(int, input().split())))
        v.sort()
        p.sort()
        vL.append(v)
        pL.append(p)

    for test in range(T):
        cWL(pL[test], vL[test])


if __name__ == "__main__":
    main()
