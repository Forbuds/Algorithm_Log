import sys
input = sys.stdin.readline
n = int(input())
s = set()
for i in range(n):
    tmp = input().strip().split()
    # print(s,tmp)
    if len(tmp)==1:
        if tmp[0] == 'all':
            s = set([i+1 for i in range(20)])
        else:
            s = set()
    else:
        ins = tmp[0]
        x = int(tmp[1])

        if ins == 'add':
            s.add(x)
        elif ins == 'remove':
            s.discard(x)
        elif ins == 'check':
            if x in s:
                print(1)
            else:
                print(0)
        elif ins == 'toggle':
            if x in s:
                s.discard(x)
            else:
                s.add(x)