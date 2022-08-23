

def main():

    a = 1       # m/s
    b = 3       # m/s
    c = 5      # m/s
    x = 0.4       # m/s^2
    y = 0.4       # m/s^2
    l = 50      # m

    t1 = findT(x, c - a)
    t2 = findT(y, c - b)

    area1 = calTrap(a, c, t1)
    area2 = calTrap(b, c, t2)

    hsa = l - (area1 + area2)         # 최고속도 구간의 넓이
    t3 = hsa / c

    print(area1, hsa, area2)
    print(t1, t3, t2)
    print(t1 + t2 + t3)

def calTrap(a, b, x):
    return (a + b) * x * 0.5

def calRec(x, y):
    return x * y

def findT(acc, speed):
    return speed / acc

if __name__ == "__main__":
    main()