# 백준 2609번 최대공약수와 최소공배수
# 유클리드 호제법 사용(2개의 자연수 또는 정식의 최대공약수를 구하는 알고리즘)
a, b = map(int, input().split())

# 최대공약수 구하기
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

# 최소공배수 구하기
def lcm(a, b):
    return a * b // gcd(a, b)

print(gcd(a, b))
print(lcm(a, b))