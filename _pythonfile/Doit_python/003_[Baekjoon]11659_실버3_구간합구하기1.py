# 입력
# 첫줄 : N의 갯수 , 합을 구해야하는 횟수(M)
# N개의 수
# M 개의 줄에 i, j

# 출력
# M개의 줄에 입력으로 주어진 i-j 합을 출력

# 문제 분석
# 줄의 개수 최대와 합을 구해야하는 횟수 100,000
# 1초 계산량 2,000만번 계산
# 조건 시간은 0.5초
# 최악의 경우 100,000 * 100,000 = 10,000,000,000 1억 이상

N, M = map(int, input().split())
num = list(map(int,input().split()))
answer =[]
# print(num)
s = [num[0]]
for k in range(1,len(num)):
  s.append(s[k-1] + num[k])
# print(s)

for _ in range(M):
  i, j = map(int,input().split())
  i = i-2
  j = j-1
  if i >= 0:
    answer.append(s[j]-s[i])
  else:
    answer.append(s[j])
for i in answer:
  print(i)

#책보고 느낀점
# i,j를 설정하는데에 있어서 배열인덱스랑 세는 것과 달라서 고민이었음
# 그런데 책은 센스있게 0을 하나 추가해서 아예 인덱스를 한칸씩 뒤로 밀어버렸음
# 이런 센스가 필요한듯!
# sum은 변수이름으로 사용가능하다