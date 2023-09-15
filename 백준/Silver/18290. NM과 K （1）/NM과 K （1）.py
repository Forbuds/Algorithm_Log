import sys
input = sys.stdin.readline

n,m,k = map(int, input().strip().split())
arr = []
v = [[0]*m for _ in range(n)]
for i in range(n):
    arr.append(list(map(int, input().strip().split())))
dx = [-1,1,0,0]
dy = [0,0,1,-1]
q = []
result = -10000 * k -1
def dfs(l,x,y,s):
    global result
    if l==k:
        # print(sum(s))
        # print(q)
        result = max(s,result)
        return
    else:
        for i in range(x,n):
            for j in range(y if i==x else 0 ,m):
                if [i, j] not in q:
                    # print(l, i, j)
                    if ([i + 1, j] not in q) and ([i - 1, j] not in q) and ([i, j + 1] not in q) and (
                            [i, j - 1] not in q):
                        q.append([i, j])
                        dfs(l + 1,i, j, s + arr[i][j])
                        q.pop()

dfs(0,0,0,0)
print(result)