#문제
# 그룹단어란 단어에 존재하는 문자에 대해서 각 문자가 연속해서 나타나는 경우
# ccazzzzbb cabz가 연속해서 나타나기 때문에 그룹단어
# kin도 연속해서 나타나기 때문에 그룹단어
# aabbbccb는 b가 떨어져서 나타나기 때문에 그룹단어가 아니다
# 단어 N개 입력받아 그룹단어의 개수를 출력하는 프로그램

# 입력
# 첫줄에 단어 개수 N
# 0 < N <= 100
# 둘쨰줄 N개의 단어 입력
# 알파벳 소문자로 되어있고 중복 없고 길이는 최대 100

# 발상
# 앞에 나온 숫자가 다시 나오면 안됨
# 딕셔너리로 해서 앞에 나왔던 문자면 count 하지 않는 걸로
import sys
N = int(input())
Nlist = []
count =N
for _ in range(N):
  Nlist.append(list(sys.stdin.readline()))

# print(Nlist)

for i in Nlist:
  dic = {}
  before = i[0]
  dic[i[0]] = 1


  for j in i:
    if j != before :
      # print("dic", dic.keys())
      if j not in dic.keys():
        dic[j] = 1
        before = j
      else:
        # print("그룹 아님")
        count -= 1

        break

print(count)