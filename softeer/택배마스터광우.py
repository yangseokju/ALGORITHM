import sys
from itertools import permutations

def cal(rail):
    global min_num

    cnt = 0 # 횟수를 나타내는 변수
    idx = -1 # 인덱스를 나타내는 변수
    num = 0 # 저장되는 수를 나타내는 변수

    while cnt != k:
        temp = 0
        cnt += 1
        while temp+rail[(idx+1)%n] <= m:
            idx += 1
            idx %= n
            temp += rail[idx]
        num += temp
    if num < min_num:
        min_num = num


n, m, k = map(int, sys.stdin.readline().split())
# n : 레일의 개수, m : 택배 바구니의 무게, k : 일의 시행 횟수
arr = list(map(int, sys.stdin.readline().split()))
# arr : 택배 레일의 전용 무게

min_num = 1000000
rail_arr = list(permutations(arr, n))
for rail in rail_arr:
    cal(rail)

print(min_num)