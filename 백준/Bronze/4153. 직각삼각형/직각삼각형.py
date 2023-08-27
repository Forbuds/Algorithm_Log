import sys

input = sys.stdin.readline

while True:
    s = list(map(int,input().strip().split()))
    if s == [0,0,0]:
        break
    else:
        s = sorted(s)
        result = s[0]**2 + s[1]**2
        if result == s[2]**2:
            print('right')
        else:
            print('wrong')