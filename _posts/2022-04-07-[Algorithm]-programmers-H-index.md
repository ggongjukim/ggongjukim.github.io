---
title : "[프로그래머스]H-Index"
layout: single
categories : Algorithm
tag : [python, python3]
toc : true
---
### | 문제
발표한 논문 n편 중, h번 이상 인용된 논문이 h편이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 h-index입니다. => 먼소리지?

### | 입력
과학자가 발표한 논문의 인용횟수를 담은 배열 citations

### | 출력
h-index return

### | 예시

|**citations**|**return**|
|---|---|
|[3, 0, 6, 1, 5]| 3|


### | 발상
- 내림차순으로 해서 h편이상 인용논문이 h개 이상이면 return 아니면 index +1
- [10,10,10,10,10]은 5다 주의할것



### | 풀이

``` python
def solution(citations):
    answer = 0
    citations.sort(reverse= True)
    hindex =0
    while True:
      if hindex >= len(citations):
        answer = len(citations)
        break

      temp = citations[:hindex]
      if citations[hindex] <= len(temp):
        answer = hindex
        break
      else:
        hindex += 1
    return answer

```

### | 소감 및 팁
- 순서대로가 쉬울때가 더많다