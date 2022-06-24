## 입력 출력
- 프로그래머스이면 신경쓰지 않아도됨
- input() 이런걸 생각하지 않아도됨 다 자동으로 입력 출력이됨
- return에 잘 맞추어 출력만 신경쓰면됨
- 그러나 반복문으로 여러줄 입력받는 상황에서는 반드시 sys.stdin.readline()을 사용해야 시간초과가 발생하지 않습니다.
## 문자열 -> 리스트
- list(문자열)

## max()에서 같은게 있으면 어떻게 되나용?

## 모든 문자를 소문자로하려면
- 문자열.lower()

## 모든 문자를 대문자로 하려면
- 문자열.upper()

## 리스트 -> 문자열
- ''.join(리스트)
- 문자열.spilt(',') => ,로 나누기

## 리스트 정렬
- 리스트.sort()
- 리스트.sort(key = len) => 리스트 원소의 길이에 따라 오름차순으로 목록 정렬
- 리스트[::-1] =>역순으로 출력

##인덱스 원소 동시 접근
- for a,b in enumerate(리스트)
- 키벨류스위치할딕셔너리 = {v:k for k,v in enumerate(딕셔너리 or 리스트)} => 키밸류 바꾸기 => 안되는데?
- {v:k for k,v in di.items()}

## 딕셔너리 정렬
### value로 정렬 => 튜플로됨
sorted_dict = sorted(my_dict.items(), key = lambda item: item[1])
sorted_dict = sorted(my_dict.items(), key = lambda item: item[1], reverse = True) =>내림차순

##딕셔너리
- 딕셔너리.get('키')
- 밸류로 키찾기
  - [k for k, v in aa.items() if v == 'CC']
  
##순열 - 순서가 있는 조합 ab != ba
* [방법1]
- from itertools import permutations => 앞에 선언
- permutation(리스트 or 튜플 or 문자열, 몇개뽑을건지) => 튜플로 출력
- list(permution(리스트 or 튜플 or 문자열, 몇개뽑을건지)) => 이런식으로 쓰면됨
- 출력하여 보고싶을때 , 다시 튜플을 문자열로 붙이려면 
  ```python
  for i in temp:
    candidate.append(''.join(i))
  ```


* [방법2]
-  

##조합 - 순서가 없는 조합 ab == ba
- from itertools import combinations => 앞에 선언
- combinations(리스트 or 튜플 or 문자열, 몇개뽑을건지) => 튜플로 출력

##두개이상의 리스트에서 모든 조합 구하기
- product

##리스트 중복제거
- set(리스트) =>set 
- list(set(리스트)) => 리스트

## popleft
- 리스트[0] 제거
- 맨 왼쪽값 가져오고 제거

## appendleft
- 리스트[0]에 추가

##참고 코드
import sys
input = sys.stdin.readline
N = int(input())
board =[]
for i in range(N):
  board.append(list(map(int,input().split())))
visit = [[0]*N for _ in ragne(N)]
queue = [[0,0]]