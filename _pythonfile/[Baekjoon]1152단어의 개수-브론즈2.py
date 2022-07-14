##문자열의 개수

li = list(map(str, input().split(' ')))
if li[0] == '':
  li = li[1:]
if li[-1] == '':
  li = li[:len(li)-1]

print(li)
print(len(li))