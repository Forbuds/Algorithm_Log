from collections import deque
from itertools import combinations
n = int(input())
g = []
for _ in range(n):
    g.append(list(map(int, input().strip().split())))
def printg(g):
    for i in range(len(g)):
        print(g[i])
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def harmony(l):
    '''
    그룹 a와 그룹 b의 조화로움은 
    (그룹 a에 속한 칸의 수 + 그룹 b에 속한 칸의 수 ) 
    x 그룹 a를 이루고 있는 숫자 값 
    x 그룹 b를 이루고 있는 숫자 값 
    x 그룹 a와 그룹 b가 서로 맞닿아 있는 변의 수로 정의됩니다.
    하나 차이나는 쌍의 숫자: 각 원소를 tmp에 저장해 두고 비교해야 하나?
    set으로 비교하면 좋을텐데
    '''
    a,b = l[0],l[1]     # [[a[(),(),..], 숫자],b]
    
    len_a,len_b = len(a[0]),len(b[0])   #그룹 a에 속한 칸의 수
    n_a,n_b = a[1],b[1]                 #그룹 a를 이루고 있는 숫자 값 
  
    return (len_a+len_b )*n_a*n_b   # 맞댄 변 제외한 점수 계산

def bfs(x,y,c,v):     # 그룹 구하기

    tmp = [(x,y)]
    q = deque([(x,y)])
    v[x][y] = 1
    while q:
        x,y  = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<n and g[nx][ny]==c and v[nx][ny]==0:
                v[nx][ny]=1
                q.append((nx,ny))
                tmp.append((nx,ny))
    # print(tmp)
    return tmp,v

def combi(l,k,s,g_each,pairs):   # 조합 구하기
    if l==2:
        # print(s)
        pairs.append(list(s))
        return 
    else:
        for i in range(k,len(g_each)):
            s.append(g_each[i])
            combi(l+1,i+1,s,g_each,pairs)
            s.pop()

def art_score(g):

    score = 0  # 초기 예술 점수

    v = [[0]*n for _ in range(n) ]

    g_each = []     #bfs로 각 그룹을 구하고, [그룹에 속하는 인덱스 리스트들, 그룹을 이루는 숫자] 쌍을 구해 놓는다.
    for x in range(n):
        for y in range(n):
            if v[x][y]==0:
                tmp,v = bfs(x,y,g[x][y],v)
                g_each.append([tmp,g[x][y]])
              
    pairs = []    #쌍 중에 2개를 조합으로 뽑기
    combi(0,0,[],g_each,pairs)

    for pair in pairs:
        p1 = []
        p2 = set(pair[1][0])
        num = 0
        for i in range(4):
            for x,y in pair[0][0]:
                if (x+dx[i],y+dy[i]) in p2:     
                    # 하나를 기준잡고, 하나는 set으로 만들어준 다음에, dxdy 적용해서 맞닿을때마다 update
                    # 처음에는 둘 다 set으로 했는데, 그랬더니 '변'이 아니라 맞닿은 '인덱스' 숫자가 나와서 '변'을 구하려면 이렇게 해야 함
                    num+=1
        if num>0:
            score+= harmony(pair)*num

    return score

def clock(g):

    # 1 2 3
    # 4 5 6
    # 7 8 9

    # 7 4 1
    # print(list(zip(*g[::-1])))

    return list(map(list, zip(*g[::-1])))


def rclock(g):
    # print(list(map(list,zip(*g))[::-1]))
    return list(map(list,zip(*g)))[::-1]

def rotate(g):
    # 회전은 정중을 기준으로 두 선을 그어 만들어지는 십자 모양과 그 외 부분으로 나뉘어 진행됩니다
    # 1 2
    # 3 4
    # 4분면
    r1 = clock([[ g[x][y]  for y in range(0,n//2)] for x in range(0,n//2)   ])
    r2 = clock([[ g[x][y]  for y in range(n//2+1,n)] for x in range(0,n//2)   ])
    r3 = clock([[ g[x][y]  for y in range(0,n//2)] for x in range(n//2+1,n)   ])
    r4 = clock([[ g[x][y]  for y in range(n//2+1,n)] for x in range(n//2+1,n)   ])

    # 십자 모양십자 모양
    cross = rclock(g)

    # 범위 나눠서 진행   : 1사분면이면 r1, 2사분면이면 r2, 중앙이면 (x==n//2 or y==n//2) cross
    for x in range(n):
        for y in range(n):
            if x==n//2 or y==n//2:
                g[x][y] = cross[x][y]
            elif x<n//2:
                if y<n//2:
                    g[x][y] = r1[x][y]
                
                else:
                    g[x][y] = r2[x][y-n//2-1]
            else:
                if y<n//2:
                    g[x][y] = r3[x-n//2-1][y]
                
                else:
                    g[x][y] = r4[x-n//2-1][y-n//2-1]

    # printg(g)
    return g

def sol(g):
    result = art_score(g)
    for i in range(3):
        g = rotate(g)
        result += art_score(g)

    print(result)
sol(g)
