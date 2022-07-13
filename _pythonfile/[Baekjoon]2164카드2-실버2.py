# N장의 카드
# 1 - N 까지 번호
# 1 제일 위 N 가장아래

# 제일 위에 있는 카드 버린다
# 그다음 제일위에있는 카드를 제일 아래있는 카드 밑으로
# 이걸 한장 남을 때까지 진행

# N = int(input())
# li = [ i for i in range(N,0,-1) ]
# print(li)
# while len(li) > 1: # 한개 초과 일때 까지
#
#   li.pop() # 버림
#   tmp = li.pop()
#
#   li = [tmp] + li
#
#
# print(li[0])

from collections import deque
N = int(input())
li = deque()
for i in range(N):
  li.append(i+1)

while len(li) > 1:
  li.popleft()
  tmp = li.popleft()
  li.append(tmp)
print(li[0])

#다른 풀이
from collections import deque

li = deque([i for i in range(1, int(input()) + 1)])

while len(li) >= 2:
    li.popleft() # 왼쪽이 제일 위
    li.rotate(-1) #

print(li[0])