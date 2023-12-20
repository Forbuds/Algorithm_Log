# https://softeer.ai/app/assessment/index.html?xid=65767&xsrfToken=Kbsni0Oh9uPYbwS7kc0M04LR5SsSr2e7&testType=practice

import sys
import heapq as hq
from collections import defaultdict
input = sys.stdin.readline
n = int(input())
scores = []
results = []
final = defaultdict(int)
for _ in range(3):
  scores.append(list(map(int, sys.stdin.readline().split())))


for score in scores:
  result = []
  tmp = defaultdict(int)
  tmp_k = 1
  tmp_point = 0
  k = 1
  for i,point in enumerate(score):
    hq.heappush(result,(-point,i))
  for _ in range(n):
    point,i = hq.heappop(result)
    # print(i,point)
    if point == tmp_point:
      tmp[i] = tmp_k
    else:
      tmp[i] = k 
      tmp_k = k
      tmp_point = point
    k += 1
    final[i] -= point
  # print([ num for k,num in sorted(tmp.items())])
  results.append([ num for k,num in sorted(tmp.items())])

tmp = defaultdict(int)
result = []
tmp_k = 1
tmp_point = 0
k = 1
for i,point in final.items():
  # print(i,point)
  hq.heappush(result, (-point,i))
for _ in range(n):
  point,i = hq.heappop(result)
  if point == tmp_point:
      tmp[i] = tmp_k
  else:
    tmp[i] = k 
    tmp_k = k
    tmp_point = point
  k += 1

for result in results:
  print(' '.join(map(str,result)))
# print(tmp)
print(' '.join(map(str,[ num for k,num in sorted(tmp.items())])))
