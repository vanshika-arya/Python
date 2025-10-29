num=5
sum=0
def SON(num):
   if(num==1):
    return 1
   else:
    return num+SON(num-1)

print(SON(num))