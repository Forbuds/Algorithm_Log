import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
g = []
for i in range(n):
    g.append(list(map(int,list(input().strip()))))
v = [[0]*(n) for i in range(n)]
cnt = 1
dx = [0,0,1,-1]
dy = [1,-1,0,0]
s = []

def bfs(i,j,cnt):
    q = deque([(i,j)])   
    result = 1
    v[i][j] = cnt        
    while q:
        x, y = q.popleft()
        for i in range(4): 
            nx, ny = x + dx[i],y + dy[i]
            if (0 <= nx < n and 0 <= ny < n) and v[nx][ny] == 0 and g[nx][ny] == 1 :
                q.append((nx,ny)) 
                result += 1 
                v[nx][ny] = cnt
    s.append(result)

for i in range(n):
    for j in range(n):
        if v[i][j] ==0 and g[i][j]==1:
            bfs(i,j,cnt)             
            cnt+=1
# print(v)
print(cnt-1)
print('\n'.join(map(str,sorted(s))))
