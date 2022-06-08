---
title : "[백준]10816번 숫자카드2-이진탐색"
layout: single
categories : Algorithm
tag : [python, python3]
toc : true
---

### | 문제
숫자카드 N개, 정수 M개 정수가 적힌 숫자카드 몇개인지

### | 입력
첫줄 : N 숫자카드개수
둘째줄 : N개의 정수
셋째줄 : M 확인할 정수 개수
넷째줄 : M개의 정수

### | 출력
숫자카드에 몇개인지 출력



### | 풀이
```python
n = int(input())
n_arr = list(map(int, input().split()))
m = int(input())
m_arr = list(map(int, input().split()))
n_dic = {}

n_arr.sort()
before = n_arr[0]
for i in range(0,len(n_arr)):
  try:
    n_dic[n_arr[i]] += 1
  except:
    n_dic[n_arr[i]] = 1


for i in m_arr:
  try:
    print(n_dic[i], end = " ")
  except:
    print(0, end = " ")
```

### | 소감
이분 탐색이라는데 왜 이분탐색이지? .. 
dictionary을 만들고 key를 찾을 때 이분탐색을 찾으라는 것 같다