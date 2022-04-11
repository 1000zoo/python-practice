"""
    주사위 a,b,c 를 던졌을 때
    (a-b)(b-c)(c-a) = 0 인 경우의수는?
"""

count = 0
for a in range(1, 7):
    for b in range(1, 7):
        for c in range(1, 7):
            if (a-b)*(b-c)*(c-a) == 0:
                print("a:", a, "b:", b, "c:", c)
                count += 1

print(count)