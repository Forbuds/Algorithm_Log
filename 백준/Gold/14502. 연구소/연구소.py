import sys
from collections import deque
from itertools import combinations
from copy import deepcopy
input = sys.stdin.readline

n,m = map(int, input().strip().split())
G=[]
for _ in range(n):
    tmp = list(map(int, input().strip().split()))
    G.append(tmp)

# 0은 빈칸, 1은 벽, 2는 바이러스
dx = [0,0,1,-1]
dy = [-1,1,0,0]
result = 0

def bfs(i,j,v,flag):
    q = deque([(i,j)])
    v[i][j] = 1
    while q:
        nx,ny = q.popleft()
        for k in range(4):
            cx, cy = nx+dx[k], ny+dy[k]
            if 0<=cx<n and 0<=cy<m and g[cx][cy]==0 and v[cx][cy]==0:
                q.append((cx,cy))
                v[cx][cy] = 1
                if flag:
                    g[cx][cy] = 2

# 바이러스 퍼짐: 값이
# 안전영역 개수: 값이 0
#
# for문 돌다가 2면 bfs

def safe(g):
    safe_bound = 0
    v = [[0]*m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if g[x][y]==0 and v[x][y]==0:
                bfs(x,y,v,False)

    for x in range(n):
        for y in range(m):
            safe_bound += v[x][y]
    return safe_bound

combi_arr = []
for x in range(n):
    for y in range(m):
        if G[x][y]==0:
            combi_arr.append((x,y))

for combi in  combinations(combi_arr,3):
    # print(combi)
    g = deepcopy(G)
    for x,y in combi:
        g[x][y] = 1
    v = [[0]*m for _ in range(n)]
    # g[1][0] = 1
    # g[0][1] = 1
    # g[3][5] = 1
    for x in range(n):
        for y in range(m):
            if v[x][y] == 0 and g[x][y]==2:
                bfs(x,y,v,True)
    result = max(result, safe(g))
print(result)