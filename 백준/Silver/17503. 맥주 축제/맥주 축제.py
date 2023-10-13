import sys
from heapq import heappush, heappop
input = sys.stdin.readline
n,m,k = map(int,input().strip().split())
# m을 채우면서, n개의 맥주, k의 종류
# k개의 맥주 중에 선호도 레벨 따져서 n개 먹자
# m은 높고, 도수는 낮은 친구들을 먹으면 된다.
# 일단 n개를 채워넣고,
beers = [list(map(int, input().strip().split())) for i in range(k)]
beers = sorted(beers, key = lambda x: (x[1],x[0]))  # 도수 낮은 것부터 알아가기
# print(beers)

# 선호도, 도수
heap=[]
prefer = 0
answer = -1
for beer in beers:
    # print(heap, prefer)
    heappush(heap, beer)
    prefer += beer[0]  # 먼저 먹어
    if len(heap) == n:
        if prefer>=m:
            answer = beer[1]  # 안채우고, answer 반환
            break
        else:
            prefer -= heappop(heap)[0]

print(answer)