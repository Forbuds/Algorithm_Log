n, m, K = map(int, input().strip().split())
arr = []
g = [[list() for _ in range(n)] for _ in range(n)]
result = 0
for _ in range(m):
    x, y, m, s, d = map(int, input().strip().split())
    x, y = x - 1, y - 1
    g[x][y] = [(m, s, d)]  # 격자가 최선이 아닐 수도?    # ✅ 어차피 격자가 작아서, 격자로 탐색해도 충분, arr 를 하나 격자를 하나 별 타격 없음
    arr.append(tuple([x,y,m,s,d]))
# print(g)

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def move(g,arr):
    tmp = [[list() for _ in range(n)] for _ in range(n)]
    for i in range(len(arr)):
        x, y, m, s, d = arr[i]
        x, y = (x + s * dx[d]) % n, (y + s * dy[d]) % n  # 이거 모르겠음
        tmp[x][y].append((m, s, d))
        # print(tmp[x][y])
    # print(tmp)
    arr = []
    for i in range(n):
        for j in range(n):
            if len(tmp[i][j])>1:
                M,S,D = 0,0,[]
                for l in tmp[i][j]:
                    m, s, d = l
                    M+=m
                    S+=s
                    D.append(d%2)
                    # if D%2==0:   # 상하좌우 관련 문제 잘못 읽음
                    
                M = M//5
                S = S//len(tmp[i][j])
                D = set(D)
                # print(D)
                if len(D)==1:     # 이것도 잘못 읽음, 한 종류라면 -> 상하좌우
                    # print(D)
                    D = [0,2,4,6]
                    # print(D)
                else:
                    D = [1,3,5,7]
                tmp[i][j] = list()
                if M==0:
                    pass
                else:
                    for k in range(4):
                        tmp[i][j].append((M,S,D[k]))
                        arr.append((i,j,M,S,D[k]))
            elif len(tmp[i][j]) == 1:
                # print(tmp[i][j])
                m,s,d = tmp[i][j][0]
                arr.append((i,j,m,s,d))

    return tmp,arr

def remain(g):
    global result
    # print(g)
    for x in range(n):
        for y in range(n):
            if len(g[x][y])>0:
                # print(g[x][y])
                for l in g[x][y]:
                    result += l[0]

    # ✅ 위랑 같은데, 이렇게도 가능함
    result = sum([
        weight
        for i in range(n)
        for j in range(n)
        for weight, _, _ in g[i][j]
    ])

def printg(g):
    for i in range(len(g)):
        print(g[i])

for k in range(K):
    # print('s: ')
    # printg(g)
    g,arr = move(g,arr)
    # print('e: ')
    # printg(g)

remain(g)
print(result)
