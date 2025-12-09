n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort() 
for i in range(1, m+1):
    count=0
    for j in a:
        if j==i:
            count += 1
        elif j > i:
            break
    print(count)
