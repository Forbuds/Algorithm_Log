import sys
input = sys.stdin.readline
n, m = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
arr = sorted(arr)
s = []
v = [0]*n
def dfs(c,l):
    if l==m:
        print(' '.join(map(str,s)))
        return
    else:
        tmp = 0
        for i in range(n):
            if v[i]==0 and arr[i]!=tmp:
                s.append(arr[i])
                v[i] = 1
                dfs(i+1,l+1)
                tmp = s.pop()
                v[i] = 0
dfs(0,0)