---
---
### | 문제
정수의 배열이 있을 때 적절히 더하거나 빼서 타겟 넘버를 만들 수 있는 경우의 수를 구해윱

### | 입력
숫자 배열, 타겟 넘버

### | 출력
타겟 넘버를 만들 수 있는 조합의 경우의 수

### | 예시

|**숫자 배열**|**타겟**|**결과**|**원리**|
|---|---|---|---|
|[1,1,1,1,1]|3|5| 5-3 =2 2/2 =1 1만 빼면됨|
|[4,1,2,1]|4|2|   8-4 =4 4/2 =2 2만 빼면됨=2를 만들수 있는 방법|
|[4,1,2,2]|5|2|   9-5 =4 4/2 =2 2만 빼면됨|
|[4,1,2,2]|4|-| 9-4=5 
|[1,1,1,1,1]|1|5| 5-1 =4 4/2 = 2 2를 만들수 있는방법

### | 발상
- 이외진? ... 이게 왜 bfs,, dfs인지 알다가도 모를일...
- 구냥 숫자 앞에 +랑 -해서 타겟 숫자 나오면 횟수++ 해주면 되는거 아닌가? => 이거 자체가 그래프 탐색이었음... !

### | 풀이

``` python
from collections import deque
def solution(numbers, target):
  count =0
  visited = [False]* len(numbers)
  queue = deque()
  queue.append([numbers[0],0])
  queue.append([-1*numbers[0],0])
  visited[0] = True
  print(queue)

  while queue:

    currentNode = queue.popleft() # currentNode = 1
    if currentNode[1] == len(numbers)-1:
      print(count)
      break
    queue.append([currentNode[0]+numbers[currentNode[1]+1],currentNode[1]+1])
    queue.append([currentNode[0]-numbers[currentNode[1]+1],currentNode[1]+1])
    
    if currentNode[1]+1 == len(numbers)-1:
      print('걸림')
      if queue[-1][0] == target :
        count += 1
      if queue[-2][0] == target :
        count += 1
      print(count)
    print(queue,currentNode[1]+1)
    print('\n')
  answer = 0
  return answer

solution([1, 1, 1,1,1]	,3)

```

### | 소감
- 너무 어렵다..
- dfs bfs 아주 기본예제에 갇혀있어서 어려운거 같다..
- 응용하는 연습이 필요해보인다!
