#주어진 수 N개 중에서 소수가 몇개인지 찾기

N = int(input())
li = list(map(int,input().split(' ')))
print(li)
count =N
for i in li:
  for j in range(1,i+1):
    print("i,j",i ,j,i % j)
    if i == 1:
      count -= 1
      break

    if i % j == 0: # 나누어서 0 이 나왔는데
      if j == 1 or j == i: #나눈 수가 1이나 자기자신이 아님
        continue
      else:
        print("소수가 아닙니다")
        count -= 1
        break
print(count)

##풀었던건데 왜이리 오래걸리노  ㅠ
