---
title : "[프로그래머스]문자열 압축"
layout: single
categories : Algorithm
tag : [python, python3]
toc : true
---
### | 문제
 문자열에서 같은 값이 연속해서 나타나는 것을 그 문자의 개수와 반복되는 값으로 표현하여 더 짧은 문자열로 줄여서 표현하기  
 반복이 안되는 경우는 1로 표현하지 않고 그냥 생략한다

### | 입력
문자열 s

### | 출력
가장 짧게 표현되는 문자열의 길이 k

### | 예시

|**s**|**result**|
|---|---|
|"aabbaccc"|7|
|"ababcdcdababcdcd"|9|
|"abcabcdede"|8|
|"abcabcabcabcdededededede"|14|
|"xababcdcdababcdcd"|17|



### | 발상
- 1개 반복으로 설정해서 문자열 길이 세고,2개 반복으로 설정해서 문자열 길이 세고, 3개 반복으로 설정해서 문자열 길이 세고..  최대 반복 개수는 문자열 길이의 절반이다.
  - => 1 부터 len(문자열)//2 까지 순회 => range(1,len(s)//2+1)
- 


### | 풀이

``` python
def solution(s):
  result = len(s)
  minlen = len(s)
  for k in range(1,len(s)//2+1): # 2부터 절반까지 순회하여 조사
    arr = []
    total = 1
    count = 0
    compare = s[0:k] # 문자열 0 부터 k까지
    finish=''


    for i in range(0+k, len(s)+k,k): #k개씩 짤라서 비교해서 검사
      if compare == s[i:i+k]:# 단위랑 같으면 
        total += 1 #단위 계수에 1더해주기
      else :# 다르면
        if total == 1:#반복횟수가 1이면
          finish += compare#반복횟수 안하고 붙이기
        else:
          finish += str(total)+compare#반복횟수가 1 이상이면 반복횟수를 string으로 바꿔서 붙이기
        compare = s[i:i+k]#비교단위 다음 순서로 교체
        total = 1#total 초기화

    result = len(finish)# 순회하여 조사할때마다 문자열 길이 조사 
    if minlen > result:
      minlen = result
  return minlen

```

### | 소감 및 팁
- 문자열자르기
  - 문자열[시작:끝]
- 나누기 종류
  - 5 // 2 => 2(몫)
  - 5 / 2 => 2.5(나누기)
  - 5 % 2 => 1(나머지)
- 생각하는 건 늘 어렵다.. 