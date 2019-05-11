'''
Lista: [1,2,7,1,9,2]

El numero mas grande, sin utilizar max, sort.

'''

L = [1,2,7,1,9,2]
L.sort()


mylist = [1,2,7,1,9,2]
print(mylist)
n = len(mylist)
for i in range(n):
    for j in range(1, n-i):
        if mylist[j-1] > mylist[j]:
             (mylist[j-1], mylist[j]) = (mylist[j], mylist[j-1])
print(mylist)






data_list = [1,2,7,1,9,2]
new_list = []

while data_list:
    minimum = data_list[0]  # arbitrary number in list
    for x in data_list:
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    data_list.remove(minimum)

print (new_list)

pass
