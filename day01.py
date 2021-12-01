data = []
prev = [0, 0, 0, 0]
inc = 0
while True:
    try:
        line = int(input())
    except:
        break
    prev = prev[1:] + [line]
    if prev[0] == 0:
        pass
    else:
        if sum(prev[1:]) > sum(prev[:-1]):
            inc += 1
            print(prev)




print(inc)