pair = {"(": ")", "[": "]", "{": "}", "<":">"}

points = {")":3, "]": 57, "}": 1197, ">": 25137}
def corruption(s):
    types = r")]}>"
    stack = []

    for x in s:
        if x in r"([{<":
            stack.append(x)
        else:
            c = pair[stack.pop()]
            if x != c:
                return points[x]
    return -1

points2 = {")":1, "]": 2, "}": 3, ">": 4}
def autocomplete(s):
    types = r")]}>"
    stack = []

    for x in s:
        if x in r"([{<":
            stack.append(x)
        else:
            stack.pop()
        
    here = 0
    while len(stack) > 0:
        c = pair[stack.pop()]
        here *= 5
        here += points2[c]
    return here

result = 0
result2 = []
while True:
    try:
        line = input()
    except:
        break

    x = corruption(line)
    if x > 0:
        result += x
    else:
        result2.append(autocomplete(line))

result2.sort()
print(result)
print(result2[len(result2)//2])