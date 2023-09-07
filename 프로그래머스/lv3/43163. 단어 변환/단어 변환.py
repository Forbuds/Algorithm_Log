from collections import deque
def solution(begin, target, words):
    answer = 0
    n = len(begin)
    q = deque([begin])
    v = [0]*len(words)
    c = 1
    def calc(x,y):
        flag = 0
        for i in range(n):
            if x[i]!=y[i]:
                flag+=1
        if flag==1:
            return True
        else:
            return False
    
    # 문제에서 dfs, bfs가 주어지지 않았다면, 정렬로 시도했을 것 같음 
    # -> 다 돌면서 하나씩 비교해봐야 하나? 아, 그럼 일단 모두에 대해서 cloud를 만들어 둬야 겠다.
    while q:
        w = q.popleft()
        if w == target:
            return c
        tmp = []
        if w in words:
            c = v[words.index(w)] +1
        for i in range(len(words)):
        
            if calc(words[i], w) and v[i]==0:
                v[i] = c
                q.append(words[i])
                tmp.append(words[i])
        
    return answer