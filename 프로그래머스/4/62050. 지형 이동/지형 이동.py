from collections import deque, defaultdict
import math


def solution(land, height):
    n = len(land)
    answer = 0
    v = [[0] * n for _ in range(n)]
    dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]

    def find(x,parent):

        if x != parent[x]:
            parent[x] = find(parent[x], parent)
        return parent[x]

    def union(a, b, parent):
        a = parent[a]
        b = parent[b]
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    def get_groups_wieghts(land, groups, height):
        weights = defaultdict(lambda: math.inf)

        for i in range(len(groups)):
            for j in range(len(groups[0])):
                now = groups[i][j]
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]

                    if nx < 0 or ny < 0 or nx >= n or ny >= n or groups[nx][ny] == now:
                        continue

                    dist = abs(land[nx][ny] - land[i][j])

                    # 그룹과 그룹 사이 놓을 수 있는 사다리 중 가장 적은 비용을 저장
                    weights[(now, groups[nx][ny])] = min(
                        dist, weights[(now, groups[nx][ny])])

        return weights

    def kruskal(group_weights, groups):
        sum = 0
        roots = {_: _ for _ in range(1, groups)}  # {1:1, 2:2, 3:3 ... }
        # print('-', group_weights, roots)
        for (x, y), value in group_weights:
            # print(x, y, value)
            if find(x, roots) != find(y, roots):
                sum += value
                union(x, y, roots)
            if len(roots.items()) == 1:
                return sum
        return sum

    def bfs(x, y, cnt):
        l = 10000000000
        q = deque([(x, y)])
        v[x][y] = cnt
        while q:
            cx, cy = q.popleft()
            ground = land[cx][cy]
            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]
                if 0 <= nx < n and 0 <= ny < n and v[nx][ny] == 0:
                    diff = abs(land[nx][ny] - ground)
                    if diff <= height:
                        # print(nx,ny)
                        q.append((nx, ny))
                        v[nx][ny] = cnt
                    else:
                        # print(land[nx][ny], ground, l, diff)
                        l = min(l, diff)
        # print(f'l:{l}')
        if l == 10000000000:
            return 0
        else:
            return l

    cnt = 1
    for i in range(n):
        for j in range(n):
            if v[i][j] == 0:
                # print('---', i, j)
                answer += bfs(i, j, cnt)
                cnt += 1

    # for i in range(n):
        # print(v[i])

    w = get_groups_wieghts(land, v, height)
    w = sorted(w.items(), key=lambda x: x[1])
    answer = kruskal(w, cnt)
    # print(f'answer: {answer}')

    return answer


