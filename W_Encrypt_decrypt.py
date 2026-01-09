key="PgEfTYaWGHjDAmxQqFLRpCJBownyUKZXkbvzIdshurMilNSVOtec#@_!=.+-*/"
original="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
q=int(input())
s=input()
l=[]
new_s=[]
if q==1:
    l.append(original.replace(original, key))
    encrypt_o=l[0]
    for j in range(len(s)):
        if original.__contains__(s[j]):
            index_j=original.index(s[j])
            new_s.append(s.replace(s,encrypt_o[index_j]))
    print(''.join(new_s))
else:
    l.append(key.replace(key, original))
    dcrypt_k=l[0]
    for j in range(len(s)):
         if key.__contains__(s[j]):
             index_j=key.index(s[j])
             new_s.append(s.replace(s,dcrypt_k[index_j]))
    print(''.join(new_s))




