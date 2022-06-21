#N개의 정점과 M개의 간선으로 이루어진 그래프
# 정점 번호는 1번 부터 N번
# 간선의 가중치는 1
# 정점 R에서 시작하여 BFS으로 노드 방문 순서 출력

# 입력
# 정점의 수 N # 간선의 수 M # 시작 정점 R
# M개의 줄에 간선 정보가 주어짐

# 출력
# i번째 줄에 정점 i의 방문 순서
# 시작정점 방문순서 1
# 시작정점에서 방문할 수 없는 경우 0

# 인접 정점은 오름차순으로 방문
from  collections import deque
N,M,R = list(map(int, input().split()))
graph = []
visited = [False] * (N+1)
for i in range(N):
  graph.append([])

for i in range(M):
  a,b = map(int,input().split())
  graph[a].append(b)

  graph[b].append(a)

# 오름 차순 정리
for i in graph:
  i.sort()
print(graph)
#BFS는 큐!
#그래프, 시작노드, visited

def BFS(graph, start, visited): #

  #큐에 시작노드를 담고
  queue = deque([start])
  #우선 방문처리
  visited[start] = True

  #큐가 존재할동안 계속 반복
  while queue:

    now = queue.popleft()
    #여기! 0 처리하는거!!!
    print("now",now)

    temp = []*len(graph[now])
    for i in graph[now]:

      if not visited[i]:
        visited[i] = True
        queue.append(i)
      else:
        temp.append(True)
      print(visited)

  if len(temp) == len(graph[now]):
    print(0)


BFS(graph, R,visited)

