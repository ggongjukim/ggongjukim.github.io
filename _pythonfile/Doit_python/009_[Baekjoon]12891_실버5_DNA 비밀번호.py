# 이중 반복문 아니고 => 상태 업데이트에 따라 count 를 올려줘야함
s, p = map(int, input().split())
DNA = input()
a, c, g, t = map(int, input().split())
start, end = [0, p - 1]
result = {"A": 0, "C": 0, "G": 0, "T": 0}
count = 0

# 처음 상태 초기화 a c g t 개수 세기
for i in DNA[start:end + 1]:
  result[i] += 1
# 조건 검사
if result['A'] < a or result['C'] < c or result['G'] < g or result['T'] < t:
  pass
else:
  count += 1
# 상태 업데이트
result[DNA[start]] -= 1
start += 1
end += 1

while end < len(DNA):
  # 상태 업데이트
  result[DNA[end]] += 1
  # 조건 검사
if result['A'] < a or result['C'] < c or result['G'] < g or result['T'] < t:
  pass
else:
  count += 1

result[DNA[start]] -= 1
start += 1
end += 1

print(count)