# 인덱스로 탐색
# 연속한 수도 아니고 2개씩 본다고 했으니 양쪽 끝에서 시작해야함
# 투포인터 방식도 여러가지있다는 거 알기
N = int(input())
M = int(input())
arr = list(map(int,input().split(' ')))
print(arr)
arr.sort()#정렬
print(arr)

sum = arr[0]+arr[N-1]
start = 0
end = N-1
count =0
while start < end:
  print(start, end, sum, count)
  if sum > M:
    sum -= arr[end]
    end-=1
    sum += arr[end]
  elif sum < M:
    sum-= arr[start]
    start +=1
    sum += arr[start]
  else:# 같을떄
    count+=1
    sum -= arr[start]
    sum -= arr[end]
    start +=1
    end -=1
    sum+= arr[start]
    sum +=arr[end]
print(count)