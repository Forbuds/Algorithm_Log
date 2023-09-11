import sys
input = sys.stdin.readline
n,m = map(int, input().strip().split())
# print(n,m)
s =[]
v = [0]*(n)
def dfs():
    if(len(s)==m):
        print(' '.join(map(str,s)))
    else:
        for i in range(n):
            if v[i]==0:
                s.append(i+1)
                v[i]=1
                dfs()
                s.pop()
                v[i] = 0
            else:
                pass

dfs()