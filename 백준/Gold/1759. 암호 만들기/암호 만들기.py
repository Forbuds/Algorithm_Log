import sys
input = sys.stdin.readline
from itertools import combinations
m,n = map(int, input().strip().split())
arr = list(map(str, input().strip().split()))
arr_a = [k for k in arr if k in 'aeiou' ] # 두개 골라잡고 / 그다음에 한번에
arr_b = list(set(arr)-set(arr_a))
# print(arr_a)
# print(arr_b)
s = []
for i in range(m-3+1):
    # print(i + 1, m - 3 - i + 2)
    if i+1>len(arr_a) or m-3-i+2>len(arr_b):
        continue
    else:
        # print(i + 1, m - 3 - i + 2)
        for x in combinations(arr_a,i + 1):
            for y in combinations(arr_b,m - 3 - i + 2):
                s.append(''.join(sorted(x+y)))
for x in sorted(s):
    print(x)


# 참고 코드: https://www.acmicpc.net/source/68333541
nCr = itertools.combinations(characters, L)
mo = ('a', 'e', 'i', 'o', 'u')
for s in nCr:
    moCount = 0
    jaCount = 0
    for c in s:   # 돌면서, 모음과 자음의 개수를 세고, 조건 충족하면 print해주는 방식
        if c in mo:
            moCount += 1
        else:
            jaCount += 1
        if moCount >=1 and jaCount >= 2:
            print("".join(s))
            break

# 참고 코드2: https://codinghejow.tistory.com/230
# dfs 그대로 사용, 조건 달아줄 것
def dfs(l,c):
    if l==m:
        mo,ja = 0,0
        for x in s:
            if x in 'aeiou':
                mo +=1
            else:
                ja +=1
        if mo>=1 and ja >=2:
            print(''.join(s))
        return
    else:
        for i in range(c,n):
            s.append(arr[i])
            dfs(l+1,i+1)
            s.pop()
dfs(0,0)
