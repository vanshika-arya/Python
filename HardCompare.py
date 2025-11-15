import math
a,b,c,d=map(int,input().split())
left= b*math.log(a)
right= d*math.log(c)

if(left>right):
    print("YES")
else:
    print("NO")
# e=1
# f=1
# for i in range(1,b+1):
#     e=e*a
# for j in range(1,d+1):
#     f=f*c
# if e>f:
#     print("YES")
# else:
#     print("NO")
