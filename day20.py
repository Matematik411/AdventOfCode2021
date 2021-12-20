enhancing = input()
input()

image = []
while True:
    try:
        line = [x for x in input()]
    except:
        break
    
    image.append(line)

h = len(image)
w = len(image[0])

def expand(p, h, w, r):
    #background is white or dark, depending on the round
    bg = ("." if r%2 == 1 else "#")
    new = [[bg for _ in range(w+2)]]
    for j in range(h):
        line = [bg]
        for i in range(w):
            line.append(p[j][i])
        line.append(bg)
        new.append(line)
    new.append([bg for _ in range(w+2)])
    return (new, h+2, w+2)

def convert(s):
    binary = s.replace("#", "1").replace(".", "0")
    number = int(binary, 2)

    return enhancing[number]

image, h, w = expand(image, h, w, -1)
image, h, w = expand(image, h, w, -1)

for r in range(50):
    bg = ("." if r%2 ==1 else "#")
    new = [[bg  for _ in range(w)]]
    for jj in range(1, h-1):
        line = [bg]
        for ii in range(1, w-1):
            nr = [x for x in image[jj-1][ii-1:ii+2]]
            nr += [x for x in image[jj][ii-1:ii+2]]
            nr += [x for x in image[jj+1][ii-1:ii+2]]
            
            nr = "".join(nr)
            line.append(convert(nr))
        line.append(bg)
        new.append(line)
    new.append([bg for _ in range(w)])
    image, h, w = expand(new, h, w, r)

    if r == 1:
        print("part one:")
        print(sum([x.count("#") for x in image]))
    elif r == 49:
        print("part two:")
        print(sum([x.count("#") for x in image]))

