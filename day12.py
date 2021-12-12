data = {"start":[], "end":[]}
while True:
    try:
        l, r = input().split("-")
    except:
        break

    if l not in data:
        data[l] = [r]
    else:
        data[l].append(r)
    
    if r not in data:
        data[r] = [l]
    else:
        data[r].append(l)
    

stack = []
stack.append([["start"],False])

paths = 0
while len(stack) > 0:
    p, a = stack.pop()
    c = p[-1]


    if c == "end":
        paths += 1
        continue

    for n in data[c]:
        if n == "start":
            continue

        if n.isupper():
            stack.append([p + [n],a])
        else:
            already = p.count(n)
            if already == 0:
                stack.append([p + [n],a])
            elif already == 1:
                if not a:
                    stack.append([p + [n],True])

print(paths)