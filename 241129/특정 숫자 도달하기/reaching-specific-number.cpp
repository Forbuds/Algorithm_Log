#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int arr[10];
    int flag = 0;
    double s=0,avg=0;

    for(int i=0;i<10;i++){
        cin>>arr[i];
        if(arr[i]>=250){
            flag = i;
            break;
        }
        s+=arr[i];
    }
    if (flag){
        cout<<s<<" ";
        printf("%.1lf",s/flag);
    }
    else{
        cout<<s<<" ";
        printf("%.1lf",s/10);
    }
    
    
    return 0;
}