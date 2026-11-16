t = int(input())

for _ in range(t):
    h, m = map(int, input().split(":"))

    if h == 0:
        h = 12
        am_pm = "AM"
    elif h < 12:
        am_pm = "AM"
    elif h == 12:
        am_pm = "PM"
    else:
        h -= 12
        am_pm = "PM"

    print(f"{h:02d}:{m:02d} {am_pm}")