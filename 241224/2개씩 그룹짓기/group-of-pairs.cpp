#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin>>n;
    int arr[2*n];

    for(int i=0;i<2*n;i++){
        cin>>arr[i];
    }

    sort(arr, arr+(2*n));
    printf("%d", arr[n-1]+arr[2*n-1]);

    return 0;
}