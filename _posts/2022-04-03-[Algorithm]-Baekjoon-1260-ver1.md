---
title : "[백준]1260번 DFS와 BFS-톱니형 리스트"
layout: single
categories : Algorithm
tag : [python, python3]
toc : true
---

### | 문제
그래프 DFS 탐색 결과와 BFS 탐색결과 출력
정점 번호는 1번-N번
### | 입력 
첫줄 : N 정점의 갯수 M 간선의 갯수 V 탐색 시작 정점 번호  
그다음줄 : 간선이 연결하는 두 정점의 번호 

### | 출력
DFS 출력결과
BFS 출력결과

### | 예시 1
|**input**|**output**|
|---|---|
|4 5 1</br>![image](https://user-images.githubusercontent.com/75241542/160990853-9ff8d726-aafb-4de6-ad4c-e82e475cb28e.png)|1 2 4 3</br>1 2 3 4|    
       
### | 발상
DFS 출력하려면.. 
- view 지났는지 안지났는지 확인
- dfs 스택담기, 방문처리, 출력하기
BFS 출력하려면
- bfs 큐담기, 방문처리, 출력하기
이 문제는 graph를 정리하는게 더 중요할지도..!
- 톱니형 리스트 사용하기
- 둘째줄부터 입력부터는 정렬을 하는게 좋을지도..!

### | 풀이
``` python
from collections import deque
n, m, v = map(int, input().split())
#input 받기
graph=[]
for i in range(n+1):#grpah[0] 포함
  graph.append([])
print(graph)
#input 톱니형 리스트로 정리
for i in range(m):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)
print(graph)
# 정렬
for i in range(n+1):
  graph[i].sort()
print(graph)

dfsvisited = [False]* (n+1)
print(dfsvisited)
bfsvisited = [False]* (n+1)
def dfs(graph,v,dfsvisited):
  dfsvisited[v] = True
  print(v, end=' ')
  for i in graph[v]:
    if not dfsvisited[i]:
      dfs(graph,i,dfsvisited)

dfs(graph,v,dfsvisited)

def bfs(graph,start,bfsvisited):
  bfsvisited[start] = True
  queue = deque([start])
  while queue:
    currentNode = queue.popleft()
    print(currentNode,end =' ')
    for i in graph[currentNode]:
      if not bfsvisited[i]:
        bfsvisited[i] =True
        queue.append(i)
bfs(graph,v,bfsvisited)
  
  

```

