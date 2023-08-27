import sys
input = sys.stdin.readline
while True:
    s = list(map(int,input().strip()))
    if sum(s)==0:
        break
    else:
        # print('------------')
        # print(s)
        l = len(s)
        if l==1:
            print('yes')
        else:
            if l%2==1:
                # print(s[:l // 2], [i for i in reversed(s[-l // 2+1:])])
                if s[:l // 2] == [i for i in reversed(s[-l // 2+1:])]:
                    print('yes')
                else:
                    print('no')
            else:
                # print(s[:l//2] , [i for i in reversed(s[-l // 2 :])] )
                if s[:l//2] == [i for i in reversed(s[-l // 2 :])]:
                    print('yes')
                else:
                    print('no')
        # print(s[:l//2])
        # print(s[-l//2+1:])
