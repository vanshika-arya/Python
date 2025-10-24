
N = int(input())
cycles = [
    [0, 0, 0, 0],
    [1, 1, 1, 1], 
    [2, 4, 8, 6], 
    [3, 9, 7, 1], 
    [4, 6, 4, 6], 
    [5, 5, 5, 5], 
    [6, 6, 6, 6], 
    [7, 9, 3, 1],
    [8, 4, 2, 6], 
    [9, 1, 9, 1]  
]
for i in range(N):
    
    a, b = map(int, input().split())
    if b == 0:
        print(1)
        continue
    last_digit_a = a % 10
    cycle_index = b % 4
    
    if cycle_index == 0:
        cycle_index = 4
    list_index = cycle_index - 1
    result = cycles[last_digit_a][list_index]
    
    print(result)