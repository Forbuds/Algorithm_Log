#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int arr[100];
    int tmp,c;

    for(int i=0;i<100;i++){
        scanf("%d",&tmp);
        if(tmp==0){
            c = i;
            break;
        }
        arr[i] = tmp;
    }
    for (int i=0;i<c;i++){
        tmp = arr[i];
        if(tmp%2==1){
            printf("%d ",tmp+3);
        }
        else{
            printf("%d ",tmp/2);
        }
    }
    return 0;
}