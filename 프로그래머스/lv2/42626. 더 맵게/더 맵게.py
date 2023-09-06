import heapq
def solution(scoville, K):
    answer = 0
    # 가장 작은거 순차로 뺌 -> 최소 힙, 최대 힙 문제
    # 만들자마자 K이상인지 확인후 return
    h = []
    for x in scoville:
        heapq.heappush(h,x)
        
    while True:
        if len(h)==1:
            if heapq.heappop(h)<K:
                return -1
            else:
                return answer
        
        v1 = heapq.heappop(h)
        v2 = heapq.heappop(h)
        # print(v1,v2)
        if v1 >=K:
            return answer
        
        result = v1 + 2*v2
        heapq.heappush(h,result)
        answer+=1
        
    
    return answer