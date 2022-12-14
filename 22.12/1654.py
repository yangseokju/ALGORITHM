# 백준 1654번 랜선 자르기

# 이진검색 : 오름차순으로 정렬된 리스트에서 특정한 값의 위치를 찾는 알고리즘
# 처음 중간의 값을 임의의 값으로 선택하여, 그 값과 찾고자 하는 값의 크고 작음을 비교하는 방식
# def binarySearch(array, value, low, high):
# 	if low > high:
# 		return False
# 	mid = (low+high) / 2
# 	if array[mid] > value:
# 		return binarySearch(array, value, low, mid-1)
# 	elif array[mid] < value:
# 		return binarySearch(array, value, mid+1, high)
# 	else:
# 		return mid

k, n = map(int, input().split())
s = []

for i in range(k):
    s.append(int(input()))
s.sort()

low = 1 # 답이 될수있는 가장 최소의 값
high = s[-1] # 답이 될수있는 가장 최대의 값

# 가장 큰값이 나올때까지 반복 
while low <= high:
    mid = (low + high) // 2
    check = 0
    for i in s:
        check += i//mid

    # 중간값인 mid보다 커야하면 low에 mid + 1
    # 작아야하면 high에 mid - 1을 반복
    if check >= n:
        low = mid + 1
    else:
        high = mid - 1

# 가장 큰 값을 출력해야 하므로 반복하면서 탈출된 마지막값을 출력
# check 와 n이 같을때의 값을 출력하면 안된다.(최대값이 안나올수도 있음.)
print(high)