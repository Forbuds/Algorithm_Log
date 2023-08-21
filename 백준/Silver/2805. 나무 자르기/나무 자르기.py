import sys
import time
input = sys.stdin.readline
n,m = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
# m을 하나씩 하기란 불가능에 가까움
h = max(arr)
s = 0
e = max(arr)

flag = 0
while True:
    log = 0
    for x in arr:
        if x>=h:
            log+=x-h
    
    if log==m or flag>1:
        print(h)
        break

    elif log>=m:
        # print(s, h, e, sum([x-h if x>=h else 0 for x in arr]), m)
        s = h
        h = (s + e) // 2
        if s==h:
            flag=2
        # time.sleep(1)
    elif log<=m:
        # print('',s, h, e, sum([x-h if x>=h else 0 for x in arr]), m)
        e = h
        h = (s + e) // 2
        if e==h:
            flag=2
        # time.sleep(1)