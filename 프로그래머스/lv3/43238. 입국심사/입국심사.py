def solution(n, times):
    answer = 0
    
    # 심사를 받는 데 걸리는 시간이 answer
    s  = 1
    e = max(times)*n
    res = e
    people = 0
    
    while s<=e:
        mid = (s+e)//2
        people = 0
        for t in times:
            people += mid//t
        if people >= n:  # 시간이 넉넉
            e = mid -1
            res = min(res,mid)
        else:
            s = mid +1
            
    
    return res



# mid는 심사를 받는 데에 걸리는 시간
# mid안에 진짜로 몇명이나 검사받을 수 있는데?
# 각 타임 mid/타임