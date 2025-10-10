a=100
b=30
c=20
if a>b:
    if a>c:
        print("a is greater")
    else:
        if b>c:
            print("b is greater")
        else:
            print("c is greater")
else:
    if b>c:
        print("b is greater")
    else:
        if a>c:
            print("a is greater")
        else:
            print("c is greater")