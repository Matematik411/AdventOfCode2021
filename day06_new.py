data = list(map(int, input().split(",")))

rem = [0 for _ in range(9)]
for x in data:
    rem[x] += 1

for _ in range(256):
    rem[7] += rem[0]
    rem = rem[1:] + rem[:1]
print(sum(rem))