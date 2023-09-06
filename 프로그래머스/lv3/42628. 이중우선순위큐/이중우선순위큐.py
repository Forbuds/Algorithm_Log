import heapq
def solution(operations):
    h_m = []
    h_x = []
    for o in operations:
        o, n = o.split(' ')
        if o=='I':
            n = int(n)
            heapq.heappush(h_m, n)
            heapq.heappush(h_x, -1*n)
                           
        else:
            # print(h_m,h_x)
            if len(h_m)==0 or len(h_x)==0 :
                pass
            else:
                if n=='1':
                    # 최댓값 삭제
                    h_m.remove(-1*heapq.heappop(h_x))
                else:
                    # 최솟값 삭제
                    h_x.remove(-1*heapq.heappop(h_m))
    
    if len(h_m) == 0:
        return [0,0]
    else: # 남아있으면
        return [-1*heapq.heappop(h_x),heapq.heappop(h_m)]
