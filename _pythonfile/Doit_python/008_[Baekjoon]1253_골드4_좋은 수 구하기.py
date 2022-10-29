# N 개의 수 중에
# 어떤 다른 수 두개의 합으로 나타낼 수 있으면 그 수는 좋은 수!
# 수의 위치가 다르면 값이 같아도 다른 수
# 예외
# 3
# -5 -2 -3
# 정답: 1
#
# 3
# 0 0 0
# 정답: 3
#
# 3
# 0 0 1
# 정답: 0
import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split((' '))))
arr.sort() #정렬 한번 해주고
good = []
check = len(arr)-1
# arr = arr[:len(arr)-1]
start = 0
end = len(arr) - 1

while check >= 0:
  # print( check,arr[check],"/", start, end,"합",arr[start] + arr[end])
  if start >= end: # or start > len(arr) or end < 0 :
    check -= 1
    start = 0
    end = len(arr)-1

  if check < 0:
    break


  if arr[start] + arr[end] > arr[check] :
    end -= 1
  elif arr[start] + arr[end] < arr[check]:
    start +=1
  else : # 좋은 수 등장
    # good +=1
    if start != check and end != check:
      # print("걸림", check,arr[check],"/", start, end, "합", arr[start] + arr[end])

      good.append(arr[check])
      check -= 1
      start = 0
      end = len(arr)-1
    elif start == check:
      start += 1
    elif end == check:
      end -= 1

print(len(good))