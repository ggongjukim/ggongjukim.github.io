---
title : "[백준]2667번 단지번호붙이기 실버1"
layout: single
categories : Algorithm
tag : [python, python3, BFS]
toc : true
---

### | 문제 :crystal_ball:
1은 집이 있는거  
0은 집이 없는거  
인접하게 집이있는 것을 단지로 만들어라  
단지의 개수와 단지의 집 개수를 출력해라  

### | 입력 :cd:
N : n*n 정사각 행렬 마을  
정사각 행렬 맵

### | 출력 :dvd:
단지 개수  
단지 집 개수 출력  
오름차순으로 

### | 예시 :pill:
|**input**|**output**|
|---|---|
|7<br>0110100<br>0110101<br>1110101<br>0000111<br>0100000<br>0111110<br>0111000<br>|3<br>7<br>8<br>9<br>|

### | 발상 :mag_right:
- map이 주어지는 BFS는 x,y 가 필요하다
- map을 순회하면서 1이면 bfs 진행
- bfs는 상하좌우를 탐색함

### | 풀이  :tada:
```python
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
```
###소감 :pushpin:
- 한번에 잘풀어서 다행이라구 생각
- map을 줄때 띄어쓰기 없이 주면 input().split()을 쓸수 없음 temp로 담아서 list로 바꿈