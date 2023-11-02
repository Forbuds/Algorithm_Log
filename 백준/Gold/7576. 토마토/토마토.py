import sys
from collections import deque
input = sys.stdin.readline

# 1 익은 토마토 0 익지 않능 토마토 -1 토마토 없음

m,n = map(int, input().strip().split())
g = []
for _ in range(n):
    g.append(list(map(int,input().strip().split())))
v = [[0]*m for _ in range(n)]
q = deque([])
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
result = -1000

for i in range(n):
    for j in range(m):
        if g[i][j] == 1:
            q.append((i, j))
if all(0 not in l for l in g):
    print(0)
else:

    while q:
        cx,cy = q.popleft()
        for k in range(4):
            nx = cx+dx[k]
            ny = cy+dy[k]
            if 0 <= nx < n and 0 <= ny < m :
                if g[nx][ny] == 0:
                    g[nx][ny] = g[cx][cy]+1
                    q.append((nx,ny))
    for l in g:
        if 0 in l:
            print(-1)
            exit(0)
        else:
            result = max(result,max(l))
    print(result-1)

# a =[ [1,1,1,-1],[1,1,1,1]]
# print(any(0 in l for l in a))