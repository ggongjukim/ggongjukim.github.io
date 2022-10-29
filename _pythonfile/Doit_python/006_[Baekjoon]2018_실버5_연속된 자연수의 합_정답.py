# 정답
# 초기 설정을어떻게 하는지가 관건
# 배열을 만들것 없이 할 수 있어야함
# 여기서 합은 start 와 end로 구성
# start와 end의 증감을 고려하고 그에따라 sum 이 결정되는 방식이다
N = int(input())
end = 1
start = 1
sum = 1
count = 1
while end != N:
  # print(start, end , sum, count)
  if sum > N:
    sum -= start
    start+=1

  elif sum < N :
    end += 1
    sum += end
  else :
    count += 1
    end += 1
    sum += end
print(count)

