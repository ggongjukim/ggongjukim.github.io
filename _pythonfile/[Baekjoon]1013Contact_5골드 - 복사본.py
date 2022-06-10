# 무한히 넓은 저 우주에 인류만이 홀로 존재한다면, 그건 정말 슬픈일 아닐까요

#전파의 기본 단위 0,1
#x+()는 임의의 개수 x의 반복으로 이루어진 전파의 집합을 나타낸다.
#(xyx)+()는 괄호 내의 xyx 반복으로 이루어진 전파의 집합

#(100+1+|01)+패턴을 지니는 프로그램

#입력
#테스트 케이스의 수 T
#테스트 케이스 문자열
#

def Contact(arr):
  while len(arr) > 0:
    print(arr)
    if arr[0:2] == '01':
      arr = arr[2:]

    elif arr[0:3] == '100':
        arr = arr[3:]
        print(arr)
        if arr[0] =="1":#100 1...
          if "0" not in arr: #100 111111111...
            print("YES")
            break
          else:# 어딘가에 0이 있음
            if arr[1] == "1" : # 1이 두개 이상일 경우
              arr = arr[arr.find("0")-1:]
              if arr[0:3] =="100":
                continue
              else:
                arr = arr[1:]
                continue
            else: #1이 하나임
              arr = arr[1:]
              continue


        else:#0일때
          if "1" not in arr:
            print("NO")
            break
          else:#100 0.. 1..
            # print(arr)
            arr = arr[arr.find("1"):]
            # print(arr)
            if "0" not in arr:
              print("YES")
              break
            else:
              if arr[1] == "1": # 1이 두개 이상일 경우
                arr = arr[arr.find("0") - 1:]
                if arr[0:3] == "100":
                  continue
                else:
                  arr = arr[1:]
                  continue
              else:  # 1이 하나임
                arr = arr[1:]
                continue


    else:
      print("NO")
      break

import sys
T = int(sys.stdin.readline())
t_str = []
for i in range(T):
  temp = sys.stdin.readline()
  t_str.append(temp)

for i in t_str:
  Contact(i)
