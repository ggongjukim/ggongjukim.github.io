# 수열 A가 주어졌을때 가장 긴 증가하는 부분 수열을 구하는 프로그램
# 수열에서 규칙을 찾았을 때 가장 긴것은 무엇일까

# DP 조건
# 작은 문제로 큰문제 해결 가능
# 중복 등작
N = int(input())
li = list(map(int,input().split(' ')))
countli = []
def countSeq(i1, i2):
  count =2
  d = li[i2] - li[i1]
  for i in li:
    if i == li[i2] + d:
      count += 1
    countli.appned(count)

 # ??? 