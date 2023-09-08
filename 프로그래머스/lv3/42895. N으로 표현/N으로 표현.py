def solution(N, number):
    answer = 0
    # 사용한 횟수로 dp를 만드는 것이 핵심이다.
    dp = [[] for _ in range(9)]
    dp[1] = [N]
    # dp[2] = [11*N , +N, *N, /N, -N ]
    # dp[3] = dp[2] * 
    for k in range(1,9):
        tmp = [int(str(N)*k)]
        for i in range(1,k):
            for x in dp[i]:
                for y in dp[k-i]:
                    tmp.append(x+y)
                    tmp.append(x-y)
                    tmp.append(y-x)
                    tmp.append(x*y)
                    if x!=0:
                        tmp.append(y//x)
                    if y!=0:
                        tmp.append(x//y)
        tmp = list(set(tmp))
        if number in tmp:
            return k
        else:
            dp[k]  = list(set(tmp))
    # print(dp)
        
    
    return -1