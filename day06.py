from functools import lru_cache
result = 0
data = list(map(int, input().split(",")))

@lru_cache(maxsize=None)
def number(d):
    days, c = d
    if days <= 0:
        return 1
    
    sol = 0
    if c > 0:
        sol += number((days-c, 0))

    if c == 0:
        sol += number((days-1, 6)) + number((days-1, 8))
    
    return sol

for x in data:
    result += number((256, x))


print(result)