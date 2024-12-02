#include <iostream>
#include <climits>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    int cnt=0;
    int min = INT_MAX ;

    cin>>n;
    int arr[n];
    
    for(int i=0;i<n;i++)
    {
        scanf("%d ",&arr[i]);
        if (arr[i]<min)
        {
            min = arr[i];
            cnt = 1;
        }
        else if(arr[i] == min)
        {
            cnt+=1;
        }
    }
    cout<<min<<" "<<cnt;

    return 0;
}