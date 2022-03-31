---
title : [알고리즘공부][백준]1260 DFS와 BFS
---

### 문제
그래프 DFS 탐색 결과와 BFS 탐색결과 출력
정점 번호는 1번-N번
### 입력 
첫줄 : N 정점의 갯수 M 간선의 갯수 V 탐색 시작 정점 번호  
그다음줄 : 간선이 연결하는 두 정점의 번호 

### 출력
DFS 출력결과
BFS 출력결과

### 예시 1
input 4 5 1  
![image](https://user-images.githubusercontent.com/75241542/160990853-9ff8d726-aafb-4de6-ad4c-e82e475cb28e.png)

### 발상
DFS 출력하려면.. 
- view 지났는지 안지났는지 확인
- dfs - 안지났으면 재귀함수로 
