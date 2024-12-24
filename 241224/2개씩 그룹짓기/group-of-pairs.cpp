#include <iostream>
#include <algorithm>
#include <functional>

using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin>>n;
    int arr1[2*n];

    for(int i=0;i<2*n;i++){
        cin>>arr1[i];
    }
    int group_max = 0;
    int s;
    sort(arr1, arr1+2*n);
    for(int i=0;i<2*n;i++){
        s = arr1[i] + arr1[2*n-1-i];
        group_max = max(s, group_max);
    }
    printf("%d", group_max);

    

    return 0;
}