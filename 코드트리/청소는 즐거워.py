import copy
import math
n = int(input())
g = []
for _ in range(n):
    g.append(list(map(int, input().strip().split())))

'''
빙빙 돌며 + 
처음에 정가운데 격자에는 먼지가 존재하지 않습니다. 
정가운데부터 시작하여 아래 그림과 같이 나선형으로 바닥 청소를 하려 합니다.
'''

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
result = 0  # 격자 밖으로 떨어진 먼지 양의 총합


def is_in(x, y):
    return 0 <= x < n and 0 <= y < n


dust_tmp = [[0, 0, 2, 0, 0],
            [0, 10, 7, 1, 0],
            [5, 0, 0, 0, 0],
            [0, 10, 7, 1, 0],
            [0, 0, 2, 0, 0]]
dust_ratio = []
dust_ratio.append(dust_tmp)
for i in range(3):
    tmp = list(map(list, zip(*dust_tmp)))[::-1]
    # print(tmp)
    dust_ratio.append(tmp)
    dust_tmp = tmp
# print(len(dust_ratio))
# print(dust_ratio[1])


def printg(g):
    for i in range(len(g)):
        print(g[i])


def add_dust(cx, cy, d):
    global result, g
    dust = g[cx][cy]
    g[cx][cy] = 0
    tmp = 0
    # print('--',d)
    # tmp_dust = dust_ratio[d][d]
    # print(tmp_dust)
    # print('--')

    for i in range(5):
        for j in range(5):
            # print(cx-2+i,cy-2+j,i,j)

            c_dust = dust * (dust_ratio[d][i][j]) // 100
            tmp += c_dust
            if is_in(cx - 2 + i, cy - 2 + j) :
                g[cx - 2 + i][cy - 2 + j] += c_dust
            else:
                result += c_dust
    if is_in(cx + dx[d], cy +dy[d]):
        g[cx + dx[d]][cy + dy[d]] += dust - tmp
    else:
        result += dust-tmp

    # printg(g)


# cy-2   cx,cy-1 cx,cy cx,cy+1
#    cx+1,cy-1


# 0   2,1     2.2   2.3
#    3.1     3.2   3.3


# cx-2+i
# add_dust(2,1,0)


def move():
    '''
    빗자루가 이동할 때마다 빗자루가 이동한 위치의 격자(Curr)에 있는 먼지가 함께 이동하는데
    아래의 비율에 맞춰서 먼지가 이동하게 됩니다.
    이동한 먼지는 기존의 먼지 양에 더해지고,
    v 빗자루가 이동한 위치(Curr)에 있는 먼지는 모두 없어지게 됩니다.
    a%에 해당하는 먼지 양은 다른 격자에 이동한 먼지의 양을 모두 합한 것을 이동한 위치에 있던
    먼지의 양에서 빼고 남은 먼지에 해당합니다.
    비율을 곱해줄 때 소숫점 아래의 숫자는 버림해줍니다.
    '''

    g = [[0] * n for _ in range(n)]
    d = 0
    x, y = n // 2, n // 2
    cnt = 1
    num = 2
    i = 0
    while True:
        if x == 0 and y == 0:
            # print('------')
            break
        else:
            if i == 2:
                cnt += 1
                i = 0
            else:
                for j in range(cnt):
                    x, y = x + dx[d], y + dy[d]
                    # print(x, y)
                    # g[x][y]=num
                    add_dust(x, y, d)
                    # print('---')
                    # num+=1
                    if x == 0 and y == 0:
                        # print('------')
                        break
                d = (d + 1) % 4
                i += 1

    # printg(g)
    return


move()
print(result)
