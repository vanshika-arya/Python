#frozen set are immutable hum values add ni kar sakte
s1= frozenset({1,2,3,4})
s2= frozenset({2,3,4,7,5}) 
# s1.add(8)
print(s1) #error

print(s1.union(s2))
print(s1.difference(s2))
print(s1.intersection(s2))
print(s1.symmetric_difference(s2))

lst =["name" , "vanshika" ,"nitin ","alshifa", "ashi","rohit"]
target='a'
for i in  lst:
    if target in lst:
        print(target)


   