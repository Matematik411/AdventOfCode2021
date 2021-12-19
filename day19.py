from itertools import count, permutations
scanners = []
result = 0
#32 scanners
for _ in range(32):
    input()
    this_one = []
    while True:
        try:
            line = list(map(int, input().split(",")))
        except:
            break
        
        this_one.append(line)
    this_one.sort()
    scanners.append(this_one)

absolute_loc = scanners[0]

def compare(i, j):
    orig_1 = scanners[i]
    vect_1 = set()
    for k in range(len(orig_1)):
        for l in range(k+1, len(orig_1)):
            a = orig_1[k]
            b = orig_1[l]
            vect_1.add((a[0]-b[0], a[1]-b[1], a[2]-b[2]))

    for (x, y, z) in permutations(range(3)):
        for x_f in [1, -1]:
            for y_f in [1, -1]:
                # coordinate system must still be positively oriented!
                if (x, y, z) in {(0, 1, 2), (1, 2, 0), (2, 0, 1)}:
                    z_f = x_f*y_f
                else:
                    z_f = -x_f*y_f

                orig_2 = [
                    [x_f*scanners[j][k][x], y_f*scanners[j][k][y], z_f*scanners[j][k][z]]
                    for k in range(len(scanners[j]))
                ]
                orig_2.sort()
                # print(orig_2)
                vect_2 = set()
                for k in range(len(orig_2)):
                    for l in range(k+1, len(orig_2)):
                        a = orig_2[k]
                        b = orig_2[l]
                        vect_2.add((a[0]-b[0], a[1]-b[1], a[2]-b[2]))
                
                inters = vect_1.intersection(vect_2)
                if len(inters) >= 12*11/2:
                    return orig_2

    return False

def move(i, other):
    pos_1 = scanners[i]
    pos_2 = other

    vect_1 = {}
    for k in range(len(pos_1)):
        for l in range(k+1, len(pos_1)):
            a = pos_1[k]
            b = pos_1[l]
            vect_1[(a[0]-b[0], a[1]-b[1], a[2]-b[2])] = k

    center = False
    for k in range(len(pos_2)):
        if center:
            break
        for l in range(k+1, len(pos_2)):
            a = pos_2[k]
            b = pos_2[l]
            v = (a[0]-b[0], a[1]-b[1], a[2]-b[2])
            if v in vect_1:
                k_1 = vect_1[v]

                #moving vector
                center = (
                    pos_1[k_1][0] - pos_2[k][0],
                    pos_1[k_1][1] - pos_2[k][1],
                    pos_1[k_1][2] - pos_2[k][2]
                )
                break
    
    new_2 = []
    for (a, b, c) in pos_2:
        new_2.append([
            a + center[0],
            b + center[1],
            c + center[2]
        ])
    
    return new_2, center

found = {0}
centers = {0: (0, 0, 0)}
beacons = {tuple(x) for x in scanners[0]}
to_check = [0]

# print(scanners)
counter = 0
while len(found) < 32:
    print(to_check)
    current = to_check.pop()
    for j in range(32):
        if j == current or j in found:
            continue
        s = compare(current, j)
        if s:
            final, loc = move(current, s)
            scanners[j] = final
            found.add(j)
            beacons.update({tuple(x) for x in final})
            to_check.append(j)

            loc = (
                loc[0],
                loc[1],
                loc[2]
            )

            centers[j] = loc


max_dist = 0
for i in range(32):
    for j in range(i+1, 32):
        a = centers[i]
        b = centers[j]

        dist = sum([abs(a[k]-b[k]) for k in range(3)])
        if dist > max_dist:
            max_dist = dist



print(centers)
print("part one: ", len(beacons))
print("part two: ", max_dist)
