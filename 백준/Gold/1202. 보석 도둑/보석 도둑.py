# 보석담기? https://bio-info.tistory.com/195
import sys
from heapq import heappush,heappop, heapify
input = sys.stdin.readline

n,k = map(int,input().strip().split())
jus = []
bags = []
for i in range(n):
    m, v = map(int,input().strip().split())
    jus.append([m,v])

for i in range(k):
    bags.append(int(input()))
heapify(bags)
heapify(jus)

# 보석은 가격이 높은 순 -> 그 다음엔 무게 순
# 무게 작은 가방 뽑아서 높은 가격부터 돌아본다

tmp = []
result = 0
for _ in range(k):
    bag = heappop(bags)  # 작은거 뽑기
    # print(bag)
    while 1:
        if jus and jus[0][0] <= bag:
            heappush(tmp, -heappop(jus)[1])
        else:
            break
    if tmp:
        result -= heappop(tmp)     # tmp는 새로 비워주고 채우는게 아니라, 갖고 다니면서 누적된다.
print(result)

# for 문으로 bas에서 가방의 무게를 작은 것부터 반복한다. 각 가방의 무게에 대해,
# 그 가방으로 훔칠 수 있는 보석들을 while문을 돌며 최대 힙에 저장한다.
# 보석은 무게로 판단해서 그 중 가장 가치가 높은 것을 빼낸다.
# 의문점: 그리디처럼 풀어도 되는걸까?