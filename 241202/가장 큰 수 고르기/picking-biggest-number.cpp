#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int arr[10];
    
    int max = 0;

    for(int i=0;i<10;i++)
    {
        scanf("%d ",&arr[i]);
        if (max<arr[i])
        {
            max = arr[i];
        }
    }
    cout<<max;

    return 0;
}