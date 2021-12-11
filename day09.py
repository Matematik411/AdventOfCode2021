from queue import Queue
data = []
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

while True:
    try:
        line = [int(x) for x in input()]
    except:
        break

    data.append(line)



w = len(data[0])
h = len(data)
terrain = [[10 for _ in range(w+2)]]
terrain += [[10] + data[i] + [10] for i in range(h)]
terrain += [[10 for _ in range(w+2)]]
w += 2
h += 2



# poisce okolico - dodaja vse kar < 9
def basin(x, y):
    visited = set()
    stack = []
    stack.append((x, y))
    size_visited = 0

    while len(stack) > 0:
        (x, y) = stack.pop()

        if (x, y) in visited:
            continue

        visited.add((x, y))
        size_visited += 1

        for (dx, dy) in dirs:
            x_n = x + dx
            y_n = y + dy
            if terrain[y_n][x_n] < 9:
                stack.append((x_n, y_n))

    return size_visited

result_a = 0
basins = []
for i in range(1, w-1):
    for j in range(1, h-1):
        here = terrain[j][i]
        low = True
        for (dx, dy) in dirs:
            x_n = i + dx
            y_n = j + dy
            if terrain[y_n][x_n] <= here:
                low = False
        
        if low:
            result_a += 1 + here
            basins.append(basin(i, j))

basins.sort()
result_b = basins[-1] *basins[-2] * basins[-3]

print(result_a)
print(result_b)