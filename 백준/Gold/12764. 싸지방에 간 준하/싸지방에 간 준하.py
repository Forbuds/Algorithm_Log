# https://www.acmicpc.net/source/65350757
# https://deok2kim.tistory.com/326
import sys
from heapq import heappush, heappop, heappushpop
# 모든 사람은 정해진 시간에 싸지방 이용
# 사용률에 따라 사양 다르게 설치
# 사람이 들어오면 컴퓨터 번호 작은 자리부터
# 기다리지 않고 싸지방 이용할 수 있는
# 최소 개수, 몇 명 사용했는가
# 컴퓨터가 우선순위 큐?
input = sys.stdin.readline
n = int(input())
people = []
for i in range(n):
    people.append(list(map(int, input().strip().split())))
cnt = 0
people = sorted(people,key = lambda x: x[0])

computers = [i for i in range(n)]
heap = []  # tail, 개수
result = [0] * n

for i in range(n):
    s,t = people[i]
    # print(s,t)
    # print(heap, computers)
    if not heap or heap[0][0] > s:   # 아무데도 비어있지 않죠
        cnt+=1
        # print('up')
        idx = heappop(computers)
        result[idx] += 1
        heappush(heap, [t, idx])
        # print(heap, computers)
    else:   # 어딘가가 비어 있습니다.
        # 혼자만 비어 있나요?
        #     넣고 끝
        # 여러 군데가 비어 있나요?
        #     인덱스 찾자요
        while True:
            tail,idx = heappop(heap)

            if heap and heap[0][0] < s:  # 여러 군데 비어 있어요
                heappush(computers, idx)
                continue
            else:   # 혼자만 비어 있어요
                new_i = heappushpop(computers, idx)
                # print(computers)
                heappush(heap, [t, new_i])
                result[new_i] += 1
                break
    # print(heap, computers)

    # print(computer,computer_tmp)
ans = []
cnt = 0
for i in result:
    if i != 0:
       cnt += 1
       ans.append(i)

print(cnt)
print(*ans)


# 7
# 0 20
# 3 10
# 5 17
# 7 13
# 8 15
# 14 25
# 16 30