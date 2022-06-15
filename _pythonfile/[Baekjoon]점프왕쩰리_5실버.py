from collections import deque
mmap = []
N = int(input())
for _ in range(N):
  mmap.append(list(map(int, input().split())))
visit = [[False]* N for _ in range(N)]

# print(visit)
queue = deque()
queue.append([0,0]) #위치좌표
while queue:
  # print("queue",queue,end='')
  x,y = queue.popleft()#이게 뭔지 잘 모르겠음 # 행, 렬 인덱스로 나오네

  if x == N-1 and y == N-1:
    print("HaruHaru")
    exit(0)

  #점프
  jump = mmap[x][y]
  nx = x + jump
  ny = y + jump
  # print("nx,ny",nx,ny)

  if 0<=nx<N and visit[nx][y] == False:
    visit[nx][y] = True
    queue.append([nx,y])

  if 0<=ny<N and visit[x][ny] == False:
    visit[x][ny] = True
    queue.append([x,ny])

print("Hing")