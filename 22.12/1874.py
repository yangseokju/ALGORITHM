# 백준 1874번 스택 수열

n = int(input())
arr = [i for i in range(1, n+1)]
s = [] # 입력받은 숫자
result1 = [] # 숫자를 담을 스택
result2 = [] # 결과값을 담을 리스트

for i in range(n):
    s.append(int(input()))

k = 0
while k != n:
    if len(arr) != 0:
        for i in arr:
            # 일단 스택에 순차적으로 숫자를 넣고 push(+)를 넣는다.
            result1.append(i)
            result2.append('+')
            # 스택의 길이가 0보다 크고, 스택의 마지막 값이 입력받은 숫자순서와 같은동안 
            while len(result1) > 0 and result1[-1] == s[k]:
                # 스택의 마지막숫자 빼기 + 결과에 pop(-) 넣기
                result1.pop()
                result2.append('-')
                k += 1
                if k == n:
                    break
            if k == n:
                break
    # 모두 순회를 마치고 탈출했다면 결과 출력
    if k == n and len(result1) == 0:
        for r in result2:
            print(r)
    # 아니면 'NO' 출력
    else:
        print('NO')
        break