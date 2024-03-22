def solution(triangle):
    answer = 0
    n = len(triangle)
    for l in range(n-2,-1,-1):
        # print(l)
        # print(triangle[l])
        for i in range(len(triangle[l])):
            triangle[l][i] += max( triangle[l+1][i], triangle[l+1][i+1])
    # print(triangle)
    return triangle[0][0] 