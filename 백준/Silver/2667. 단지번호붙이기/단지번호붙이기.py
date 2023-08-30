import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
g = []
for i in range(n):
    g.append(list(map(int,list(input().strip()))))
v = [[0]*(n) for i in range(n)]
cnt=1
dx = [0,0,1,-1]
dy = [1,-1,0,0]
s = []
# print(v)
# print(g)
def bfs(i,j,cnt):
    q = deque([(i,j)])
    result = 1
    v[i][j] = cnt
    while q:
        x_c, y_c = q.popleft()
        for i in range(4):
            x_f,y_f = x_c+dx[i],y_c+dy[i]
            if (0<=x_f<n and 0<=y_f<n) and v[x_f][y_f] == 0 and g[x_f][y_f] == 1 :
                q.append((x_f,y_f))
                result += 1
                v[x_f][y_f] = cnt
    s.append(result)
for i in range(n):
    for j in range(n):
        if v[i][j] ==0 and g[i][j]==1:
            bfs(i,j,cnt)
            cnt+=1
# print(v)
print(cnt-1)
print('\n'.join(map(str,sorted(s))))