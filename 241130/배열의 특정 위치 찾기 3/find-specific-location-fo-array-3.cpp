#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int arr[100];
    int tmp;

    for(int i=0;i<100;i++){
        scanf("%d",&tmp);
        if(tmp == 0){
            printf("%d", arr[i-1]+arr[i-2]+arr[i-3]);
            break;
        }
        arr[i] = tmp;
    }
    return 0;
}