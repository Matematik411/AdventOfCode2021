import re
data = set()
while True:
    try:
        x, y = map(int, input().split(","))
    except:
        break

    data.add((x, y))

nr = [655, 447, 327, 223, 163, 111, 81, 55, 40, 27, 13, 6]
dirs = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0]

for i in range(12):
    pos, n = re.match(r"fold along (.)=(\d*)", input()).groups()
    n = int(n)
    new = set()
    for (x, y) in data:
        if pos == "x":
            if x > n:
                x -= 2*(x-n)
        else:
            if y > n:
                y -= 2*(y-n)
        new.add((x, y))
    data = new
    if i == 0:
        print("part a:", len(data), "\n")

x_m = min([x[0] for x in data])
y_m = min([x[1] for x in data])
x_M = max([x[0] for x in data])
y_M = max([x[1] for x in data])

grid = [["." for _ in range(x_M-x_m+1)] for _ in range(y_M-y_m+1)]

for (x, y) in data:
    grid[y-y_m][x-x_m] = "#"

pict = ""
for l in grid:
    pict += "".join(l) + "\n"
print(pict)
