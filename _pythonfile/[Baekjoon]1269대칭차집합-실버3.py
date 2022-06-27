#문제
#자연수 원소인 집합 A,B 공집합 아님
# 두집합의 대칭 차집합 원소의 개수를 출력

# 입력
# A의 원소 개수 , B원소 개수
# 둘쨰줄 집합 A의 모든 원소
# 셋째줄 집합 B의 모든 원소

A,B = list(map(int,input().split()))
Alist =list(map(int,input().split()))
Blist = list(map(int,input().split()))

A_B = set(Alist)-set(Blist)
B_A = set(Blist)-set(Alist)
result = A_B | B_A
print(len(result))