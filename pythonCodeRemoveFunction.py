list=[33,1,6,5,5,5,4,3,4,5,33,1,1]
list.sort()
print(list)
for x in list:
    y = list.count(x)
    if y>1:
        list.remove(x)
print(list)
