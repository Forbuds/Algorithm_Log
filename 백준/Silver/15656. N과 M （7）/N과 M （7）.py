import sys
input = sys.stdin.readline
n, m = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
arr = sorted(arr)
s = []
def dfs(c,l):
    if l==m:
        print(' '.join(map(str,s)))
        return
    else:
        for i in range(n):
            s.append(arr[i])
            dfs(i,l+1)
            s.pop()
dfs(0,0)