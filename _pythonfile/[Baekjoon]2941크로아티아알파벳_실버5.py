# 문자열
# 주어진 문자열이 크로아티어 몇글자인지 찾기

#c= c- dz= d- li nj s=

N = list(input())
count = 0
cro = ['c=','c-','dz=', 'd-','lj','nj','s=','z=']
while N:
  i=0
  temp = N[i:i+2]
  temp = ''.join(temp)
  temp2 = N[i:i+3]
  temp2 = ''.join(temp2)
  # print(temp, temp2)

  if temp in cro:
    count+=1
    N = N[i+2:]
  elif temp2 in cro:
    count+=1
    N = N[i+3:]
  else:
    count+=1
    N = N[i+1:]
  # print('count',count,'result',N)

print(count)

# 다른 사람 풀이
# croatia_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# word = input()
#
# for i in croatia_alphabet:
#     word = word.replace(i, 'a')
#
# print(len(word))
