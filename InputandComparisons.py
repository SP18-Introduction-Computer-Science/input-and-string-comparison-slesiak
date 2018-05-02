textfile = open("strings.txt", "r")

a = []
b = []

lineList = []
count = 0
for line in textfile :
    count +=1
    if count % 2 == 0:
        a.append(line)
    else :
        b.append(line)

print("The even lines are: ")
for element in a :
    print(element)
    
print("The odd lines are: ")
for element in b :
    print(element)
