#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    scanf("%d",&n);
    int arr[n];
    int tmp;

    for (int i=0;i<n;i++){
        scanf("%d", &tmp);
        arr[i] = tmp*tmp;
    }

    for(int i=0;i<n;i++){
        printf("%d ",arr[i]);
    }
    return 0;
}