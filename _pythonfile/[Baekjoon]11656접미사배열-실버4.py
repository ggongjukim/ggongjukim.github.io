#접미사 배열은 문자열 S의 모든 접미사를 사전순으로 정렬
#baekjoon의 접미사는

#발상
#스택으로 하면 되지 않을깡
from collections import deque
S = list(input())
stack = []
misa =[]

for i in range(len(S)-1,-1,-1):
  stack.append(S[i])
  print(stack)
  misa.append(''.join(stack[::-1]))
print(misa)
misa.sort()
print(misa)

for i in misa:
  print(i)




# ##다른사람 풀이 - 읭 이게 더 쉽자낭?

# s = input()
#
# anw = []
#
# for i in range(len(s)):
#     anw.append(s[i:])
#
# anw.sort()
#
# for i in anw:
#     print(i)