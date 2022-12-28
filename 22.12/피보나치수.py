# 프로그래머스 피보나치 수

# 첫번째 풀이
# 그냥 메모이제이션으로 풀었을때 시간초과랑 런타임에러가 났다.
# 재귀의 호출 깊이를 늘려줘서 문제를 해결하였다.
# 동적프로그래밍 문제를 풀때 중요한 개념이기 때문에 기억해놔야겠다.
import sys
sys.setrecursionlimit(10 ** 6)

def solution(n):
    global memo
    if n >= 2 and len(memo) <= n:
        memo.append((solution(n-1) + solution(n-2))%1234567)
    return memo[n]

# 다른사람의 풀이
# 다른사람의 풀이를 봤는데 파이썬의 특징을 잘 살려서 풀었다.
# 시간도 내가풀었던 메모이제이션 방법보다 훨씬 빠르고, 메모리 사용도 적었다.
memo = [0, 1]
def solution(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,(a+b)%1234567
    return a