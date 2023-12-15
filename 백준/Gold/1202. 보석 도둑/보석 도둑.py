import sys
import heapq as hq
input = sys.stdin.readline

n,k = map(int,input().strip().split())
result = 0   # 최대 가격
jus = []
bags = []

for i in range(n):
    m, v = map(int,input().strip().split())
    hq.heappush(jus, (m,v))

for i in range(k):
    c = int(input())
    bags.append(c)

bags.sort()
tmp = []
for bag in bags:
    while 1:
        if jus and jus[0][0] <= bag:
            hq.heappush(tmp,-hq.heappop(jus)[1])
        else:
            break
    if tmp:
        result -= hq.heappop(tmp)

print(result)
