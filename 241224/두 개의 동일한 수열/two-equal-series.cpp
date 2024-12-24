#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    int a1[n],a2[n];

    for(int i=0;i<n;i++){
        cin>>a1[i];
    }
    for(int i=0;i<n;i++){
        cin>>a2[i];
    }

    sort(a1,a1+n);
    sort(a2,a2+n);

    bool B = 1;
    for(int i=0;i<n;i++){
        if (a1[i] != a2[i]) B = 0;

    }

    if(B){printf("Yes");}
    else{
        printf("No");
    }
    return 0;
}