# 백준 1259번 팰린드롬수
while True:
    s = input()
    i = -1
    # 0을 입력받으면 while문 탈출(input으로 입력받아서 문자열형태)
    if s == '0':
        break
    while True:
        i += 1
        # 중간값까지 모두 확인했을때 yes를 출력
        if i == len(s)//2:
            print('yes')
            break
        # 앞뒤 비교
        if s[i] == s[len(s)-i-1]:
            pass
        # 다르면 no 출력
        else:
            print('no')
            break