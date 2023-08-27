import sys
input = sys.stdin.readline
n,k = map(int, input().strip().split())
result = 0
s = []

def combi(L,c):
    global result
    if L==k:
        result+=1
        # print(' '.join(map(str,s)))
    else:
        for i in range(c,n):
            s.append(i+1)
            combi(L+1,i+1)
            s.pop()
combi(0,0)
print(result)