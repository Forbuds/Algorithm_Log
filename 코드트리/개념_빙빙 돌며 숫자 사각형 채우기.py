https://www.codetree.ai/missions/5/problems/snail-number-square/description

import time
n,m  = map(int,input().strip().split())
dx = [0,1,0,-1]
dy = [1,0,-1,0]

g = [[0]*m for _ in range(n)]

# 그 다음이 숫자거나 , 끝을 만나면 뱡향 전환
# (i+1)%4
# 아니면 1씩 더해감

def is_in(x,y):
    return 0<=x<n and 0<=y<m
cnt = 0
num = 1
x,y = 0,0
i = 0
while num<=n*m:
    nx,ny = x+cnt*dx[i],y+cnt*dy[i]
    if is_in(nx,ny) and g[nx][ny]==0:
        g[nx][ny] = num
        num+=1
        cnt+=1
    else:
        x, y = nx - dx[i], ny - dy[i]
        i = (i+1)%4
        cnt = 1
        print(g)
        time.sleep(1)
print(g)
