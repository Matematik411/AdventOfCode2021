def path(x0, y0):
    highest = 0
    x = 0
    y = 0
    dx = x0
    dy = y0

    while (x < 66) and (y > -226):
        x += dx
        y += dy

        if y > highest:
            highest = y
        
        dy -= 1
        if dx > 0:
            dx -= 1
    
        if (66 > x > 31) and (-226 < y < -176):
            return (x, y, highest)

    return 0


all_highest = 0
hits = 0
# border values (where hits exist):
# x_b = [8, 65]
# y_b = [-225, 224]
for x0 in range(8, 66):
    for y0 in range(-225, 225):
        sol = path(x0, y0)
        if sol:
            if sol[2] > all_highest:
                all_highest = sol[2]
            hits += 1

print(all_highest)
print(hits)

