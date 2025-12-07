# n=int(input())
# a=list(map(int,input().split()))
# def check_even():
#     for i in a:
#         if i%2!=0:
#             return False
#         return True
# count=0
# if check_even():
#     for j in a:
#         j=j//2
#         count+=1

# if count!=0:
#     print(count)
# else:
#     print("0")

n = int(input())
a = list(map(int, input().split()))
count = 0
while True:
    for x in a:
        if x % 2 != 0:
            print(count)
            exit()
    for i in range(n):
        a[i] = a[i] // 2
    count += 1
