from queue import PriorityQueue
data = []
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

while True:
    try:
        line = [int(x) for x in input()]
    except:
        break

    data.append(line)

W = len(data[0])
H = len(data)

w = 5*len(data[0])+2
h = 5*len(data)+2
terrain = [[0 for _ in range(w)] for _ in range(h)]
terrain[0] = [10000 for _ in range(w)]
terrain[-1] = [10000 for _ in range(w)]
for j in range(1, h-1):
    terrain[j][0] = 10000
    terrain[j][-1] = 10000
    for i in range(1, w-1):
        quadr_j = (j-1) // H
        quadr_i = (i-1) // W
        pos_j = (j-1) % H
        pos_i = (i-1) % W
        

        v = (data[pos_j][pos_i] + quadr_j + quadr_i)
        if v < 10:
            terrain[j][i] = v
        else:
            terrain[j][i] = v-9


# Dijkstra
q = PriorityQueue()
q.put((0, 1, 1))
visited = set()
part_one = False
while not q.empty():
    r, x, y = q.get()

    if (x, y) == (W, H) and not part_one:
        print("part one: ", r)
        part_one = True

    if (x, y) == (w-2,h-2):
        print("part two: ", r)
        break

    if (x, y) in visited:
        continue

    visited.add((x, y))

    for (dx, dy) in dirs:
        x_n = x + dx
        y_n = y + dy
        if (x_n, y_n) not in visited:
            q.put((r + terrain[y_n][x_n], x_n,y_n))

