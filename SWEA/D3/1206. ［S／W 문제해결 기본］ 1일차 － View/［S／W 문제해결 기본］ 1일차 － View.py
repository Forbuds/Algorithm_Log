T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    n = int(input())
    arr = list(map(int, input().strip().split()))
    result = 0
    for i in range(2, n-2):
        result += max(arr[i]- max(arr[i-2],arr[i-1], arr[i+1],arr[i+2]),0)
    print(f'#{test_case} {result}')