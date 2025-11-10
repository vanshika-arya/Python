# lst = [3, 4, 5, 1, 4, 2]

# for i in range(len(lst)):
#     for j in range(i + 1, len(lst)):
#         s = lst[i] + lst[j]
#         print(lst[i], "+", lst[j], "=", s, " (indices:", i, ",", j, ")")

a=[2,7,11,15]
target =18
ans = None
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i]+a[j] ==target:
            ans =[i,j]
            break
    if ans: break
print(ans)
            