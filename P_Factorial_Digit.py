import math

N = int(input())

digits = 0
for i in range(1, N + 1):
    digits += math.log10(i)

print(f"Number of digits of {N}! is {int(digits) + 1}")

