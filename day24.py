# TO SE NE IZVEDE !!!!!!!!
# implementation of the ALU

ALU_ex = {"x": 0, "y": 0, "z": 0, "w": 0}
instr = []

while True:
    try:
        line = input().split()
    except:
        break
    
    instr.append(line)


def program(ALU, number):
    pos = 0

    for case in instr:
        if case[0] == "inp":
            ALU[case[1]] = int(number[pos])
            pos += 1

        elif case[0] == "add":
            is_nr = False
            b = case[2]
            try:
                b = int(b)
                is_nr = True
            except:
                pass

            if is_nr:
                ALU[case[1]] = ALU[case[1]] + b
            else:
                ALU[case[1]] = ALU[case[1]] + ALU[b]
                
        elif case[0] == "mul":
            is_nr = False
            b = case[2]
            try:
                b = int(b)
                is_nr = True
            except:
                pass

            if is_nr:
                ALU[case[1]] = ALU[case[1]] * b
            else:
                ALU[case[1]] = ALU[case[1]] * ALU[b]

        elif case[0] == "div":
            is_nr = False
            b = case[2]
            try:
                b = int(b)
                is_nr = True
            except:
                b = ALU[b]
            
            if b == 0:
                print("Crash for number", number)
                return -1

            ALU[case[1]] = int( ALU[case[1]] / b )
            

        elif case[0] == "mod":
            is_nr = False
            b = case[2]
            try:
                b = int(b)
                is_nr = True
            except:
                b = ALU[b]
            
            if ALU[case[1]] < 0 or b <= 0:
                print("Crash for number", number)
                return -1

            ALU[case[1]] = ALU[case[1]] % b
            
        elif case[0] == "eql":
            is_nr = False
            b = case[2]
            try:
                b = int(b)
                is_nr = True
            except:
                b = ALU[b]

            ALU[case[1]] = 1 if ALU[case[1]] == b else 0
    
    return ALU

# print(program(ALU_ex, "7"))


sols = [92171126131911, 99394899891971]
for i in sols:
    j = str(i)
    if j.count("0") > 0:
        continue

    ALU_ex = {"x": 0, "y": 0, "z": 0, "w": 0}
    sol = program(ALU_ex, j)
    if sol != -1 and sol["z"] == 0:
        print(i, sol)
