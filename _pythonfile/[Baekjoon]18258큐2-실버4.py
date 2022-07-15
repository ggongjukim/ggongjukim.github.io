#정수를 저장하는 큐를 구현한 다음
#입력으로 주어지는 명령을 처리하는 프로그램램
from collections import deque
import sys
que = deque()
N = int(input())
for _ in range(N):

  order = sys.stdin.readline().rstrip() #input()
  # order.replace('\n','')
  # order.rstrip('\n')

  if 'push' in order:
    order,x = order.split(' ')
    que.append(x)

  elif 'pop' in order:
    if len(que) == 0:
      print(-1)
      # break
    else:
      print(que.popleft())

  elif 'size' in order:
    print(len(que))

  elif 'empty' in order:
    if len(que) == 0:
      print(1)
    else:
      print(0)

  elif 'front' in order:
    if len(que) == 0:
      print(-1)
      # break
    else:
      print(que[0])

  elif 'back' in order:
    if len(que) == 0:
      print(-1)
      # break
    else:
      print(que[-1])
  # print(que)