#공부 못하는 상근이 동생
#
a,b = map(str,input().split())
print(a,b)
a = list(a)
b = list(b)
print(a,b)
a = ''.join(a[::-1])
b = ''.join(b[::-1])
print(max(a,b))
