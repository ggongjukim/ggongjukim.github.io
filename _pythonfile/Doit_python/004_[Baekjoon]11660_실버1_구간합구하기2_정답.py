# x1,y1 부터 x2,y2 까지 합 구하기

# 일단 행별로 합구하기

# 입력
# N : 표크기 / M : 합을 구해야하는 횟수

N,M = map(int,input().split(' '))
graph = [[0]*(N+1)]

for i in range(N):
  temp = list(map(int,input().split(' ')))
  graph.append([0] + temp)
# print(graph)

#합그래프
sumgraph = graph
# print(sumgraph)
for i in range(1,N+1):
  for j in range(1,N+1):
    sumgraph[i][j] = sumgraph[i-1][j] + sumgraph[i][j-1] - sumgraph[i-1][j-1] + graph[i][j]
# print(sumgraph)
# print(graph)

answer = []
for _ in range(M):
  x1, y1, x2, y2 = map(int,input().split(' '))
  answer.append(sumgraph[x2][y2] - sumgraph[x1-1][y2] - sumgraph[x2][y1-1] + sumgraph[x1-1][y1-1])

for i in answer:
  print(i)