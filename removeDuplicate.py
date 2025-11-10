lst = [2,3,2,4,3,5,5]
lst2=[]
lst3=[]
for x in lst:
    if x  not in lst2:
        lst2.append(x)
        lst3.append(x)
print(lst3)

