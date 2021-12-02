loc = [0, 0]
dirs = {"forward": (1, 0), "up": (0, -1), "down": (0, 1)}
aim = 0
while True:
    try:
        line = input().split()
    except:
        break
    d , x = line[0], int(line[1])
    if d == "down":
        aim += x
    elif d == "up":
        aim -= x
    else:
        loc[0] += dirs[d][0] * x

        loc[1] += aim * x

print(loc[0] * loc[1])