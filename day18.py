data = []
result = 0

while True:
    try:
        line = input()
    except:
        break
    
    data.append(line)

def reduce(a):
    change = True


    while change:
        # print(a)
        change = False

        #exploding
        brackets = 0
        i = 0
        for i in range(len(a)):
            x = a[i]
            if x == "[":
                brackets += 1
            elif x == "]":
                brackets -= 1
            
    	    
            if brackets == 5:
                start = i
                while a[i] != "]":
                    i += 1
                end = i
                l, r = map(int,a[start+1: end].split(","))
                a = a[:start] + "0" + a[end+1:]
                end = start + 2
                start -= 2

                number = ""
                reading = 0
                while start > 0:
                    if a[start] not in ",][":
                        number = a[start] + number
                        reading += 1
                    if a[start] in ",[]" and reading > 0:
                        break
                    start -= 1

                if start > 0:
                    here = int(number)
                    here += l
                    a = a[:start+1] + str(here) + a[start+reading+1:]

                number = ""
                reading = 0
                while end < len(a):
                    if a[end] not in ",][":
                        number = number + a[end]
                        reading += 1
                    if a[end] in ",[]" and reading > 0:
                        break
                    end += 1


                if reading > 0:
                    here = int(number)
                    here += r
                    a = a[:end-reading] + str(here) + a[end:]
                
                change = True
                break
            i += 1

        #split
        if change:
            continue
        prev = False
        m, n = 0, 0
        for i in range(len(a)):
            x = a[i]
            if x not in "[]," and not prev:
                prev = True
                m = int(x)
            elif x not in "[],":
                n = int(x)
                t = 10*m+n
                l = t//2
                r = t-l
                a = a[:i-1] + "[" + str(l) + "," + str(r) + "]" + a[i+1:]
                change = True
                break
            else:
                prev = False


    return a

def addition(a, b):
    s = "[" + a + "," + b + "]"
    s = reduce(s)

    return s

def magnitude(s):
    c = s.count(",")
    if c == 1:
        return 3*int(s[1]) + 2*int(s[3])
    
    i = 0
    level = 0
    for i in range(len(s)):
        x = s[i]
        if x == "[":
            level += 1
        elif x == "]":
            level -= 1
        elif x == "," and level == 1:
            l = s[1:i]
            r = s[i+1:-1]
            return 3*magnitude(l) + 2*magnitude(r)
    
    return 0


total = data[0]
for a in data[1:]:
    total = addition(total, a)

result = magnitude(total)

print("part a")
print(total)
print(result)

#part b
max_magn = 0
for i in range(len(data)):
    for j in range(len(data)):
        if i != j:
            l = data[i]
            r = data[j]
            suma = addition(l, r)
            magn = magnitude(suma)
            if magn > max_magn:
                max_magn = magn

print("part b")
print(max_magn)




