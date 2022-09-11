# x1,y1 부터 x2,y2 까지 합 구하기

# 일단 행별로 합구하기

# 입력
# N : 표크기 / M : 합을 구해야하는 횟수

N,M = map(int,input().split(' '))
graph = []
for _ in range(N):
  graph.append(list(map(int,input().split(' '))))
# print(graph)

# 합그래프
sumgraph = []
for i in graph:
  sum = 0
  temp = []
  for j in i:
    sum = sum + j
    temp.append(sum)
  sumgraph.append(temp)
# print(sumgraph)

answer = []
for _ in range(M):
  x1, y1, x2, y2 = map(int,input().split(' '))
  x1 -= 1
  y1 -= 1
  x2 -= 1
  y2 -= 1
  tempsum = 0
  for i in range(x1,x2+1):
    # print(sumgraph[i])
    if y1-1 >= 0:
     tempsum += sumgraph[i][y2] - sumgraph[i][y1-1]
    else:
      tempsum += sumgraph[i][y2]

  answer.append(tempsum)

for i in answer:
  print(i)