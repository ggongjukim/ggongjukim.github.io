#0 으로 split
# 1 로 spilt
#더 적은걸 선택하여 반대로 바꾸기

S = list(map(int,input()))
# zero = S[:].split('1')
# print(zero)
# one = S[:].split('0')
# print(one)
zero = 0
one = 0
isZero = False

if S[0]==1:
  one +=  1
else :
  zero += 1
  isZero = True

for i in range(1,len(S)):
  if S[i] == S[i-1]:
    continue
  else:
    if isZero: ##여태 제로 였으면
      one += 1
      isZero = False
    else:
      zero += 1
      isZero = True
# print(zero, one)

if zero == 0 or one == 0:
  print(0)
else:
  print(min(zero,one))

## 다른 사람 풀이
## 엄청 짧고 엄ㅊ청쉽네 ..