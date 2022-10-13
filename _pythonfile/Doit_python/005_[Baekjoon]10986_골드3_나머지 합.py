# N 개의 수에서 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 구하는 프로그램
N, M = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))
sumarr = [arr[0]]
for i in range(1,len(arr)):
  sumarr.append(sumarr[i-1]+arr[i])
print(sumarr)

sumarr2 = sumarr[:] + arr[:]
for i in range(2,len(sumarr)):
 for j in range(i,len(sumarr)):
   sumarr2.append(sumarr[j]-sumarr[i-2])
print(sumarr2)

count = 0
for i in sumarr2:
  if i%M ==0:
    count += 1

print(count)