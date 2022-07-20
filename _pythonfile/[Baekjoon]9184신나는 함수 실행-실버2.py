# w 재귀함수를 오랜시간이 걸리지 않도록
# 똑같은 출력이 되는 함수 짜기
wdic = {}
count = 0


def w(a,b,c):
  global count
  count +=1
  #print('wdic.keys()',wdic,count)

  # if (a,b,c) in wdic.keys():#wdic.get([a,b,c]) != None:
  #   # print(wdic[(a,b,c)],"있음")
  #   return wdic[(a,b,c)]

  if a <=0 or b <= 0 or c <= 0 :
    #print("1번",a,b,c)
    wdic[a,b,c] = 1
    return 1
  else:
    if (a, b, c) in wdic.keys():  # wdic.get([a,b,c]) != None:
      # print(wdic[(a,b,c)],"있음")
      #print("2번",a,b,c)
      return wdic[(a, b, c)]

  if a >20 or b > 20 or c >20:
    #print("3번",a,b,c)
    return w(20,20,20)

  if a<b and b<c: #c 가 제일 크다
    #print("4번",a,b,c)
    wdic[(a, b, c)] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    return w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

  else:
    #print("5번", a,b,c)
    wdic[(a, b, c)] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
    return wdic[(a, b, c)]


while True:
  a,b,c = list(map(int,input().split(' ')))

  if a == -1 and b == -1 and c ==-1 :
    break
  count = 0
  print("w("+str(a)+", "+str(b)+", "+str(c)+") =" ,w(a,b,c))
  #print("끝",wdic)
