# https://velog.io/@himi/%EB%B0%B1%EC%A4%80-10942.-%ED%8C%B0%EB%A6%B0%EB%93%9C%EB%A1%AC
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().strip().split()))
m = int(input())
dp = [[0]*n for _ in range(n)]

for length in range(n):
    # print(f'-------length : {length}')
    for s in range(n-length):
        # print(s, s+length)
        e = s + length
        if s == e:
            # 시작점과 끝점이 같다면? 팰린드롬
            dp[s][e] = 1
        elif arr[s] == arr[e]:
            # 끝에 두 문자가 같다면?
            if s+1 == e:   #길이가 2라면, 무조건 팰린드롬
                dp[s][e]=1
            elif dp[s+1][e-1]==1:   # 가운데 문자열 검사
                dp[s][e] = 1

for i in range(m):
    s,e = map(int, input().strip().split())
    print(dp[s-1][e-1])