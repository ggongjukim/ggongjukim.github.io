#큐 였음
#새로운 조건
# 중요도 확인
# 현재 문서보다 중요한 문서가 하나라도 있으면 맨뒤에 배치
# 특정 문서가 몇번째로 인쇄되는 지 알아내는 것

#입력
#테스트케이스의 수 : 두줄
# N 문서개수
# M 몇번째로 출력되는지 궁금한 정수 맨 왼쪽은 0 번째


import sys
from collections import deque
countarr=[]
def test():
  arr = []
  count = 0
  n,m = list(map(int,input().split(' ')))
  temp = list(map(int,input().split(' ')))
  # print(temp)

  for k,v in enumerate(temp):
    arr.append([v,k])
  # print(arr)

  while arr:
    if max(arr)[0] == arr[0][0]:
      count += 1
      if m == arr[0][1]:
        countarr.append(count)
        break
      arr = arr[1:]
      # print("pop", arr)

    else :
      arr = arr[1:] + [arr[0]]
      # print("뒤에 붙이기", arr)

T = int(input())
for _ in range(T):
  test()

for i in countarr:
  print(i)

# #다른 풀이
# from collections import deque
#
# t = int(input())
# for _ in range(t):
#     n, m = map(int, input().split())
#     print_q = deque(list(map(int, input().split())))
#     order_q = deque([[0] for _ in range(n)])
#
#     answer = []
#     order_q[m] = 1
#     while print_q:
#         print_now = print_q.popleft()
#         order_now = order_q.popleft()
#
#         if print_q and print_now < max(print_q):
#             print_q.append(print_now)
#             order_q.append(order_now)
#         else:
#             answer.append(order_now)
#     print(answer.index(1) + 1)