from collections import deque
n,Q = map(int, input().strip().split())
g = []

'''
회전을 모두 끝낸 뒤에 남아있는 빙하의 총 양
'''
remain = 0
'''
가장 큰 크기를 가지는 얼음군집의 크기    / 얼음 군집이 존재하지 않는다면 0
'''
max_ice = 0

for i in range(2**n):
    g.append(list(map(int, input().strip().split())))
level = list(map(int, input().strip().split()))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

# def is_in

def neigh(x,y,k):
    cnt = 0
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0<=nx<k and 0<=ny<k:
            if g[nx][ny]>0:
                cnt+=1
    if cnt>=3:
        return 0
    else:
        return -1
                
def melt(g):
    k = len(g)
    tmp_melt = [[0]*k for _ in range(k)]

    for x in range(k):
        for y in range(k):
            if g[x][y]<1:
                continue
            else:
                tmp_melt[x][y] = neigh(x,y,k)



    return [[g[x][y]+tmp_melt[x][y] for y in range(k)] for x in range( k) ]

def rotate(g):

    k = len(g)
    # if k==2:
    #     return g
    # else:
    ddx = [+k//2,0,0,-k//2]
    ddy = [0,-k//2,+k//2,0]
    tmp = [[0]*k for _ in range(k)]
    cnt = 0
    # print('rotate')
    for i in range(2):
        for j in range(2):
            for x in range(i*k//2,(i+1)*k//2):
                for y in range(j*k//2,(j+1)*k//2):
                    tmp[x][y] = g[(x+ddx[cnt])%k][(y+ddy[cnt])%k]
                    # print(x,y,(x+ddx[cnt])%k,(y+ddy[cnt])%k)
            # tmp[i*k//2:(i+1)*k//2][j*k//2:(j+1)*k//2]  =  g[i*k//2+ddx[cnt]:(i+1)*k//2+ddx[cnt]][j*k//2+ddy[cnt]:(j+1)*k//2+ddy[cnt]]
            cnt+=1

    # printg(tmp)


    return tmp
def printg(g):
    for i in range(len(g)):
        print(g[i])

def select(g,l):
    range_list = [0]
    for p in range(1,2**n//2**l+1):
        range_list.append(2**l*p)
    # print(range_list)    # range_list로 하여금 범위를 선택할 수 있는 기능을 부여
    for i in range(len(range_list)-1):
        for j in range(len(range_list)-1):
            # print('-'*40,f'{range_list[i]}:{range_list[i+1]},{range_list[j]}:{range_list[j+1]}')
            # printg([[g[x][y] for y in range(range_list[j],range_list[j+1])] for x in range(range_list[i],range_list[i+1])])
            
            tmp = rotate([[g[x][y] for y in range(range_list[j],range_list[j+1])] for x in range(range_list[i],range_list[i+1])])
            for x in range(range_list[i],range_list[i+1]):
                for y in range(range_list[j],range_list[j+1]):
                    g[x][y] = tmp[x-range_list[i]][y-range_list[j]]
                    # print(x,y,x-range_list[i],y-range_list[j])
    return g



# print(2**n//2**2)
# select(g,2)

def bfs(g,x,y):
    
    s = deque([(x,y)])
    v[x][y]=1
    c = 1
    while s:
        x,y = s.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<len(g) and 0<=ny<len(g) and v[nx][ny]==0 and g[nx][ny]>0:
                s.append((nx,ny))
                v[nx][ny]=1
                c+=1
    # print(f'c:{c}')
    return c

def group(g):
    global v
    v =[[0]*len(g) for _ in range(len(g)) ]
    cnt = 0
    max_group = 0
    for i in range(len(g)):
        for j in range(len(g)):
            if g[i][j]>0 and v[i][j]==0:
                max_group = max(max_group,bfs(g,i,j))
                cnt+=1
    # print('max_group',max_group)

    return max_group
def remain(g):
    sum_of = 0
    for i in range(len(g)):
        sum_of+=sum(g[i])
    return sum_of


for q in range(Q):
    # print('--'*20,'s', level[q])
    # printg(g)
    g = select(g,level[q])
    # print('--'*20,'e')
    # printg(g)
    g = melt(g)

print(remain(g))
print(group(g))
