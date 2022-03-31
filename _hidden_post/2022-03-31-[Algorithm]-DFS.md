---
title : DFS 공부
---

### DFS 개념 
- 깊이 우선
- 뿌리의 뿌리의 뿌리의 뿌리... 를 찾아서..!
- 스택을 이용!
- 재귀함수 이용!


###  예제
![image](https://user-images.githubusercontent.com/75241542/160992601-f87529f7-4bd3-4296-97c4-48c4570c67eb.png)
탐색 순서 : 1->2->7->6->8->3->4->5

### idea
- 현재노드 일단 방문 체크
- graph[현재노드] 에서 방문 안한애 있으면 dfs 실행
- graph는 크기 순으로 정리가 잘되어있음

``` python
def dfs(graph,v,visited): #v는 현재노드
  visited[v] = True
  print(v,end=' ')
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)
      
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
### point 
- graph를 노드에 따라 잘 정리하는 것이 중요하다!
- 재귀함수가 뽀인트!
