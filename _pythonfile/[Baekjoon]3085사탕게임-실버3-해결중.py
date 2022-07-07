##봄보니 게임
# n*n 크기에 사탕을 채워 놓는다 색은 모두 같지 않을 수 도 있다.
# 사탕색 다른 인접한 두칸을 고른다
# 고른 칸에 들어있는 사탕을 서로 교환한다
# 모두 같은 색으로 이루어져있는 가장 긴 행 또는 열을 고른다음 사탕을 모두 먹는다
# 사탕이 채워진 상태가 주어졌을때 상근이가 먹을 수 있는 사탕의 최대 갯수를 구해라

# c 빨
# p 파
# z 초
# y 노

# 우, 하 문자 다르면 발상 하나씩 바꿔 보고 행 렬 같은 문자 최대 인거 찾기

N = int(input())
graph = []
tempcount = []
for _  in range(N):
   graph.append(list(input()))

print(graph)

def findLongest(graph):
  tempcount.clear()
  for i in graph:
    #행으로 찾기
    tempcount.append(i.count('C'))
    tempcount.append(i.count('P'))
    tempcount.append(i.count('Z'))
    tempcount.append(i.count('Y'))

  tmp = []
  changeGraph =[]
  # 열로 찾기
  for i in range(len(graph)):
    tmp.clear()

    for j in range(len(graph)):
      tmp.append(graph[j][i])
      # print('j',j,' i',i,graph[j][i],tmp)

    changeGraph.append(tmp[:])
    # print("changeGraph", changeGraph)

  for i in changeGraph:
    tempcount.append(i.count('C'))
    tempcount.append(i.count('P'))
    tempcount.append(i.count('Z'))
    tempcount.append(i.count('Y'))

  return max(tempcount),tempcount

for i in graph:
  for j in range(len(i)-1):
    if i[j] != i[j+1]:
      i[j],i[j+1] = i[j+1],i[j]
      # print(graph)
      print(i[j],findLongest(graph))
      i[j],i[j+1] = i[j+1],i[j] #다시 돌려놓기


