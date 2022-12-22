# 백준 1978번 소수 찾기
# 에라토스테네스의 체

n = int(input())
s = list(map(int, input().split()))
result = 0

# 최대값 길이만큼의 리스트를 만들어 모두 True로 설정(모두 소수라고 표시)
arr = [True] * (max(s)+1)
for i in range(2, max(s)):
    # 만약 i번이 소수라면
    if arr[i]:
        # 그 배수들은 소수가 아니라고 표시한다.
        for j in range(i+i, max(s)+1, i):
            arr[j] = False

# 주어진 숫자가 1이 아닐때(1은 소수가 아니기 때문에)
# True이면(소수이면) 결과값 result에 +1 한다.
for k in s:
    if k != 1 and arr[k] == True:
        result += 1

print(result)