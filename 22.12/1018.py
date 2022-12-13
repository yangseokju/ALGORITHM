# 백준 1018번 체스판 다시 칠하기

N, M = map(int, input().split())
arr = []
min_result = 64 # 나올수있는 최댓값을 최소 결과로 지정
check = ['B', 'W'] # 나올수있는 색상 두가지

for i in range(N):
    arr.append(list(input()))

# a : 행에 더해줄 값, b : 열에 더해줄 값, c : 색상의 인덱스 값
a, b, c = 0, -1, 0
while True:
    result = 0
    b += 1
    # 기준점에서 행이나 열 방향으로 8칸을 이동했을때 벗어난다면 break
    if b == M - 7:
        b = 0
        a += 1
        if a == N - 7:
            break
    # 일단 색상이 같으면 결과값에 더해준 후에 연산이 끝난 후 64에서 빼준다.
    for i in range(8):
        c += 1
        c %= 2
        for j in range(8):
            c += 1
            c %= 2
            if arr[a + i][b + j] == check[c]:
                result += 1
    if result > 32:
        result = 64 - result
    # 최소값 판별
    if min_result > result:
        min_result = result
print(min_result)