n = int(input())
s = list(input())
for i in range(n):
    for j in range(0, n - i - 1):
        if s[j] > s[j + 1]:
            s[j], s[j + 1] = s[j + 1], s[j]
print("".join(s))



