

class chip():
    def __init__(self, color):
        self.color = color

    def print_color(self):
        print(self.color, end="\t")

def init(n, color):
    ret = []
    for i in range(n):
            ret.append(chip(color))
    return ret

def shuf(left, right):
    ret = []
    for l, r in zip(left, right):
        ret.append(l)
        ret.append(r)
    
    return ret

def sideprint(left, right):
    for l, r in zip(left, right):
        l.print_color()
        r.print_color()
        print()

def check(now, origin):
    for n, o in zip(now, origin):
        if (n.color != o.color):
            return False
    return True

def main():
    carr = []
    n = 0
    while True:
        n += 1
        cnt = 0
        leftside = init(n, "white")
        rightside = init(n, "blue")
        orl = leftside
        orr = rightside
        sideprint(leftside, rightside)
        while True:

            print("="*20)
            carr = shuf(leftside, rightside)
            leftside = carr[:len(carr)//2]
            rightside = carr[len(carr)//2:]
            sideprint(leftside, rightside)
            cnt += 1

            if check(leftside, orl) and check(rightside, orr):
                break

        print(n, ":", cnt)
        input()
    
if __name__ == "__main__":
    main()

