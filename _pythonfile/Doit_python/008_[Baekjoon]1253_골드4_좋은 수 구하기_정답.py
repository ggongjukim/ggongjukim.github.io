# N 개의 수 중에
# 어떤 다른 수 두개의 합으로 나타낼 수 있으면 그 수는 좋은 수!
# 수의 위치가 다르면 값이 같아도 다른 수
import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split((' '))))
good = 0
arr.sort()
for k in range(len(arr)):
  check = arr[k]
  start = 0
  end = len(arr)-1
  while start < end:
    if arr[start] + arr[end] == check:
      if start !=k and end != k:
        good += 1
        break
      elif start == k:
        start += 1
      elif end == k:
        end -= 1
    elif arr[start] + arr[end] < check:
      start +=1
    else:
      end -=1
print(good)