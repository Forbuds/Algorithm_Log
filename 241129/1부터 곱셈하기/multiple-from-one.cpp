#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin>>n;
    int cnt=1; int i=1;

    while(1){
        cnt*=i;
        if(cnt>=n){
            cout<<i;
            break;
        }
        i+=1;

    }


    return 0;
}