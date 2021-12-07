data = list(map(int, input().split(",")))
result = 0

min = 355521 * 1000

for m in range(max(data)):
    result = 0
    for x in data:
        dist = abs(x-m)
        result += dist*(dist+1)// 2

    if result < min:
        min = result


print(min)