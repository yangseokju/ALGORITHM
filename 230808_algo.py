# 백준 9095번  1, 2, 3 더하기
t = int(input())

for k in range(t):
    n = int(input())

    result = [0] * 11

    result[0] = 1
    result[1] = 2
    result[2] = 4

    for i in range(3, 11):
        result[i] = result[i-3] + result[i-2] + result[i-1]
    
    print(result[n-1])