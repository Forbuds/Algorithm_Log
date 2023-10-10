def rotate_arr(arr):
    '''
    종이를 준비한다. 돌려준다.
    앞에는 멀쩡한 배열을, 옆에는 돌린 배열을 그려준다. 각 행과 열에는 행 번호와 열 번호가 쓰여 있다.

    시계방향 : 90도
    0,0 | 0,1 | 0,2            *2,0 | 1,0 | 0,0
    1,0 | 1,1 | 1,2     ==      2,1 | 1,1 | 0,1
    2,0 | 2,1 | 2,2             2,2 | 1,2 | 0,2

    행과 열이 뒤바뀐다. (90도라서)
    *를 보고 판단한다.
    행은  = 열의 반대로 뒤집은 형태 : n-1-y
    열은  = 행 x
    '''
    n = len(arr)
    arr_new = [[0]*(n) for _ in range(n)]
    for x in range(n):
        for y in range(n):
            # new_arr.append([y,n-1-x])
            arr_new[y][n-1-x]= arr[x][y]
    return arr_new
def rotate(arr):
    '''
    arr[::-1]로 [7,8,9],[4,5,6],[1,2,3] 만든다.
    *arr[::-1] 로 이터레이터를 만들어 준다.
    zip() 으로 (7,4,1),(8,5,2),(9,6,3) 을 만든다.
    위에는 튜플이니까 map(list, 튜플) 로 한번에 list 적용해준다.
    list로 감싸서 대괄호 만들어 준다.
    '''
    arr = list(map(list,zip(*arr[::-1])))
    return arr


arr = [[1,2,3],[4,5,6],[7,8,9]]

print(rotate_arr(arr))
print(rotate(arr))
# [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
# [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
