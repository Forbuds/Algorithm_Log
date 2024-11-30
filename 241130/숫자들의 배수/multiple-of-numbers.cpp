#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int cnt=0;
    int n,tmp;
    cin>>n;

    for(int i=1;i<11;i++){
        tmp = n*i;
        printf("%d ", tmp);
        if (tmp%5 == 0){
            cnt+=1;
            if (cnt==2){
                break;
            }
        }
        
    }

    return 0;
}