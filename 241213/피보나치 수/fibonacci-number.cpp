#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin>>n;
    int DP[45]={0,};
    DP[1] = DP[0] = 1;

    if(n<=2) cout<<1;
    else{
        for(int i=2;i<n;i++){
            DP[i] = DP[i-1]+DP[i-2];
        }
        cout<<DP[n-1];
    }
    

    return 0;
}