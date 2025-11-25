n=int(input())
for i in range(n):
    num=int(input())
    rev=0
    while num>0:
        temp=num%10
        rev=(rev*10)+temp
        print(rev,end=" ")
        num//10
    print()