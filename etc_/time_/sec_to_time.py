t = 4100

day = round(t / (3600 * 24))
t = t % (3600 * 24)
hour = round(t / 3600)
t = t % 3600
min = round(t / 60)
t = t % 60
sec = round(t)

print(day, hour, min, sec)