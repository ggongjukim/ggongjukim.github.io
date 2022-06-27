# 모든 음식 스코빌 지수 K 이상으로
# 스코빌 지수 가장 낮은 두개의 음식을 섞어 새로운 음식
# 섞 = 가장 안매운 + (두번쨰로 안매운*2)
# 모든 음식 K 이상일때까지 반복하여 섞기
# 모든 음식 K 이상으로 만들기 위해 섞어야하는 최소 횟수
# k 이상으로 만들 수 없는 경우 -1 반환

def solution(scoville, K):
  answer = 0
  scoville = list(scoville)
  scoville.sort()
  print(scoville)

  if scoville[-1] < K:
    print("scoville[-1]",scoville[-1])
    return -1

  while True:
    scoville.sort()
    if scoville[0] > K:
      break

    min = scoville[0]
    min2 = scoville[1]
    temp = scoville[2:]
    sum =[]
    sum.append(min + min2 * 2)
    scoville = sum + temp
    answer += 1

  print("answer",answer)
  return answer

solution([1, 2, 3, 9, 10, 12],7)
