import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().strip().split()))
tmp = list(map(int, input().strip().split()))  # + - x /
cal = []
for i in range(4):
    for j in range(tmp[i]):
        cal.extend([i+1])
# print(cal)
v = [0]*len(cal)
result_min = 10**9
result_max = -10**9
s = []
def calc(s):
    result = arr[0]
    for i in range(len(s)):
        if s[i]==1:
            result += arr[i + 1]
        elif s[i]==2:
            result -= arr[i + 1]
        elif s[i]==3:
            result *= arr[i + 1]
        else:
            if result<0:
                result = -(abs(result)//arr[i+1])
            else:
                result = result // arr[i + 1]
    return result
def dfs(l):
    global result_min,result_max
    if l==len(cal):
        # print(s,calc(s))
        result = calc(s)
        result_min = min(result_min, result)
        result_max = max(result_max, result)
        return
    for i in range(len(cal)):
        if v[i]==0:
            v[i]=1
            s.append(cal[i])
            dfs(l+1)
            s.pop()
            v[i] = 0

dfs(0)
print(result_max)
print(result_min)