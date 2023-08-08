import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int,input().strip().split()))
result = 0
# print(n,l)
for k in l:
    cnt = 0
    for i in range(1,k+1):
        if k%i==0:
            cnt+=1
    if cnt ==2:
        result+=1
print(result)