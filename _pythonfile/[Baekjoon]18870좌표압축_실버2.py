#문제
#수직선 위해 N개 좌표있다.
#좌표 압축을 하려한다
#좌표 압축 xi-> x'i
#xi>xj를 만족하는 서로다른 좌표의 개수와 같아야함
#압축한 좌표 결과를 출력하라

#입력
#첫줄 N
#둘째줄 공백한칸으로 구분된 x1,x2,x3...xN 주어짐

#출력
#x'1,x'2,x'3... x'N을 공백한 칸으로 구분하여 출력

#주의할점 같은 수 반복

# N=int(input())
# li = list(map(int,input().split()))
# li2 = li[:]
# dic ={}
# li2.sort()
# # print(li2)
# smaller = 0
# min = li2[0]
# for i in range(len(li2)):
#   if li2[i] > min:
#     smaller+=1
#     min = li2[i]
#   dic[li2[i]] = smaller
# # print(dic)
# for i in li:
#   print(dic[i],end=' ')

#다른 사람 풀이 좋은뎅?
from sys import stdin

n = int(stdin.readline())

li = list(map(int, stdin.readline().split()))

li_s = sorted(set(li))
print(li_s)

dic = {li_s[i] : i for i in range(len(li_s))}
print(dic)

for i in li:
    print(dic[i], end=" ")

