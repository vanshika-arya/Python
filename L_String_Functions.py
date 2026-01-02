n, q = map(int, input().split())
s = list(input())

for _ in range(q):
    query = input().split()

    if query[0] == "pop_back":
        s.pop()

    elif query[0] == "front":
        print(s[0])

    elif query[0] == "back":
        print(s[-1])

    elif query[0] == "sort":
        l, r = int(query[1]), int(query[2])
        s[l:r+1] = sorted(s[l:r+1])

    elif query[0] == "reverse":
        l, r = int(query[1]), int(query[2])
        s[l:r+1] = list(reversed(s[l:r+1]))

    elif query[0] == "print":
        l, r = int(query[1]), int(query[2])
        print("".join(s[l:r+1]))

    elif query[0] == "push_back":
        s.append(query[1])