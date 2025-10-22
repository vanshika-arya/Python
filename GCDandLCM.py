T = int(input())
for i in range(T):
    X, Y = map(int, input().split())
    
    orig_X = X
    orig_Y = Y
    a = X
    b = Y
    
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    GCD = a
    LCM = (orig_X * orig_Y) // GCD
    print(LCM, GCD)