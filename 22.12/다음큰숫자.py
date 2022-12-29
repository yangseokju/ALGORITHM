# 프로그래머스 다음 큰 숫자

# 내 풀이
def solution(n):
    answer1 = two(n) # 처음 주어진 숫자의 1의숫자를 담는다
    while True:
        # 1씩 늘려가면서 1의숫자가 같을때까지 반복한다
        n += 1
        answer2 = two(n)
        if answer1 == answer2:
            break
    return n

# 2진수에서 1의 갯수를 세는 함수
def two(n):
    count = 0
    while n != 0:
        if n%2:
            count += 1
        n //= 2
    return count

# 다른 사람의 풀이
# 파이썬의 bin이라는 2진수구하는 방법으로 1의 갯수를 세어주는 방법
# 실행속도나 메모리 측면에서 내가 만든 함수랑 똑같았다.
def nextBigNumber(n):
    num1 = bin(n).count('1')
    while True:
        n = n + 1
        if num1 == bin(n).count('1'):
            break
    return n