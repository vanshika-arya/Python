a=10
b=50
for i in range(a,b):
    if i>1:
        is_Divisibl=False
        for index in range(2,i):
            if i%index==0:
                is_Divisibl=True
        if not is_Divisibl:
            print(i)