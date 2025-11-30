t = int(input())
for i in range(t):
    n, s = map(int, input().split())
    if s > n*(n+1)//2:
        print(-1)
        continue
    total = 0
    i = 0  
    for i in range(1, n+1):
        total += i
        if total >= s:
            break
    d = total - s  
    ans = []
    for x in range(1, i+1):
        if x == d:
            continue
        ans.append(x)
    ans.reverse()
    print(*ans)


