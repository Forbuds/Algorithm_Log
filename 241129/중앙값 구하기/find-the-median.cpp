#include <iostream>
#include<algorithm>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int arr[3];
    for(int i=0;i<3;i++){
        cin>>arr[i];
    }
    sort(arr,arr+3);
    cout<<arr[1];

    return 0;
}