from collections import deque
def solution(numbers, target):
    answer = 0
    
    q = deque([[numbers[0],0], [-1*numbers[0],0]] )
    print(q)

    tmp = 0
    
    while q:
        x, idx = q.popleft()
        if idx == len(numbers)-1:
            if x == target:
                answer+=1
        else:
            q.append([x + numbers[idx+1], idx+1 ])
            q.append([x - numbers[idx+1], idx+1 ])
    
    
    return answer