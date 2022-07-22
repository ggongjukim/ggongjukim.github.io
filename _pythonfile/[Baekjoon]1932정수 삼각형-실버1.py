N = int(input())
graph =[]
dp =[]
for _ in range(N):
  graph.append(list(map(int,input().split(' '))))
print(len(graph))

for i in range(1,len(graph)):
  for j in range(len(i)):

    #윗줄 한칸 앞이랑 더하기
    if j-1 < 0:
      pass #다음줄로 넘어가기
    else:
      dp.append(graph[i][j] + dp[i-1][j-1])

    if j>= len(graph[i-1]): #윗줄 길이 보다 크면
      pass# 다음 줄로 넘어가기
    else:
      dp.append(graph[i][j] + dp[i-1][j])
