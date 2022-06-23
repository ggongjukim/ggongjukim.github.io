#문제
#단어에서 가장 많이 사용된 알파벳 찾으세용
#대소문자 구분 없음

#질문
#파이썬은 대소문자를 구별하는가?
#구분함
#일단 다 소문자로 바꿔야 겠군

#입력
#단어

#출력
#가장 많이 사용된 알파펫을 대문자로 출력
#여러개 존재하면 ?를 출력

#발상
#문자열을 리스트로 해가지구 딕셔너리로 해야하지 않으깡? 아니면 자동으로 계산해주는 거 잇나?

# N = list(input().upper())
# print(N)
# dic = {}
# for i in N:
#   try:
#     dic[i] += 1
#   except:
#     dic[i] = 1
#
# print(dic)
# #키밸류 위치바꿈
# # dic = {v:k for k,v in dic.items()}
#
# #딕셔너리 키로 정렬
# sort_dic = sorted(dic.items(), key = lambda item: item[1], reverse = True)
# print(sort_dic[0][0])
#
# if sort_dic[0][1] != sort_dic[1][1]:
#   print(sort_dic[0][0])
# else:
#   print("?")

# 주의!
# 문자열이 하나일때도 생각을 했어야함

N = list(input().upper())

dic = {}
for i in N:
  try:
    dic[i] += 1
  except:
    dic[i] = 1


#딕셔너리 키로 정렬
sort_dic = sorted(dic.items(), key = lambda item: item[1], reverse = True)
if len(sort_dic)>1:
  if sort_dic[0][1] != sort_dic[1][1]:
    print(sort_dic[0][0])
  else:
    print("?")
else:
  print(N[0])