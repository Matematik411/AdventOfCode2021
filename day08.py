data = []
result = 0
while True:
    try:
        line = input()
    except:
        break

    # #part one
    # count = False
    # for x in line:
    #     if count:
    #         if len(x) in [2, 3, 4, 7]:
    #             result += 1

    #     if x == "|":
    #         count = True
    data.append(line)

numbers = {0:{0, 1, 2, 4, 5, 6}, 1: {2, 5}, 2: {0, 2, 3, 4, 6}, 3: {0, 2, 3, 5, 6}, 4: {1, 2, 3, 5}, 5: {0, 1, 3, 5, 6}, 6: {0, 1, 3, 4, 5, 6}, 7: {0, 2, 5}, 8: {0, 1, 2, 3, 4, 5, 6}, 9: {0, 1, 2, 3, 5, 6}}

def solve(before, after):
    values = {}

    appe = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0}
    for x in before:
        for a in x:
            appe[a] += 1

    for (k, v) in appe.items():
        if v == 9:
            values[k] = 5
        if v == 6:
            values[k] = 1
        if v == 4:
            values[k] = 4

    for x in before:
        if len(x) == 2:

            for a in x:
                if a not in values:
                    values[a] = 2

    for x in before:
        if len(x) == 4:

            for a in x:
                if a not in values:
                    values[a] = 3
    
    for x in before:
        if len(x) == 3:

            for a in x:
                if a not in values:
                    values[a] = 0
    
    for a in appe:
        if a not in values:
            values[a] = 6

    output_number = ""
    for w in after:
        this = set()
        for a in w:
            this.add(values[a])
        for (k, v) in numbers.items():
            if this == v:
                output_number += str(k)

    return int(output_number)

for line in data:
    line = line.split()
    bef = line[:10]
    aft = line[-4:]
    result += solve(bef, aft)

print(result)