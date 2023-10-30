import sys
input = sys.stdin.readline
n, m = map(int, input().strip().split())

def dfs(c,l):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    else:
        for i in range(c,n):
            s.append(i+1)
            dfs(i+1,l+1)
            s.pop()
s = []
dfs(0,0)