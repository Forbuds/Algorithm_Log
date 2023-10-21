def solution(sizes):
    x,y=0,0
    for i,j in sizes:
        i,j = max(i,j),min(i,j)
        if x<i:
            x=i
        if y<j:
            y=j
    return x*y