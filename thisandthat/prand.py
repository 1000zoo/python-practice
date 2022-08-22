import random

def prand(nmin, nmax, player=["지은", "윤우", "지우"]):
    r = list(range(nmin, nmax+1))

    random.shuffle(r)
    random.shuffle(player)
    pd = listtodict(player)
    names = list(pd.keys())

    for i, num in enumerate(r):
        pd[names[i%3]].append(num)

    for i in pd:
        pd[i].sort()

    print(pd)


def listtodict(lst):
    d = {}
    for l in lst:
        d[l] = []
    
    return d


def main():
    nmin = int(input("min number => "))
    nmax = int(input("max number => "))

    prand(nmin, nmax)

if __name__ == "__main__":
    main()
