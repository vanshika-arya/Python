# num=323

# res=[]
# is_palindrome=True
# while num>0:
#     digit=num%10
#     res.push=digit

#     num=num/10

palindrom = lambda n: str(n)==str(n)[::-1]
print(palindrom(121212121212121212))

# is_palindrome = lambda n: (lambda x, r=0: x == (lambda y: (y(x, r)))(lambda a, b: b if a == 0 else y(a // 10, b * 10 + a % 10)))(n)
# print(is_palindrome(12121))
