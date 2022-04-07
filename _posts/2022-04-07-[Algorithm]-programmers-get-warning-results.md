---
title : "[프로그래머스]신고 결과 받기"
layout: single
categories : Algorithm
tag : [python, python3]
toc : true
---
### | 문제
유저는 다른 유저를 신고할 수 있다. 정지 기준 신고횟수 k 이상 신고된 회원은 게시판 이용이 정지되며  
정지 회원을 신고한 유저들에게 메일로 정지 사실을 발송한다.  
유저를 여러 번 신고한 경우 신고 횟수 1회로 처리

### | 입력
이용자 ID가 담긴 문자배열 id_list, 신고한 이용자 ID 정보가 담긴 문자열 배열 report, 정지 기준 신고 횟수 k

### | 출력
정지 회원에 대한 정지 사실 메일을 받은 횟수를 배열로 return

### | 예시

|**id_list**|**report**|**k**|**result**|
|---|---|---|---|
|["muzi", "frodo", "apeach", "neo"]|["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]|2|[2,1,1,0]|
|["con", "ryan"]|["ryan con", "ryan con", "ryan con", "ryan con"]|3|[0,0]|


### | 발상
- 딕셔너리를 사용한다!

### | 풀이

``` python
def solution(id_list, report, k):
    answer = [0]*len(id_list)
    warnning = []
    warned = []
    count = {}

  # report 중복제거
    report = list(set(report))
    # 경고한사람, 경고당한사람 두 배열 나움
    for i in report:
      i = i.split()
      warnning.append(i[0])#신고한사람
      warned.append(i[1])#신고받은사람
    
    # 경고당한사람 횟수 세기
    for i in range(0,len(warned)):
      try: 
        temp =[] 
        temp = count[warned[i]] 
        temp.append(warnning[i])#count 딕셔너리에 key 없으면 except로 해서 key 만들어줌
        count[warned[i]] = temp
      except: 
        temp =[] 
        temp.append(warnning[i])
        count[warned[i]] = temp

    for key,val in count.items():
      if len(val) >= k:
        for i in val:
          answer[id_list.index(i)] += 1 

    return answer

```

### | 소감
- 딕셔너리 사용법 잘 익혀야한다
- try except로 딕셔너리를 채울 수 있다