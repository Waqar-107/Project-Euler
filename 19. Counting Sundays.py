def is_leap(year: int) -> bool:
    if year % 4 == 0:
        if year % 100 == 0:
            return False
        return True
    return False


def weekday(day: int, month: int, year: int) -> int:
    month_map = [-107, 11, 12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    W = day
    W += int(2.6 * month_map[month] - 0.2)
    W -= int(str(year)[:2]) * 2

    Y = int(str(year)[2:])
    if month == 1 or (month == 2 and is_leap(year)):
        Y -= 1

    W += Y
    W += Y // 4
    W += int(str(year)[2:]) // 4

    W %= 7

    if W < 0:
        W += 7
        W %= 7

    return W


ans = 0
for i in range(1901, 2001):
    for j in range(1, 13):
        if weekday(1, j, i) == 0:
            ans += 1

print(ans)

