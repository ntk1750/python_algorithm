#인출하는데 총 걸리는 시간
#줄을 서 있는 사람의 수 N, 돈을 인출하는데 걸리는 시간 Pi
#각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값

N = int(input())
pi =list(map(int, input().split())) 
pi.sort() #오름차순 정렬
sum = 0
total = 0
for i in pi:
    sum+=i
    total +=sum

print(total)