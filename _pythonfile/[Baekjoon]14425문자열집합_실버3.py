#문제
# 검사대상 문자열 S
# 주어진 문자열에서 검사대상 문자열이 몇개있는지 출력하세요

#입력
# n m
# n개의 검사대상 문자열
# m개의 주어진 문자열

import sys
N,M = list(map(int,input().split()))
listN =[]
listM = []
for _ in range(N):
  listN.append(sys.stdin.readline())
for _ in range(M):
  listM.append(sys.stdin.readline())

count =0
for i in listN:
  if i in listM:
    count += listM.count(i)


print(count)