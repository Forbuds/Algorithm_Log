#include <iostream>
#include <algorithm>
#include <functional>

using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin>>n;
    int arr1[n],arr2[n];

    for(int i=0;i<n;i++){
        cin>>arr1[i];
    }
    for(int i=0;i<n;i++){
        cin>>arr2[i];
    }

    sort(arr1, arr1+n,greater<int>());
    sort(arr2, arr2+n);
    printf("%d", arr1[n-1]+arr2[n-1]);

    return 0;
}