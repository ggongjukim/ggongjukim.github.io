#N개 수가 주어졌을때 이를 오름차순으로 정렬

#입력
# 첫째줄 주어질 수의 개수 N
# N(1 ≤ N ≤ 10,000,000)

#출력
#N개의 줄에 오름차순으로 결과를 출력

#풀이1
import sys

N = int(input())
li = [0]*10000

for _ in range(N):
  li[int(sys.stdin.readline())-1] +=1
for k,v in enumerate(li):
  if v !=0:
    for i in range(v):
      print(k+1)

  # li.append(int(sys.stdin.readline()))
# # print(li)
#
# li = sorted(li)
# for i in li:
#   print(i)

# 이렇게 하니까 맞아땅!
# import sys
#
# n = int(input())
# dic = {}
# for i in range(n):
#   temp = int(sys.stdin.readline())
#   if temp in dic:
#     dic[temp] = dic[temp] + 1
#   else:
#     dic[temp] = 1
#
# dic = sorted(dic.items())
# for i in dic:
#   for j in range(i[1]):
#     print(i[0])