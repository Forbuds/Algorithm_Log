from collections import deque
def solution(tickets):
    # 구하고자 하는 것: 공항 경로
    # 조건: 항공권은 모두 사용하기
    # 경로 여러개라면 알파벳 순서 먼저인 경로를 return
    answer = []
    hash = {}
    for s,e in tickets:
        hash[s] = hash.get(s,[])+[e]
    for x in hash:
        hash[x].sort(reverse = True)
    # print(hash)
    q = ["ICN"]
    path = []
    
    while q:
        x = q[-1]
        # print(q,path,hash.get(x,False))
        if not hash.get(x,False) or len(hash[x])==0:  # 마지막이면 path에 담자
            path.append(q.pop())
        
        else:
            q.append(hash[x].pop())
    
    return path[::-1]