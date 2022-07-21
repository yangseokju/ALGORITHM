""" #1번
N = int(input())
yak = []

for i in range(1,N+1):
    if N%i==0:
        yak.append(i)
print(*yak) """

""" #2번
list_sum = list(map(int,input().split(',')))
hap = 0

for i in list_sum:
    hap += i
print(hap) """

""" #3번
dict_list_sum = [{'name':'kim','age':12},{'name':'lee','age':4}]
dic_sum = []
a = 0

for i in range(len(dict_list_sum)):
    dic_sum.append(dict_list_sum[i]['age'])
for j in range(len(dic_sum)):
    a += dic_sum[j]
print(a) """

""" #4번
all_list_sum = ([[1],[2,3],[4,5,6],[7,8,9,10]])
new_2 = []
hap = 0

for i in range(len(all_list_sum)):
    for j in range(len(all_list_sum[i])):
        new_2.append(all_list_sum[i][j])
for k in range(len(new_2)):
    hap += new_2[k]
print(hap) """

#5번
def get_secret_word(a):
    b = []
    ascii_dic = {83:'S',115:'s',65:'A',102:'f',89:'Y'}
    return get_secret_word(a)

get_secret_word([83,115,65,102,89])