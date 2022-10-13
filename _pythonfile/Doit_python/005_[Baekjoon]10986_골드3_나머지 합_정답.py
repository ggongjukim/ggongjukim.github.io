# N 개의 수에서 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 구하는 프로그램
N, M = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))
sumarr =[arr[0]]
result = 0
C =[0]*M
for i in range(1,len(arr)):
  sumarr.append(sumarr[i-1]+arr[i])

# print(sumarr)
sumarr = list(map(lambda x: x%M,sumarr))
# #갯수 세기
# # print(sumarr.count(0))
# result += sumarr.count(0) // count 쓰니까 뻑가네
#
# #sumarr 같은거 추려서 *개 중에 2개뽑는거 더하기
# # 개수를 어떻게 세지?
# for i in range(M): # 나눠주는 애가 M이니까 나머지는 0부터 M-1 까지 존재하겠지
#   temp = sumarr.count(i)
#   result += temp*(temp-1)/2
# print(int(result))

for i in range(N):
  if sumarr[i]%M ==0:
    result += 1
  C[sumarr[i]%M]+=1

for i in range(M):
  result += C[i] * (C[i] - 1) // 2

print(result)