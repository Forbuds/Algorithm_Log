import sys
input = sys.stdin.readline

n,m = map(int, input().strip().split())
arr= list(map(int, input().strip().split()))
arr= sorted(arr)
# print(arr)
s = []
result = []
v = [0]*(n)
def comb(l,index):
    if l==m:
        # print(' '.join(map(str,s)))
        result.append(s[:])
        return
    else:
        for i in range(len(arr)):

            if v[i]==0:
                s.append(arr[i])
                v[i] = 1
                comb(l+1, index+1)
                s.pop()
                v[i] = 0

comb(0,0)
for k in sorted(list(set(map(tuple,result)))):
    print(*k,sep=' ')