rules = {}
appearances = {}

original = input()
input()

while True:
    try:
        l, r = input().split(" -> ")
    except:
        break

    rules[l] = r
    appearances[l] = 0

for i in range(len(original)-1):
    a = original[i]
    b = original[i+1]
    appearances[a+b] += 1

def polymerization(d):
    new = {x: 0 for x in rules}
    singular = {x: 0 for x in rules.values()}

    for ((a, b), c) in rules.items():
        new[a+c] += d[a+b]
        new[c+b] += d[a+b] 
        singular[c] += d[a+b]
        singular[a] += d[a+b]
    #last letter of the word is a K (not not counted above)    
    singular["K"] += 1
    return new, singular

for i in range(40):
    (appearances, sing) = polymerization(appearances)



counts = [(v, k) for (k, v) in sing.items()]
counts.sort()


print(counts[-1][0] - counts[0][0])