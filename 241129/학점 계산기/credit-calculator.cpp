#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    double arr[5];

    cin>>n;
    for(int i=0;i<n;i++){
        scanf("%lf",&arr[i]);
    }

    double avg = 0;
    for(int i=0;i<n;i++){
        avg+= arr[i];
    }
    avg = avg/n;
    printf("%.1lf\n",avg);

    if(avg>=4){
        printf("Perfect");
    }
    else if(avg>=3){
        printf("Good");
    }
    else{
        printf("Poor");
    }



    return 0;
}