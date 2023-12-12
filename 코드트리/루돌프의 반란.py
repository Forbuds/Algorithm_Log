# p명의 산타
# 루돌프가 산타 박치기, 산타는 루돌프 잡고싶다
import sys
sys.stdin = open("E:\노트북\취준\삼성\sample_input_2312.txt",'r',)
import heapq as hq
n, M, p, c, d = map(int, input().strip().split())
rx, ry = map(int, input().strip().split())
rx, ry = rx-1, ry-1
s = [()]*p
print(s)
for _ in range(p):
    sn, sx, sy = map(int, input().strip().split())
    s[sn-1]=(sx-1, sy-1)
print(s)
g = [[0]*n for _ in range(n)]
# 좌상단이 1,1
# m턴, 턴마다 한 번씩 움직
# 기절, 격자밖에 나가면 움직일 수 없음
def dist(r1,c1,r2,c2):
    return (r1-r2)**2 + (c1-c2)**2
def is_in(x,y):
    return 0<=x<n and 0<=y<n

result = [0]*p  # 산타가 얻은 최종 점수
state_arr = [0]*p

dx, dy = [-1,0,1,0], [0,1,0,-1]

def s_interaction(cx,cy,i,dirx,diry):
    # 안바꿨다는 가정 하에
    print('dir',dirx,diry)
    for index in range(len(s)):
        if s[index] == (cx,cy) and index != i:
            cx, cy = cx + dirx, cy + diry
            if is_in(cx,cy):
                if (cx,cy) in s:
                    s_interaction(cx, cy, index,dirx,diry)
                else:
                    s[index] = (cx, cy)
            else:
                s[index] = (-1,-1)
                state_arr[index] = -1
                return s

    return s


def ru_target(rx,ry,s):
    distance, x, y = 10000, 0,0
    for i in range(len(s)):
        if state_arr[i] != -1:
            sx, sy = s[i]
            distance, x, y = min((dist(rx,ry,sx, sy), -sx, -sy), (distance, x, y))

    return -x, -y
def ru_move(rx,ry,sx,sy,s):
    # print(int((sx-rx)/abs(sx-rx)), sy-ry)
    dirx, diry = 0,0
    if (sx - rx)==0:
        pass
    else:
        dirx = int((sx - rx) / abs(sx - rx))
        rx += dirx
    if (sy-ry)==0:
        pass
    else:
        diry = int((sy-ry) / abs(sy-ry))
        ry += diry

    if (rx,ry) in s:  # 루돌, 산타랑 부딪
        index = s.index((rx,ry))  #몇번이랑?
        result[index] += c   #점수 부여
        cx,cy = s[index]
        cx,cy = cx+dirx*c,cy+diry*c
         #산타 위치조정,
        if is_in(cx, cy):
            s[index] = (cx, cy)
            # 상호작용
            if (cx, cy) in s: # 다른 산타랑 부딪
                s = s_interaction(cx,cy,index,dirx,diry)
            # 기절
            state_arr[index] = 2
        else:
            # 탈락
            state_arr[index] = -1
            s[index] = (-1,-1)



    return rx,ry, s

def s_move(rx, ry, sx, sy):
    posi = []
    c_distance = dist(rx,ry,sx,sy)
    for i in range(4):
        nx, ny = sx + dx[i], sy + dy[i]
        if is_in(nx,ny) and (nx,ny) not in s:
            distance = dist(rx, ry, nx, ny)
            if distance < c_distance:
                hq.heappush(posi,[distance,i,nx,ny])
    if len(posi)==0:
        return -1,-1,-1
    else:
        distance,dir, nx,ny = hq.heappop(posi)
        return dir, nx,ny

def s_return(rx,ry,s):
    tmp = []

    for i in range(len(s)):
        state = state_arr[i]
        if state != 0:
            continue
        else:
            sx, sy = s[i]
            dir, sx, sy = s_move(rx, ry, sx, sy)

            if (sx,sy) in s or not is_in(sx,sy) or sx==-1:
                continue
            else:
                s[i] = (sx, sy)
        # i가 dir 방향으로
        if (sx, sy)==(rx,ry):
            # dir 반대 방향으로 튕김
            cx,cy = sx + d*(-dx[dir]), sy+ d*(-dy[dir])
            result[i] += d

            if is_in(cx,cy):
                s[i] = (cx, cy)
                if (cx, cy) in s:  # 다른 산타랑 부딪
                    print('튕',i+1,s)
                    s = s_interaction(cx, cy,i,-dx[dir],-dy[dir])
                # 상호작용
                # 기절
                state_arr[i] = 2
            else:
                # 탈락
                print('탈', s)
                state_arr[i] = -1
                s[i] = (-1,-1)
    print(s)



    return s
m =0
while state_arr != [-1]*len(s) and m<M:
    # 만약 p 명의 산타 탈락? -> 게임 즉시 종료
    # 루돌프

    sx, sy = ru_target(rx,ry,s)
    print('s',sx, sy)
    rx,ry, s = ru_move(rx, ry, sx, sy,s)
    print('r',rx,ry)
    s = s_return(rx,ry,s)
    print('',s)
    print(state_arr)

    result = [result[i]+1 if state_arr[i]>-1 else result[i] for i in range(len(result))]
    print(result)
    print('',m)

    state_arr = [state-1 if state>0 else state for state in state_arr]
    m +=1

print(' '.join(map(str, result)))
    # (거리, x, y)로 정렬해서 돌진 - 한 칸
#
#     산타
