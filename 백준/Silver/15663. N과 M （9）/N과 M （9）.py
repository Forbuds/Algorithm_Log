import sys
input = sys.stdin.readline

n,m = map(int, input().strip().split())
arr = sorted(list(map(int, input().strip().split())))
v = [0]*n
s = []
def dfs(l):
    if l==m:
        print(' '.join(map(str,s)))
        return
    else:
        tmp = -1          
        for i in range(n):
            if v[i]==0 and tmp!=arr[i]:   #tmp : 같은 레벨에서만 다르면 된다.
                tmp = arr[i]
                s.append(arr[i])
                v[i]=1
                dfs(l+1)
                s.pop()
                v[i] = 0
dfs(0)