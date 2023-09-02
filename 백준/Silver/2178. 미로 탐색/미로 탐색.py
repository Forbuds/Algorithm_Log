import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().strip().split())
g = []
for i in range(n):
    g.append(list(input().strip()))
dx = [0,0,1,-1]
dy = [1,-1,0,0]
v = [[0]*m for i in range(n)]
cnt = 1
def bfs():
    global cnt
    q = deque([(0,0)])
    v[0][0]=1
    while q:
        x,y = q.popleft()
        cnt = v[x][y]
        if x==n-1 and y==m-1:
            break
        else:
            # print(x,y)
            # if g[x][y]=='1' and v[x][y]==0:
            #     v[x][y] = 1
            for i in range(4):
                x_c,y_c = x+dx[i], y+dy[i]
                # print(x_c,y_c)
                if 0<=x_c<n and 0<=y_c<m:
                    # print('--')
                    if v[x_c][y_c]==0 and g[x_c][y_c]=='1':
                        # print('--')
                        q.append((x_c,y_c))
                        v[x_c][y_c] = cnt +1

bfs()
print(cnt)