def rotate(g,g_p):    # 어차피 한 줄이라 이렇게 씀
    tmp = g[-1]
    for i in range(2*n-1,0,-1):
        # print(i, i-1)
        g[i] = g[i-1]
    g[0] = tmp

    for i in range(n-1,0,-1):
        # print(i,i-1)
        g_p[i] = g_p[i-1]
    g_p[0] = 0
    # print(g,g_p)

    return g,g_p


def move(g,g_p):
    if g_p[-1]>0:
        g_p[-1]=0
    # print(g_p)

    for i in range(n-2,-1,-1):
        # print(i,i+1)
        if g_p[i]>0: # 사람이 있다면
            if g_p[i+1]==0 and g[i+1]>0:
                g_p[i + 1] = g_p[i]
                g[i + 1] -= 1
                g_p[i] = 0
            else:

                continue


        if g_p[-1]>0:
            g_p[-1]=0
    # print(g_p)
    if g_p[0]==0 and g[0]>0:
        g_p[0] = 1
        g[0] -= 1

    return g,g_p
def verify(g,k):
    '''
        안정성이 0인 칸이 k개 이상인가
    '''

    tmp = g.count(0)
    return tmp >= k

n,k = map(int,input().strip().split())
g = list(map(int,input().strip().split()))
cnt = 0
g_p = [0]*(n)
# print(n,k,g)


while True:
    # time.sleep(2)
    # print(f'turn {cnt}: ')
    if verify(g,k):
        break
    else:
        cnt+=1
        g, g_p = rotate(g, g_p)
        # print(g, g_p)
        g, g_p = move(g, g_p)
        # print(g, g_p)
        if verify(g,k):
            break
print(cnt)
