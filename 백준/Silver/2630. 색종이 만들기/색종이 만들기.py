import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
def print_g(g):
    for i in range(len(g)):
        print(g[i],'_ok')

n = int(input().strip())
g = []
for i in range(n):
    # print(list(map(int,input().strip().split(' '))))
    g.append(list(map(int,input().strip().split())))

result=[]
def make_p(x,y,N):
    ch = g[x][y]

    for i in range(x,x+N):
        for j in range(y,y+N):
            if ch!=g[i][j]:
                make_p(x,y,N//2)
                make_p(x+N//2, y, N // 2)
                make_p(x, y+N//2, N // 2)
                make_p(x+N//2, y+N//2, N // 2)
                return
    if ch==0:
        result.append(0)
    else:
        result.append(1)

make_p(0,0,n)

print(result.count(0))

print(result.count(1))
