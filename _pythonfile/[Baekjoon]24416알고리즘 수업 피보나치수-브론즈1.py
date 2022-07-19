# 재귀 피보나치
countfin = 0
countfibo = 0

def fin(n):
  global countfin
  if n ==1 or n==2:
    countfin += 1
    return 1
  else:
    return fin(n-1) + fin(n-2)


N = int(input())
f = [0]*(N+1)
f[1] = 1
f[2] = 1
def fibonacci(n):
  global countfibo
  for i in range(3, n+1):
    countfibo += 1
    f[i] = f[i-1] + f[i-2]
  return f[n]

fin(N)
fibonacci(N)

print(countfin, countfibo)

## 그냥 python은 시간 초과됨
# 다른사람 풀이
# def fibonacci(n):
#   f = [0] * n
#   f[0], f[1] = 1, 1
#   for i in range(2, n):
#     f[i] = f[i - 1] + f[i - 2]
#   return f[n - 1]
#
#
# if __name__ == "__main__":
#   n = int(input())
#   fib1 = fibonacci(n)
#   fib2 = n - 2
#   print(fib1, fib2)

# #다른 풀이2
# n = int(input())
# f = [0]*40
# f[0] = f[1] = 1
# count = 0
# for i in range(2, n):
#     count += 1
#     f[i] = f[i-1] + f[i-2]
#
# print("{} {}".format(f[n-1], count))