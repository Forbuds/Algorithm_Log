import sys
input = sys.stdin.readline

n = int(input())
l = [int(input()) for _ in range(n)]
# print(n,l)

for i in range(n-1):                        # 마지막 인덱스 직전까지 탐색
    g = l[i]                                # 현재 값 보관
    c_i = l.index(min(l[i+1:]))             # 가장 작은 인덱스 추출
    if g <= l[c_i]:
        pass
    else:
        l[i] = l[c_i]
        l[c_i] = g
print('\n'.join([str(i) for i in l]))