import re
data = {}
result = 0
while True:
    try:
        line = input()
    except:
        break
        
    a, b, c, d = map(int, re.match(r"(\d*),(\d*) -> (\d*),(\d*)", line).groups())

    if a == c:
        if b > d:
            b, d = d, b
        for y in range(b, d+1):
            if (a, y) in data:
                data[(a, y)] += 1
            else:
                data[(a, y)] = 1
    elif b == d:
        if a > c:
            a, c = c, a
        for x in range(a, c+1):
            if (x, b) in data:
                data[(x, b)] += 1
            else:
                data[(x, b)] = 1

    elif abs(c-a) == abs(d-b):
        up = c-a
        r = d-b
        dir = r//abs(r)
        if up > 0:
            for i in range(up+1):
                p = (a+i, b+i*dir)
                if p in data:
                    data[p] += 1
    
                else:
                    data[p] = 1
        else:
            up = -up
            for i in range(up+1):
                p = (a-i, b+i*dir)
                if p in data:
                    data[p] += 1
                else:
                    data[p] = 1

result = 0
for k, v in data.items():
    if v > 1:
        result += 1

print(result)