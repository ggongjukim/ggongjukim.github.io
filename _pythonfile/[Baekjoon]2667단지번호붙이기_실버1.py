from collections import deque

N = int(input())
graph = []
dangi =[]
for _ in range(N):
  temp = list(input())
  graph.append(temp) #map(int, input().split() 이렇게 하면

#print("graph",graph)
visited = [[0]*N for _ in range(N)] # d이렇게 하는게 중요 [[0]*N]*N 안대!!!
#print(visited)
def BFS(graph, start,visited):
  #print("BFS")
  queue = deque([start])
  a,b= start
  visited[a][b] = 1
  count =0
  while queue:
    count += 1
    #print("count",count)
    x,y = queue.popleft()

    #상하좌우 탐색

    if y-1 >= 0 :
      if graph[x][y-1] == '1' and visited[x][y-1]==0:#좌
        visited[x][y - 1] =1
        queue.append([x,y-1])

    if y+1 < N :
      if graph[x][y+1] == '1' and visited[x][y+1]==0:#우
        visited[x][y + 1] =1
        queue.append([x, y+1])

    if x-1 >= 0 :
      if graph[x-1][y] == '1' and visited[x-1][y] ==0:#상
        visited[x-1][y] =1
        queue.append([x-1,y])
    if x+1 < N :
      if graph[x+1][y] =='1' and visited[x+1][y] ==0:#하
        visited[x+1][y] =1
        queue.append([x+1,y])

    #print("que",queue)
  dangi.append(count)


# BFS(graph, [0,1],visited)
for i in range(N):
  for j in range(len(graph[i])):
    #print("for", i,j,graph[i][j])
    if visited[i][j] == 0 and graph[i][j] == "1":
      BFS(graph, [i,j],visited)

print(len(dangi))
dangi.sort()
for i in dangi:
  print(i)