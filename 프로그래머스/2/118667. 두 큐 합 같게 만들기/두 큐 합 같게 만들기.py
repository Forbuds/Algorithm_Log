from collections import deque
def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    cnt = 0
    s1,s2 = sum(q1),sum(q2)
    total = s1+s2
    limit = len(q1+q2)*2
    # print(q1+q2)
    if total%2==1:
        return -1
    elif (total//2  < max(q1+q2)):
        return -1
    
    while 1:
        if cnt >= limit:
            return -1
        if s1 == s2:
            print(cnt)
            break
        else:
            if s1<s2:
                pop = q2.popleft()
                s2 -= pop
                s1 += pop
                q1.append(pop)
            else:
                pop = q1.popleft()
                s1 -= pop
                s2 += pop
                q2.append(pop)
            if s1==0 or s2==0:
                return -1
            cnt +=1
            
    return cnt