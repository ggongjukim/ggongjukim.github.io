## 코테 알고리즘 공부

|문자열||
|---|---|
|기본 수학| |
|재귀| |
|브루트포스 = 완전탐색| |
|정렬| |
|백트래킹| |
|동적계획법 DP = Dynamic Programming| |
|그리디 = 탐욕법| |
|구현| |
|큐/덱| |
|분할정복 = 퀵 정렬| |
|이분탐색| |
|DFS/BFS| |
|트리||

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

## 문자열에서 특정 문자열 개수 세기
- 리스트 or 문자열.count("찾으려는 문자열")

## 모든 문자를 대문자로 하려면
- 문자열.upper()

## 파이썬 리스트 swap-  바꾸기
li = [3,5]
li[0], li[1] = li[1],li[0]

## 리스트 -> 문자열
- ''.join(리스트)
- 문자열.spilt(',') => ,로 나누기

## 리스트 정렬
- 리스트.sort()
- 리스트.sort(key = len) => 리스트 원소의 길이에 따라 오름차순으로 목록 정렬
- 리스트[::-1] =>역순으로 출력


### 문자 제거법
https://codechacha.com/ko/python-string-strip/
양쪽 공백 제거 .strip()
왼쪽 공백 제거 .lstrip()
오른쪽 공백 제거 .rstrip()
()안에 문자를 넣으면 해당 문자를 제거하도록 한다

## 리스트 회전
- deque를 써야함
- 리스트.rotate(-1) 역으로 한칸회전
- 이차원 리스트도 가능함


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
### set을 리스트로

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