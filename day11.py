grid = []
flashes = 0
while True:
    try:
        line = [int(x) for x in input()]
    except:
        break

    grid.append(line)

w = len(grid[0])
h = len(grid)

r = 1
while True:
    flashes = 0
    flashed = [[False for _ in range(w)] for _ in range(h)]
    to_flash = []
    for j in range(h):
        for i in range(w):
            grid[j][i] += 1
            if grid[j][i] > 9:
                to_flash.append((i, j))

    dirs_x = [1, 1, 0, -1, -1, -1, 0, 1]
    dirs_y = [0, 1, 1, 1, 0, -1, -1, -1]

    while len(to_flash) > 0:
        (x, y) = to_flash.pop()
        flashed[y][x] = True

        for k in range(8):
            x_n = x + dirs_x[k]
            y_n = y + dirs_y[k]

            if 0 <= x_n < w and 0 <= y_n < h:
                grid[y_n][x_n] += 1
                if grid[y_n][x_n] == 10:
                    to_flash.append((x_n, y_n))

    for j in range(h):
        for i in range(w):
            if flashed[j][i]:
                grid[j][i] = 0
                flashes += 1
    
    if flashes == w*h:
        print("round", r)
        break
    r += 1

