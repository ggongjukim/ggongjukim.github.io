---
title : "[프로그래머스]가장 큰 수"
layout: single
categories : Algorithm
tag : [python, python3,정렬]
toc : true
---
### | 문제
0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내기

### | 입력
numbers - 숫자 배열

### | 출력
문자열로 return


### | 예시

|**numbers**|**return**|
|---|---|
|[6, 10, 2]|"6210"|


### | 발상
- 0은 첫번째 오면 항상 작아지고 sort도 안되니까 continue로 패스
- 큐를 써야하나? 


### | 풀이1 -> 런타임에러

``` python
from collections import deque
def solution(numbers):
  answer = ''

  visited = {}
  for i in range(len(numbers)):
    visited[numbers[i]] = False
  print(visited)
  
  queue = deque()
  for i in numbers:
    if i != 0:
      queue.append([0,i]) #일단 첫번째 숫자로 다 처넣고 0 6 10
  print("시작 : ", queue)

  while queue:
    #초기화
    for i in range(len(numbers)):
      visited[numbers[i]] = False
    
    temp = queue.popleft() #
    print('temp',temp)
    
    if temp[0] == len(numbers)-1: # 마무리
      break

    for i in range(1, len(temp)):#0 6 -> 0,6,10
      visited[temp[i]] = True
    print(visited)
    
    for i in numbers: # 6, 10, 2
      print(i)
      if not visited[i]: #i != temp[2]:
        print('걸림')
        queue.append(temp[:]) #그대로 복사 하되,
        queue[-1][0] += 1
        queue[-1].append(i)
      print(temp, queue)
    print('\n')
  
  #정리
  tmp =[]
  for i in queue:
    tmp.append(i[1:])
    
  print(tmp)
  result =[]
  for i in tmp:
    result.append(''.join(str(_) for _ in i))
  result2 =[]
  for i in result:
    result2.append(int(i))
  print(result2)
  print(max(result2))
  return str(max(result2))

solution([3, 30, 34, 5, 9])
```
### | 풀이2
``` python
def solution(numbers):
  answer = ''
  temp = sorted(map(str, numbers),reverse =True)
  print(temp)
  
  for i in temp :
    answer += i
  return answer

solution([3, 30,300, 34, 5, 9])
```
### | 소감 및 팁
- 이런건 내가 뭘 할라하지말고 돌려봐서 젤 큰거 찾으면 됨
- Max