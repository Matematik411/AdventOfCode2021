#takes about 8 min

data = []
xi = []
yi = []
zi = []
while True:
    try:
        line = input()
    except:
        break

    print(line)
    aa, bb, cc, dd = line.split(r"..")
    a = int(aa.split("=")[1])
    b = int(bb.split(",")[0])
    c = int(bb.split("=")[1])
    d = int(cc.split(",")[0])
    e = int(cc.split("=")[1])
    f = int(dd)
    xi.append(a)
    xi.append(b+1)
    yi.append(c)
    yi.append(d+1)
    zi.append(e)
    zi.append(f+1)

    if line[1] == "n":
        data.append((1, a, b+1, c, d+1, e, f+1))
    else:
        data.append((0, a, b+1, c, d+1, e, f+1))


# part one
# grid = [
#     [
#         [
#             0 for _ in range(101)
#         ]
#         for _ in range(101)
#     ]
#     for _ in range(101)
# ]
# def switch(x):
#     print(x)
#     (x, a, b, c, d, e, f) = x
#     for k in range(e, f+1):
#         for j in range(c, d+1):
#             for i in range(a, b+1):
#                 grid[k+50][j+50][i+50] = x

grid = [
    [
        [
            0 for _ in range(len(xi)-1)
        ]
        for _ in range(len(yi)-1)
    ]
    for _ in range(len(zi)-1)
]
xi.sort()
yi.sort()
zi.sort()

def switch2(x):
    (x, a, b, c, d, e, f) = x
    a = xi.index(a)
    b = xi.index(b)
    c = yi.index(c)
    d = yi.index(d)
    e = zi.index(e)
    f = zi.index(f)
    for k in range(e, f):
        for j in range(c, d):
            for i in range(a, b):
                grid[k][j][i] = x


for (x, a, b, c, d, e, f) in data:
    # part one
    # if a >= -50 and c >= -50 and e >= -50 and b <= 50 and d <= 50 and f <= 50: 
    #     switch((x, a, b, c, d, e, f))
    print((x, a, b, c, d, e, f))
    switch2((x, a, b, c, d, e, f))

# part one
# lights = 0
# for k in range(101):
#     for j in range(101):
#         lights += sum(grid[k][j])
# sum([
#     sum([grid[k][j] for j in range(101)])
#     for k in range(101)
# ])
lights = 0
for k in range(len(zi)-1):
    for j in range(len(yi)-1):
        for i in range(len(xi)-1):
            if grid[k][j][i]:
                lights += (zi[k+1]-zi[k]) * (yi[j+1]-yi[j]) * (xi[i+1]-xi[i])

print(lights)