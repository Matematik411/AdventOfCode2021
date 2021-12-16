import numpy as np


data = ""
result = 0
while True:
    try:
        line = input()
    except:
        break
    
    for x in line:
        my_hexdata = x.lower()

        binary_string = "{0:08b}".format(int(my_hexdata, 16))[4:]
        data += binary_string

values = 0

def packet(s):
    total_ver = 0

    i = 0
    ver = int(s[i:i+3], 2)
    total_ver += ver
    i += 3
    typ = int(s[i:i+3], 2)
    i += 3

    if typ == 4:
        last = False
        nr = ""
        while not last:
            last = (s[i] == "0")
            i += 1
            value = s[i:i+4]
            nr += value
            i += 4 
        nr = int(nr, 2)
        return (ver, i, nr)

    id = s[i]
    i += 1
    inner_values = []

    if id == "0":
        length = int(s[i:i+15],2)
        i += 15

        partial = 0
        while partial < length:
            p_ver, p_len, p_val = packet(s[i:])
            partial += p_len
            i += p_len
            total_ver += p_ver
            inner_values.append(p_val)
    
    else:
        number = int(s[i:i+11], 2)
        i += 11

        for _ in range(number):
            p_ver, p_len, p_val = packet(s[i:])
            i += p_len
            total_ver += p_ver
            inner_values.append(p_val)
    
    if typ == 0:
        nr = sum(inner_values)
    elif typ == 1:
        nr = np.prod(inner_values)
    elif typ == 2:
        nr = min(inner_values)
    elif typ == 3:
        nr = max(inner_values)
    elif typ == 5:
        nr = 1 if inner_values[0] > inner_values[1] else 0
    elif typ == 6:
        nr = 1 if inner_values[0] < inner_values[1] else 0
    elif typ == 7:
        nr = 1 if inner_values[0] == inner_values[1] else 0



    return (total_ver, i, nr)


sol_a, total_len, sol_b = packet(data)
print("part a: ", sol_a)
print("part b: ", sol_b)



    

