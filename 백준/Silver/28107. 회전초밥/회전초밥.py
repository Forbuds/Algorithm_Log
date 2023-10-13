# 손님 n 명, M개 초밥
# 개수, 주문목록(종류)
# 핵심: 초밥을 우선순위 큐로 만든다!
# 항상 손님이 우선순위 큐라는 편견을 버릴 것.

from heapq import heappush, heappop, heapify
n,m = map( int, input().strip().split())
arr =[[] for i in range(200000+1)]      # 초밥을 []로 때려 넣는다.
for i in range(n):
    k,*items = map( int, input().strip().split())    # map 이렇게도 쓴다.
    for item in items:
        heappush(arr[item],i)          # 초밥 종류에다가 (arr[종류번호]) 사람 번호(i) 를 우선순위 큐로 때려넣기
sushis = list(map( int, input().strip().split()))
members = [0]*n
for sushi in sushis:
    if arr[sushi]:
        members[heappop(arr[sushi])] += 1
    else:
        pass
print(' '.join(map(str,members)))