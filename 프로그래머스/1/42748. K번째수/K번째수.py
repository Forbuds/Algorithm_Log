def solution(arr, commands):
    answer = []
    
    for i,j,k in commands:
        print(i,j,k)
        # print(sorted(arr[i-1:j-1+1]))
        answer.append(sorted(arr[i-1:j-1+1])[k-1])
    return answer