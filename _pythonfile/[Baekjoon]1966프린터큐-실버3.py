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
dic ={}
temp = list(map(int,input().split(' ')))
print(temp)

for k,v in enumerate(temp):
  dic[k] = v
print(dic)


i = 0
while dic:

  if dic[i] == max(dic.values()):
    tmp = deque()
    tmp = list(dic.keys())
    print("팝", tmp)

    dic.pop(tmp.popleft())
  # else:
  #   tmp = dic[i]

  i += 1