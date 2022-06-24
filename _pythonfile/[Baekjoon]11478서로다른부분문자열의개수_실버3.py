#문제
# 문자열 s 가 주어졌을 때, s의 서로다른 부분 문자열의 개수를 구하는 프로그램을 작성하세요
#입력
#문자열 S 길이는 1000이하

#발상
#순열을 써야겠떠
from itertools import permutations
S = input()
N = len(S)
li = list(S)
result = []
for i in range(1,N+1):
  for j in range(N):
    if j+i > N:
      continue
    temp = li[j:j+i]
    # print("j,i",j,i,''.join(temp))
    result.append(''.join(temp))
result = set(result)
print(len(result))

## 소감
# set 할때 리스트끼리 비교하는거는 안된다 [a,b] [a,b] 중복이냐 아니냐 이런거는 못한다