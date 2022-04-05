---
title : "[백준]2606번 바이러스"
layout: single
categories : Algorithm
tag : [python, python3]
toc : true
---

### | 문제
그래프를 탐색하여 바이러스 시작 노드가 주어졌을때 바이러스에 걸리는 노드 수를 구해랏

### | 입력
첫줄 : 컴퓨터 수  
둘째줄 : 간선 수  
셋째줄~ : 간선 정보

### | 출력
감염되는 노드 수

### | 예시
|**input**|**output**|
|---|---|
|7<br>6<br>![image](https://user-images.githubusercontent.com/75241542/161702168-0e8974ec-679a-4999-8308-2383c1cb0cc1.png)|4|

### | 발상
- 바이러스 시작 노드로 해서 bfs나 dfs를 해서 갯수를 세면 되지않으깡!
- graph 정리가 중요
### | 풀이
