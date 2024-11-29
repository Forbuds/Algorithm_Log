#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int arr[10];
    int tmp;
    int cnt=0;
    int s = 0;

    for(int i=0;i<10;i++){
        scanf("%d",&tmp);
        if(tmp==0 || i==9){
            printf("%d %d",cnt,s);
        }
        if(tmp%2==0){
            cnt+=1;
            s+=tmp;
        }
    }
    return 0;
}