#include <iostream>
using namespace std;

int main() {
    /* 배열 사용하지 않고 피보나치 수열 구하는 법
    int pp=1,p=1;
    for(int i=3;i<11;i++){
        int temp = pp+p;
        pp =p;
        p = temp;
    }
    cout<<p;
    return 0;
    */

    int a,b;
    int arr[10];

    scanf("%d %d", &a,&b);
    arr[0] = a;
    arr[1] = b;
    for (int i=2;i<10;i++){
        arr[i] = arr[i-1]+arr[i-2];
    }
    for(int i=0;i<10;i++){
        printf("%d ",arr[i]%10);
    }
}