#
def Contact(arr):
  # print("arr : ",arr)
  if len(arr) == 0:#문자열의 길이가 null이면
    return print("YES")

  if arr[0:2] == '01':
     arr = arr[2:]
     Contact(arr)

  elif arr[0:3] == '100':
      arr = arr[3:]
      if arr[0] =="1":
        if "0" in arr:
          arr = arr[arr.find("0"):]
          Contact(arr)
        else:
          return print("YES")

      else:#0으로 시작하면
        if "1" in arr:#1이 있나 확인
          while True:
            if arr[0] == "0":
              arr = arr[1:]
            else:
              if "0" in arr:
                arr = arr[arr.find("0"):]
                Contact(arr)
                break
              else:
                return print("YES")
        else:
          return print("NO")

  else:
    return print("NO")

T = int(input())
t_str = []
for i in range(T):
  temp = input()
  t_str.append(temp)

for i in t_str:
  Contact(i)