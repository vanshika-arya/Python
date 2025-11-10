#zeros in last
lst2 = [0,1,2,3,0,0,5,3]
for i in lst2:
    if i==0:
        lst2.append(0)
        lst2.remove(i)
print(lst2)