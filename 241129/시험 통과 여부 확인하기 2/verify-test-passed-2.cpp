#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    int s;
    int cnt=0;
    cin>>n;

    for(int i=0;i<n;i++){
        int avg=0;
        for(int j=0;j<4;j++){
            cin>>s;
            avg+=s;
        }    
        if(avg/4>=60){
            printf("pass\n");
            cnt+=1;
        }
        else{
            printf("fail\n");
        }
    }
    printf("%d", cnt);
    return 0;
}