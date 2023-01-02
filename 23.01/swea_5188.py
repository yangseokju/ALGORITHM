# swea 5188번 최소합

# 첫번째 방법
# bfs로 하나씩 값을 다 돌아보면서 최소값을 찾는다
T = int(input())

di = [0, 1]
dj = [1, 0]

def cal(a, b, sum):
    global result
    if result < sum:
        return
    if a == n-1 and b == n-1 and result > sum:
        result = sum
    for i in range(2):
        ni = a + di[i]
        nj = b + dj[i]
        if 0 <= ni < n and 0 <= nj < n:
            cal(ni, nj, sum + arr[ni][nj])


for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = 1000000000
    cal(0, 0, arr[0][0])

    print(f'#{tc} {result}')


# 두번째 방법
# dp로 값을 저장해두면서 최소값을 찾는다
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 중간까지의 합을 다시 계산하지 않도록 기억해놓는 방법을 사용
    dp = [[0]*N for _ in range(N)]

    # 이동방향이 왼쪽 -> 오른쪽, 위 -> 아래
    for i in range(N):
        for j in range(N):
            # 현재 i, j 위치에서 위에서도 올수 있고, 왼쪽에서도 올수있다면
            if i-1 >=0 and j-1 >=0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + arr[i][j]
            # 위에서만 올수 있고, 왼쪽에서는 올수 없다.
            elif i-1>=0 and j-1<0:
                dp[i][j] = dp[i-1][j] + arr[i][j]
            # 왼쪽에서만 올수 있고, 위에서는 올수 없다.
            elif i-1 <0 and j-1 >=0:
                dp[i][j] = dp[i][j-1] + arr[i][j]
            elif i-1 <0 and j-1 <0:
                dp[i][j] = arr[i][j]
    # 반복이 다 끝나면 맨 오른쪽 아래칸에는 최소값이 들어 있을 것이다.
    print(f'#{tc} {dp[N-1][N-1]}')