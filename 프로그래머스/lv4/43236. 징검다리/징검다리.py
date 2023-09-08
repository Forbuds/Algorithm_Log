import heapq
def solution(distance, rocks, n):
    answer = 0
    rocks.extend([0,distance])
    rocks = sorted(rocks)
    # 바위 제거 위치
    # rocks = [rocks[i+1]-rocks[i] for i in range(len(rocks)-1)]
    def calc(rocks,k):
        current,remove = 0,0
        for i in range(1,len(rocks)):
            if rocks[i] - current < k:
                remove +=1
            else:
                current  = rocks[i]
        return remove
    
    s = 1
    e = distance
    answer = distance
    
    while s<=e:
        mid = (s+e)//2
        
        if calc(rocks,mid) <= n:  # 더 많이 제거한다면, 기준값을 낮춰야 함
            s = mid +1
            answer = mid
        else:
            e = mid -1
    
    
    return answer