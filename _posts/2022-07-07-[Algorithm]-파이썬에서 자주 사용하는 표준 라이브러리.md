---
layout: single
title: "파이썬에서 자주 사용하는 표준 라이브러리"
categories : Algorithm
tag : [python, python3]
toc : true
---

### | 실전에서 유용한 표준 라이브러리
- 내장함수        
  기본 입출력 함수, 정렬 함수 등      
  import 구문 없이 사용가능
   
- itertools     
  파이썬에서 반복되는 데이터 처리                
  순열, 조합 등       
  모든 경우의 수를 고려해야하는 경우 효과적으로 사용가능      
  순열 조합 라이브러니는 완전탐색 유형에서 유용함     


- heapq    
  힙 자료구조를 제공       
  우선순위 큐 기능을 구현하기 위해 사용        
  다익스트라 알고리즘과 같은 최단경로 알고리즘에서 많이 활용         

- bisect     
  이진탐색 기능
 
- collections      
  덱(deque), 카운터(Counter) 포함    

- math     
  다양한 수학적 기능 제공
<br><br><br>

### | 자주 사용하는 내장 함수
- ```sum()```        
  리스트나 튜플 등의 원소들의 합 반환

- ```min()```, ```max()```    
  가장 작은 값 또는 큰 값 반환

- ```eval()``` :star:       
  수식을 표현된 식을 계산한 결과를 반환

  ```python
  result = eval("(3+5)*7")
  print(result) # 56
  ```
 
- ```sorted()```      
  리스트와 같은 반복가능한 개체가 들어왔을때 각 원소를 정렬한 결과를 반환      
  - 오름차순 내림차순        
    오름차순이 default     
    내림차순은 ```reverse = True```를 마지막 인수로 넣어줘야함
  - key 속성
    딕셔너리나 튜플에서 정렬 기준을 key 속성으로 명시할 수 있음     
    정렬 기준은 람다함수로 간단히 표현   
    ```key = lambda x : x[1]``` => 두번째 원소 기준으로 정렬하세요

<br><br><br>

### | 순열과 조합 쓰는 방법
순열은 순서를 고려하고      
조합은 순서를 고려하지 않음

- 순열   
  ```from itertools import permutaions``` 쓰기       
  ```list(permutaions(리스트,2))``` => 리스트에서 두개뽑는 조합 모두 반환

  ```python
  from itertools import permutaions
  li = ['a','b','c']
  result = list(permutaions(li,3))
  print(result) 
  # 결과 
  # [('a','b','c'),('a','c','b'),('b','a','c'),('b','c','a'),('c','a','b'),('c','b','a')]
  ```

- 조합   
  ```from itertools import combinations``` 쓰기       
  ```list(combinations(리스트,2))``` => 리스트에서 두개뽑는 조합 모두 반환

  ```python
  from itertools import combinations
  li = ['a','b','c']
  result = list(combinations(li,2))
  print(result) 
  # 결과 
  # [('a','b'),('a','c'),('b','c')] 
  ```

- 중복 순열 :question:

  ```python
  from itertools import product
  li = ['a','b','c']
  result = list(combinations(li,repeat = 2)) #2개를 뽑는 모든 순열 구하기 (중복허용)
  print(result)
  # 결과 
  #
  ```

- 중복 조합 :question:

  ```python
  from itertools import combinations_with_replacement
  li = ['a','b','c']
  result = list(combinations(li,2)) #2개를 뽑는 모든 조합 구하기 (중복허용)
  print(result)
  # 결과 
  #
  ```

<br><br><br>

### | Counter  :question:
collestions 라이브러리의 Counter   
등장 횟수를 세는 기능  
각 원소가 몇번씩 등장했는지 알고자 할 때       
**딕셔너리로 변환하여 사용 가능**

```python
from collections import Counter

counter = Counter(['red','blue', 'red','green','blue', 'blue' ])

print(counter['blue']) # 3
print(dict(counter)) # {'red' : 2, 'blue' : 3, 'green' :1}
```


<br>

### | 최대 공약수 /  최소 공배수
최대 공약수  ```gcd()```

  ```python
  import math
  print(math.gcd(21,14)) # 최대 공약수

  def lcm(a,b): #최대 공배수
    return a*b // math.gcd(a,b)
  
  print(lcm(21,14))
  ```