#문제
#김진영이 듣도 못한 사람의 명단과
#보도 못한 사람의 명단이 주어질때 듣도보도못한 사람의 명단을 구해라

#입력
#N 듣도 못한 사람의 수 ,M보도못한 사람의 수
#N개 줄에 걸쳐 듣도 못한 사람의 이름과
#N+2째 줄붜 보도못한 사람의 이름
#이름 길이 20이하

# 출력
# 듣보잡의 수와 명단을 출력
import  sys
N, M = list(map(int, input().split()))
D_list =[]
B_list = []
for _ in range(N):
  D_list.append(sys.stdin.readline())
for _ in range(M):
  B_list.append(sys.stdin.readline())

count = list(set(D_list)&set(B_list))
# for i in range(N):
#   if D_list[i] in B_list:
#     count.append(D_list[i])

count.sort()

print(len(count))
for i in count:
  print(i,end ='')
