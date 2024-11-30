#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int s=0;
    int avg = 0;
    int arr[10];
    int tmp;
    int cnt = 0;

    for(int i=0;i<10;i++){
        scanf("%d",&tmp);
        arr[i] = tmp;
        if(i%2==1){
            s+= tmp;
        }
        if((i+1)%3==0){
            cnt+=1;
            avg+=tmp;
        }
    }
    printf("%d %.1lf",s,double(avg)/cnt);


    return 0;
}