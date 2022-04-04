---
layout: single
title: "BFS 공부"
categories : Algorithm
tag : [python, python3]
toc : true
---

### | BFS 개념
- 너비 우선탐색 Breadth-First Search
- 큐 사용!

### | 예제
![image](https://user-images.githubusercontent.com/75241542/160992601-f87529f7-4bd3-4296-97c4-48c4570c67eb.png)  
내답 : ~~1 -> 2 -> 3-> 8-> 7-> 6 -> 4 -> 5~~  
정답 : 1 -> 2 -> 3 -> 8 -> 7 -> 4 -> 5 -> 6  

### | idea
- 현재 노드 큐에 넣고 방문 체크
- 큐 사용
- graph[현재 노드] 중 방문 안한애 있으면 방문처리하고 큐에 넣음
- 세가지 기능 : 담기(큐에넣기), 방문처리, 출력하기
- 담기(큐에넣기) : graph[현재노드] 순회해서 방문한적없으면 방문처리하고 큐에넣기
- 방문처리 : graph[현재노드]순회해서 방문한적 없으면 방문처리
- 출력하기 : 큐에서 남아있는 것중 맨처음 원소 뽑아 현재노드로 설정하고 출력하기
- 순서 : 출력하기 -> 방문처리 -> 담기(큐에넣기)
- 시작세팅 : 시작노드를 담기(큐에넣기)하고 방문처리 (담기하면 세팅이후 큐에 남아 자동으로 출력하기 됨)

```python
from collections import deque

def bfs(graph,start,visited): #v는 현재노드
  visited[start] = True
  queue = deque([start])
  while queue: #큐에 남아있는게 있으면-> 큐에 남아있는게 있을때 까지
    #출력하기
    currentNode = queue.popleft()
    print(currentNode, end =' ')
      
      for i in graph[currentNode]:
        if not visited[i]:
          #방문처리
          visited[i] = True    
          #담기
          queue.append(i)
          
graph = [
[],
[2,3,8],
[1,7],
[1,4,5],
[3,5],
[3,4],
[7],
[2,6,8],
[1,7]
]
visited = [False]*9

dfs(graph,1,visited)
```

### | point
- 큐를 사용한다!
- dfs bfs 는 담기, 출력하기, 방문하기 기능이 있다
- dfs 는 방문하기와 출력하기가 동시에 이루어지지만 
- bfs는 아니다!

