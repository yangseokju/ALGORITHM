# 백준 10250번 ACM 호텔
# 반례를 못찾아서 조금 오래걸렸다..

T = int(input())
for tc in range(1, T+1):
    h, w, n = map(int, input().split())
    floor = n%h # 층수
    room = n//h + 1 # 방번호
    if floor == 0:
        room -= 1
        floor = h
    print(floor*100+room)