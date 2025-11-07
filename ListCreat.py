lst =["apple" , "grapes" ,"banana" , "papaya", "kiwi"]
lst2=[3,7,5,4,9]
print(lst[0])
print(lst[len(lst)-1])
print(lst)
# print(lst[0])
# print(lst[1])
# print(lst[2])
# print(lst[3])
# print(lst[4])
for i in lst:
    print("I like " +i)

lst.append("mango")
print(lst)

lst.insert(2,"watermelon")
print(lst)

del(lst[2])
print(lst)

print(lst.pop())
print(lst)

lstA =[1,2]
lstB =[3,4]
lstA.append(lstB)
print(lstA)

if "mango" in lst:
    print("yes")
else:
    print("no")

sum=0
for i in lst2:
    sum+=i
print(sum)
print(sum/len(lst2))


min=lst2[0]
maxi = lst2[0]
for i in lst2:
    if min> i :
        min=i
    if maxi<i:
        maxi=i
print(min)
print(maxi)

lst2.append(7)
lst2.append(4)
lst2.append(7)
lst2.append(7)
print(lst2)
print(lst2.count(7))

lst5=['x' ,'y' ,'z' ,'y']
# for i in lst:
print(lst5.index('y'))

lst.reverse()
print(lst)
#slicing
print(lst[:]) #print all numbers

#print from index 2 to index 3
print(lst[2:4])

    

    
        

