#동전의 총 종류 N
#동전을 적절히 사용 가치의 합을 K로 만듦
#필요한 동전 개수의 최솟값 구하기

import sys
N,K = map(int, input().split())
coin_list = []
for i in range(N):
    coin_list.append(int(input()))

count = 0
reverse_coin = list(reversed(coin_list))

for i in reverse_coin:
    if i <= K:
        count+=(K//i)
        K = K%i
       
print(count)
