from collections import deque
def solution(n, computers):
    answer = 0
    v = [0] *(n)
    def dfs(x,c):
        q = deque([x])
        while q:
            n_c = q.popleft()
            for i in range(n):
                if v[i]==0 and computers[n_c][i]==1:
                    q.append(i)
                    v[i] = c
    q = deque([])
    c = 1
    for i in range(n):
        if v[i]==0:
            dfs(i,c)
            c+=1
    return max(v)