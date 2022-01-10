area = []
result = 0

while True:
    try:
        line = [x for x in input()]
    except:
        break
    
    area.append(line)

w = len(area[0])
h = len(area)

moved = True
step = 0
while moved:
    moved = False
    new = [
        ["." for _ in range(w)]
        for _ in range(h)
    ]

    for j in range(h):
        for i in range(w):
            c = area[j][i]
            if c == ">" and area[j][(i+1)%w] == ".":
                new[j][(i+1)%w] = ">"
                moved = True
            elif c == ">":
                new[j][i] = ">"

    for j in range(h):
        for i in range(w):
            c = area[j][i]
            if c == "v" and area[(j+1)%h][i] in [".",">"] and new[(j+1)%h][i] == ".":
                new[(j+1)%h][i] = "v"
                moved = True
            elif c == "v":
                new[j][i] = "v"

    area = new
    step += 1

    print(step)

print("final result is: ", step)