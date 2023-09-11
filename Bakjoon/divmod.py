A, B, C = map(int, input().split())#공백문자로 구분

print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)