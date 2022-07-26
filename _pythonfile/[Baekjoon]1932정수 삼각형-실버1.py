N = int(input())
graph =[]

for _ in range(N):
  graph.append(list(map(int,input().split(' '))))

dp =[graph[0]]
countdp = [graph[0]]

# print(dp, countdp)

for i in range(1,len(graph)):
  countdp.append([])

  for j in range(len(graph[i])):

    #윗줄 한칸 앞이랑 더하기
    if j-1 < 0:
      before = 0
    else:
      before = countdp[i-1][j-1]

    if j>= len(graph[i-1]): #윗줄 길이 보다 크면
      after = 0
    else:
      after = countdp[i-1][j]

    countdp[i].append(max(before,after)+graph[i][j])
print(max(countdp[-1]))
