---
title : "[프로그래머스]오픈채팅방"
layout: single
categories : Algorithm
tag : [python, python3]
toc : true
---
### | 문제
오픈 채팅방에 본래 닉네임이 아닌 가상 닉네임을 사용하여 입장할 수 있다.
관리자창에서 채팅방에 나가고 들어오는 메세지를 문자열 배열형태로 return

### | 입력
오픈채팅방에 들어오거나 나간것, 혹은 닉네임 변경기록이 record 배열로 주어짐  
Enter [유저 아이디] [닉네임]  

### | 출력
관리자창에서 보여지는 최종 문자열 배열

### | 예시

|**record**|**result**|
|---|---|
|["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]| ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]|


### | 발상
- 이벤트는 Enter, Leave, Change 이 세가지만 존재
- 딕셔너리를 써서 key는 유저 ID value는 가상닉네임으로 


### | 풀이

``` python
def solution(record):
  answer = []
  dic ={}
  result =[]
    
# 전처리    
  for i in range(0,len(record)):
    temp = record[i].split(' ')
    record[i] = temp # 배열로 다 짤라버림

# dic 만들기 enter와 change
  for i in record:
    if i[0] =='Enter':
      dic[i[1]] = i[2]# dic key 생성
      answer.append([i[1],'님이 들어왔습니다.'])# 진짜 id로 일단 기록을 남김
    elif i[0] =='Change':
      dic[i[1]] = i[2]# 바꾸기
    else:
      answer.append([i[1],'님이 나갔습니다.'])

)

  for i in range(0,len(answer)):
    result.append(dic[answer[i][0]]+answer[i][1])#answer[i][0]으로 dic에서 진짜 id로 value값 찾아서 넣음
  return result

```

### | 소감 및 팁
- 뭔가 한번에 하려는 시도보다는 전처리- 중간 - 마무리 이런식으로 하는게 더 나을 때가 많다