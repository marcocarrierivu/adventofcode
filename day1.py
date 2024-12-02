
list1 = []
list2 = []

with open("input.txt") as file:
    for line in file:
        list = line.strip("\n").split("   ")
        list1.append(int(list[0]))
        list2.append(int(list[1]))
    file.close()

list1 = sorted(list1)
list2 = sorted(list2)

differenceList = []

for i in range(0,len(list1)):
    difference = abs(list1[i]-list2[i])
    differenceList.append(difference)

sum = sum(differenceList)

print(sum)
