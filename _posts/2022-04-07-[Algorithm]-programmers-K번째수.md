---
title : "[프로그래머스]K번째수"
layout: single
categories : Algorithm
tag : [python, python3,정렬]
toc : true
---
### | 문제
주어진 배열 array를 i 부터 j까지 자르고 정렬했을 때 , k번째 수 구하기 

### | 입력
array - 배열
commands - [i,j,k]로 이루어진 배열

### | 출력
commands 에 대한 연산을 마친 배열

### | 예시

|**array**|**commands**|**return**|
|---|---|---|
|[1, 5, 2, 6, 3, 7, 4]| [[2, 5, 3], [4, 4, 1], [1, 7, 3]]	|[5, 6, 3]|


### | 발상
- commands에 대한 순회를 돌면서 answer에 append하면 되지않을까!
- i j k 가 사람이 세는 순서랑 달라서 주의해야함
- i번째~j번째 추출 => array[i-1,j]


### | 풀이

``` python
def solution(array, commands):
  answer = []

  for x in commands:
    i = int(x[0])-1
    j = int(x[1])
    k = int(x[2])-1
    print(i,j,k)
    temp = array[i:j]
    temp.sort()
    answer.append(temp[k])
  return answer

```

### | 소감 및 팁
- 그냥 배열.sort() 하면 정렬이 된다