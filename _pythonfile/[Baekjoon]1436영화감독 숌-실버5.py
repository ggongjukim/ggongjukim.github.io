#666은 종말을 나타내는 숫자
#영화감독 숌을 세상의 종말이라는 시리즈 영화의 감독
#종말의 숫자 어떤 수에 6이 적어도 3개 이상 연속
# 666,1666,2666,3666

N = int(input())
start = 1666
count = 1

if N == 1:
  start = 666

else:
  while True:


    if '666' in str(start): #and count == N:
      count += 1
      if count == N:
        break

    start +=1


print(int(start))

# ##다른 풀이
# N = int(input())
# first = 666#처음 666인 수
# while N != 0:# N 이 0이 아니면 계속 반복
#     if '666' in str(first): # 만약 666이란 문자열이 문자열(first)안에 있으면
#         N = N-1# N을 1 감소시키고
#         if N == 0:# 만약 N 이 0이면
#             break# 반복문을 탈출한다.
#     first = first + 1#first의 값을 1 증가시킨다.
# print(first)