# 백준 1181번 단어 정렬

# 1.
# 단어의 알파벳순서로 정렬후에 문자의 길이가 50을 넘지 않는다고 했기때문에 1부터 50까지 반복하면서 출력
# 실행시간 4760ms
n = int(input())
s = []

for i in range(n):
    text = input()
    if text not in s:
        s.append(text)

s.sort()

for i in range(1, 51):
    for j in s:
        if len(j) == i:
            print(j)


# 2. 
# 구글링을 통해 길이로 sort하는것을 알게되었다.
# 실행시간 4328ms(실행시간에는 별 차이가 없었다.)
n = int(input())
s = []

for i in range(n):
    text = input()
    if text not in s:
        s.append(text)

s.sort()
# key를 활용해 길이로 정렬도 한다는것을 알게됨
s.sort(key=len)
for i in s:
    print(i)


# 3.
# 람다를 통해 정렬
# 실행시간 7800ms(두번째 방법이랑 비슷한데 함다함수까지 껴있어서 가장 오래걸렸다.)
n = int(input())
s = []

# 리스트에 문자의 길이까지 함께넣어서 정렬
for i in range(n):
    text = input()
    if [len(text),text] not in s:
        s.append([len(text),text])

s.sort(key=lambda x:x[1])
s.sort(key=lambda x:x[0])
for i in s:
    print(i[1])