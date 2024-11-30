#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin>>n;

    int p = 1;
    int tmp;
    printf("%d %d ",p,n);
    for(int i=0;i<20;i++){
        tmp = p+n;
        p = n;
        n = tmp;

        printf("%d ",tmp);
        if (tmp>100){
            break;
        }
    }
    return 0;
}