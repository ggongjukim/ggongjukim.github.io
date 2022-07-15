# 1부터 N까지 수로 이루어진 순열
#사전순으로 바로 이전에 오는 순열 구하기

# 순열 쫙 구해서 이전꺼 찾아 출력
from itertools import permutations

N = int(input())
li = list(map(int,input().split(' ')))
result = ''
# print(li)

def search(num):

  tmp = li[num*-1:] #검사할 부분부분
  tmp.sort()
  if tmp == li[num*-1:]:
    search(num+1)
    return

  # 오름 차순 아니면 검사를 해야징
  tmpper = list(permutations(tmp, len(tmp)))
  # print("tmpper", tmpper)

  for i in range(len(tmpper)):
    if tmpper[i] == tuple(li[num*-1:]):
      tmp = list(tmpper[i-1])
  global result
  result = li[:num*-1] + tmp


temp = li[:]
temp.sort()
if li == temp:
  print(-1)
else:
  search(2)
  for i in result:
    print(i, end=' ')
