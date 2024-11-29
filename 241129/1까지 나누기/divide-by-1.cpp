#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin>>n;
    int i=1;
    int result = n;
    int cnt =0;

    while(1){

        n=n/i;
        cnt+=1;
        
        if(n<=1){
            cout<<cnt;
            break;

        }
        i+=1;

    }


    return 0;
}