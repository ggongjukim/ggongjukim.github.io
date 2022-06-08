---
layout: single
title: "이진 탐색(Binary Search) 공부"
use_math: true
categories : Algorithm
tag : [python, python3]
toc : true
---

### | 이진 탐색 개념
- 순차 탐색 : 앞에서부터 데이터를 하나씩 확인하는 방법
- 이진 탐색 : **정렬되어있는 리스트**에서 탐색 범위를 반으로 좁히며 탐색하는 방법
  - 로그 시간의 시간 복잡도를 가진다 $log_{2}N => O($logN)
  - 시작점, 끝점, 중간점을 변수로 가지고 탐색
  - 중간점이 2개일 경우 (시작점+끝점)/2 의 소수점 이하를 제거하여 사용



### | 이진 탐색 함수
``` python
#이진 탐색 함수
def binarySearch(arr, start, end, target):
  #예외처리
  if start > end: #start가 end 보다 크면
    return None #찾는거 없습니다
  
  mid = (start + end)//2 #소수점 날리기
  if arr[mid] == target:
    return mid

  elif arr[mid] < target: #찾는 값이 중간값보다 크면
    return binarySearch(arr,start,mid-1,target) #end를 중간값-1로 넣기

  else:
    return binarySearch(arr,mid+1,end,target) #start를 중간값+1로 넣기

#배열 원소 개수와 target값 받기
n, target = list(map(int,input(.split())))

#전체 원소 입력
arr = list(map(int,input(.split())))

#결과
result = binary_search(arr,target,0,n-1)
if result === None:
  print("찾으려는 값 없음")

else:
  print(resultl+1, "번째있습니다")

```
