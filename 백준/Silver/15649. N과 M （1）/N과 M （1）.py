import sys
input = sys.stdin.readline
n, m = map(int, input().strip().split())
v = [0]*n
def dfs(c,l):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    else:
        for i in range(0,n):
            if v[i]==0:
                s.append(i+1)
                v[i]=1
                dfs(i+1,l+1)
                s.pop()
                v[i] = 0
s = []
dfs(0,0)