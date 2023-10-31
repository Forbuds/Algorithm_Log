import sys
input = sys.stdin.readline

m = int(input())
def det(x):
    if x <2:
        return False
    for i in range(2,int(x**(0.5))+1):
        # print(i,x%i)
        if x%i==0:
            return False
    return True
s = []
def dfs(l,c):
    # print(f'l : {l}')
    if l==m:
        print(c)
        return
    else:
        for x in range(10):
            num = (10)*c + x
            # print(num, det(num))
            if det(num):
                # print(num)
                s.append(num)
                dfs(l+1,num)
                s.pop()
dfs(0,0)