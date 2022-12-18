# 백준 10816번 숫자 카드2
n = int(input())
s1 = list(map(int, input().split()))
m = int(input())
s2 = list(map(int, input().split()))
s1.sort()

# 딕셔너리를 하나 만들어서 s1을 순회하면서 없다면 1 있으면 +1을 반복
check = {}
for i in s1:
    if i in check:
        check[i] += 1
    else:
        check[i] = 1

# 확인해야할 s2인덱스를 순회하면서 딕셔너리 key값으로 확인해준다.
for j in s2:
    if j in check:
        print(check[j], end=' ')
    else:
        print(0, end = ' ')

# 처음 알고리즘 문제를 배웠을때 풀었던 방식과 똑같은데 
# 그냥 [0]*20000001 이렇게 인덱스를 만들어서 인덱스에 +1 했을때는 시간초과가 났었는데
# 딕셔너리로 푸니까 시간초과가 안났다. 비슷한거 같은데 이게 조금 더 빠른가보다..