import sys
input = sys.stdin.readline
g = []
n,m = map(int,input().strip().split())
for i in range(n):
    g.append(list(map(str,input().strip())))
    
# 다 돌면서 이상한 곳 찾아내도 된다. 그런데 오래 걸리지 않을까?
# 문제에서 잘라낸 후에 다시 칠한다 했으니, 잘라내는 함수 따로 / 다시 칠하는 함수 따로

def repaint(g):
    n, m = 8,8
    result = 50*50+1
    result_w = 0
    result_b = 0

    w = [['W' if i%2==0 else 'B' for i in range(m)] if j%2==0 else ['B' if i%2==0 else 'W' for i in range(m)] for j in range(n)]
    b = [['B' if i%2==0 else 'W' for i in range(m)] if j%2==0 else ['W' if i%2==0 else 'B' for i in range(m)] for j in range(n)]
    # 두 가지 경우의 수
    
    for i in range(n):
        for j in range(m):
            if g[i][j] != w[i][j]:
                result_w+=1
            if g[i][j] != b[i][j]:
                result_b += 1
    result = min(result_b,result_w)
    
    return result

answer = 50*50+1

for i in range(n):
    if n - i < 8:
        # print('w1',len(g[i:i+8]))
        break
    for j in range(m):
        if m-j < 8:
            break
            # print(g[i:i+8][j:j+8])
        # print([tmp[j:j+8] for tmp in g[i:i+8]])
        answer = min(answer, repaint([tmp[j:j+8] for tmp in g[i:i+8]]))
        
    # 8x8로 잘라서 확인 모두, min값 찾기
print(answer)


