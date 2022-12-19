# 백준 11048번 이동하기
# bfs로 시도하다가 시간초과로 여러번 실패 후 검색해서 dp로 푸는 방법을 찾았다..
# 풀이도 훨씬 간단하고 시간복잡도도 더 빠른 방법인것 같다..

# 1. 
# bfs 풀이

# import sys
# sys.setrecursionlimit(10**6)
#
# di = [0, 1]
# dj = [1, 0]
#
#
# def cal(i, j):
#     q = []
#     v = [[0] * m for _ in range(n)]
#     q.append((i, j))
#     v[i][j] = arr[i][j]
#     while q:
#         a, b = q.pop(0)
#         for i in range(2):
#             ni = a + di[i]
#             nj = b + dj[i]
#             if 0 <= ni < n and 0 <= nj < m and v[ni][nj] <= v[a][b] + arr[ni][nj]:
#                 q.append((ni, nj))
#                 v[ni][nj] = v[a][b] + arr[ni][nj]
#     print(v[-1][-1])
#     return
#
#
# n, m = map(int, sys.stdin.readline().split())
# arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
#
# cal(0, 0)

# 2.
# dp 풀이(메모이제이션)
import sys
sys.setrecursionlimit(100000)
n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+arr[i-1][j-1]
print(dp[n][m])