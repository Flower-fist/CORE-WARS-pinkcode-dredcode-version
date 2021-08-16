##made by enrique
print('filename?:')
filename = input()
print('# of lines?:')
numOfLines = input()
list1 = []
print('opening file >:/n')
with open(filename, 'r') as f:
    for r in range(int(numOfLines)):
        temp = f.readline()
        print(temp)
        list1.append(temp)

print('printing complete >:')
print('extrcting data >:')
##turns data from file into LONG list of numbers.
list2 = []
for i in range(int(numOfLines)):
    temp = list1[i]
    temp2 = temp.split()
    
temp3 = []
for j in range(len(temp2)):
    temp3.append(int(temp2[j]))

temp2 = temp3

for k in range(len(temp2)):
    list2.append(temp2[k])

quit()
