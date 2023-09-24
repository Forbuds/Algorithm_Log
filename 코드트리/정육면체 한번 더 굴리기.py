import sys
from collections import deque
input = sys.stdin.readline

n,M = map(int, input().strip().split())
g = []
for _ in range(n):
    g.append(list( map(int, input().strip().split())))

clock = [(0,1),(1,0),(0,-1),(-1,0)]
r_clock = [x for x in clock[::-1]]

# print(clock)
# print(r_clock)
def direction(b,g_,ddx,ddy):
    if b>g_:
        ddx,ddy = clock[(clock.index((ddx,ddy))+1)%4]
    elif b<g_:
        ddx,ddy = r_clock[(r_clock.index((ddx,ddy))+1)%4]
    return ddx,ddy


def roll(top,right,front,ddx,ddy):
    if (ddx,ddy)==(1,0):
        c_list = [7-front,right,front,7-right]
        r_list = [top,7-top]
    elif (ddx,ddy) == (-1,0):
        c_list = [front,right,7-front,7-right]
        r_list = [7-top,top]
    elif (ddx,ddy) == (0,-1):
        c_list = [right,7-top,7-right,top]
        r_list = [front,7-front]
    else:
        c_list = [7-right,top,right,7-top]  
        r_list = [front,7-front]

    return c_list,r_list

dx = [1,-1,0,0]
dy = [0,0,1,-1]
def printg(arr):
    for i in range(len(arr)):
        print(arr[i])
def score(x,y):
    ground = g[x][y]
    q = deque([(x,y)])
    v = [[0]*n for _ in range(n)]
    v[x][y] = 1
    cnt = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if v[nx][ny] == 0 and g[nx][ny]==ground:
                    v[nx][ny]=1
                    q.append((nx,ny))
                    cnt+=1
    # printg(v)
    # print(cnt*g[x][y])
    return cnt*g[x][y]
result = 0

x,y = 0,0
ddx,ddy = 0,1
top,right,front = 1,3,2
c_list,r_list = roll(top,right,front,ddx,ddy)
top,right,front = c_list[0],c_list[1],r_list[0]
# print(top,right,front)
x,y = x+ddx,y+ddy
result += score(x,y)

for m in range(M-1):

    ddx,ddy = direction(c_list[2],g[x][y],ddx,ddy)
    if 0<=x+ddx<n and 0<=y+ddy<n:
        pass
    else:
        ddx,ddy = -ddx,-ddy
    x,y = x+ddx,y+ddy
    c_list,r_list = roll(top,right,front,ddx,ddy)
    top,right,front = c_list[0],c_list[1],r_list[0]
    # print(top,right,front)
    result += score(x,y)
print(result)
