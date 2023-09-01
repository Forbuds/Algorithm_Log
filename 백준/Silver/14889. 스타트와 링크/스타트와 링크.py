import sys
input = sys.stdin.readline

n = int(input())
g = []
for i in range(n):
    g.append(list(map(int, input().strip().split())))
s = []
result = 9999999999999999999999
def sum_(s):
    left, right = 0, 0
    for i in s:
        for j in s:
            if i!=j:
                left += g[i-1][j-1]
    re = set([i+1 for i in range(n)])-set(s)
    for i in re:
        for j in re:
            if i!=j:
                right += g[i-1][j-1]
    return abs(left-right)
def dfs(l,index):
    global result
    if l == n//2:
        # print(s, sum_(s))
        result = min(result, sum_(s))
        return
    for i in range(index,n):
        s.append(i+1)
        dfs(l+1,i+1)
        s.pop()

dfs(0,0)
print(result)