import sys
from collections import deque
input = sys.stdin.readline
max_height = 0
n = int(input())
g=[]
for _ in range(n):
    tmp = list(map(int, input().strip().split()))
    max_height = max(max_height, max(tmp))
    g.append(tmp)

dx = [0,0,1,-1]
dy = [-1,1,0,0]
result = 0

def bfs(i,j,v,x):
    q = deque([(i,j)])
    v[i][j] = 1
    while q:
        nx,ny = q.popleft()
        for k in range(4):
            cx, cy = nx+dx[k], ny+dy[k]
            if 0<=cx<n and 0<=cy<n and g[cx][cy]>x and v[cx][cy]==0:
                q.append((cx,cy))
                v[cx][cy] = 1
    return v

def safe(g, x):
    safe_bound = 0
    v = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if g[i][j]>x and v[i][j]==0:
                v = bfs(i,j,v,x)
                safe_bound +=1
    return safe_bound

for x in range(0,max_height+1):
    result = max(result, safe(g,x))
    
print(result)