# 1부터 N까지 수로 이루어진 순열
#사전순으로 바로 이전에 오는 순열 구하기

# 순열 쫙 구해서 이전꺼 찾아 출력
from itertools import permutations
import sys
N = int(input())
# search = tuple(map(int, input().split(' ')))
search = tuple(map(int,sys.stdin.readline().rstrip().split(' ')))
li = [i+1 for i in range(N)]
# print(li)
per = list(permutations(li, N))
# print(per)

# for i in range(len(per)):
#   if per[i] == search:
#     if i == 0:
#       print(-1)
#       break
#     tmp = per[i-1]
# print("search 인덱스", per.index(search))
tmp = int(per.index(search))-1
# print(per[tmp])
# print(' '.join(tmp))
for i in per[tmp]:
  print(i,end=' ')