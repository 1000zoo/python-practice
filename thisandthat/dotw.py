def main():
    year = int(input("year : "))
    month = int(input("month : "))
    day = int(input("day : "))

    dayOfTheWeek = ["SUN", "MON", "TUE", "WED", "THR", "FRI", "SAT"]


    y = year_rest(year)
    m = month_rest(month, yun(year))
    d = day_rest(day)

    print(dayOfTheWeek[(y + m + d) % 7])


def yun(year):
    if year % 100 != 0 and year % 4 == 0 or year % 400 == 0:
        return True
    else:
        return False

def year_rest(year):
    y = max(year % 400 - 1, 0)
    yr = ((y // 100) * 5 + (y % 100) + ((y % 100) // 4)) % 7
    return yr

def month_rest(month, yun = False):
    if month == 1:
        return 0
    max_day = [3, 0, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3]
    if yun:
        max_day[1] = 1
    
    ret = 0
    for i in range(month - 1):
        ret += max_day[i]    

    return ret % 7

def day_rest(day):
    return day % 7

if __name__ == "__main__":
    main()