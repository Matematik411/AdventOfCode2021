data_ox = []
data_CO2 = []
all = 0
ones = [0 for _ in range(12)]
while True:
    try:
        line = input()
    except:
        break

    data_CO2.append(line)
    data_ox.append(line)


def most_common(l, i):
    all = len(l)
    ones = 0

    for x in l:
        if x[i] == "1":
            ones += 1
    
    return "1" if (2*ones >= all) else "0"

#oxygen
j = 0
while len(data_ox) > 1:
    pop = most_common(data_ox, j)
    data_ox = [x for x in data_ox if x[j] == pop]
    j += 1
#co2
j = 0
while len(data_CO2) > 1:
    pop = most_common(data_CO2, j)
    data_CO2 = [x for x in data_CO2 if x[j] != pop]
    j += 1

print(data_CO2, data_ox)
print(int(data_CO2[0], 2) * int(data_ox[0], 2))


    
# from part one
# gamma = ""
# epsilon = ""
# for x in ones:
#     if 2*x >= all:
#         gamma += "1"
#         epsilon += "0"
#     else:
#         gamma += "0"
#         epsilon += "1"

# gamma = int(gamma, 2)
# epsilon = int(epsilon, 2)
# print(gamma * epsilon)


