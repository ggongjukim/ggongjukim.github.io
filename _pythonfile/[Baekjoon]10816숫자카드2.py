#숫자카드 N개 ,정수 M개
#정수가 적힌 숫자카드 몇개인지

#입력
#첫줄 : N 숫자카드개수
#둘째줄 : N개의 정수
#셋째줄 : M 확인할 정수 개수
#넷째줄 : M개의 정수

n = int(input())
n_arr = list(map(int, input().split()))
m = int(input())
m_arr = list(map(int, input().split()))
n_dic = {}

n_arr.sort()
before = n_arr[0]
for i in range(0,len(n_arr)):
  try:
    n_dic[n_arr[i]] += 1
  except:
    n_dic[n_arr[i]] = 1


for i in m_arr:
  try:
    print(n_dic[i], end = " ")
  except:
    print(0, end = " ")



