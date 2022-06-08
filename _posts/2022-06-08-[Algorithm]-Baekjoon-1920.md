---
title : "[백준]1920번 수찾기"
layout: single
categories : Algorithm
tag : [python, python3]
toc : true
---

### | 문제
N개의 정수가 주어졌을때 x정수가 존재하는지 알아내는 프로그램

### | 입력
첫줄: N
둘째줄 : N개의 정수(배열 A)
셋째줄 : M
넷째줄 : M개의 수

### | 출력
M개의 수가 배열 A에 존재하면 1, 존재하지 않으면 0


### | 발상
- 이진 탐색으로 값이 배열에 존재하면 1 존재하지 않으면 0 
### | 풀이
```python

n = int(input())
A_arr = list(map(int,input().split()))
m = int(input())
M_arr = list(map(int,input().split()))

A_arr.sort()
def binarySearch(arr, target, start, end):
  if start > end:
    return 0
  mid = (start+end)//2
  if arr[mid] == target:
    return 1
  elif arr[mid] > target:
    return binarySearch(arr, target, start, mid-1)
  else:
    return binarySearch(arr, target, mid+1, end)

for i in M_arr:
  print(binarySearch(A_arr,i,0,n-1))
```
