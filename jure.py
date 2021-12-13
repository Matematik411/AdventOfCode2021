path = "inputs\\test.txt"
file = open(path, "r")
allLines = file.readlines()

emptyList = []
for i in allLines:
    for k in i:
        if k != ',':
            number = int(k)
        emptyList.append(number)
print(emptyList)
        
counter = 0
for i in range(18):
    for j in emptyList:
        if j == 0:
            emptyList[counter] = 6
            emptyList.append(9)
        else:
            newNumber = j-1
            emptyList[counter] = newNumber
        counter += 1
    counter = 0
    print(emptyList)

print(len(emptyList))
