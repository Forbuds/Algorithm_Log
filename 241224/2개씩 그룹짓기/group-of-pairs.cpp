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

    sort(arr1, arr1+n,greater<int>());
    sort(arr1+n, arr1+2*n);
    printf("%d", arr1[n-1]+arr1[2*n-1]);

    return 0;
}