#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin>>n;
    int arr[n];
    int num[10] = {0,};
    int tmp;

    for(int i=0;i<n;i++)
    {
        scanf("%d ", &tmp);
        num[tmp] +=1;
    }
    for(int i=1;i<10;i++)
    {
        printf("%d\n",num[i]);
    }
    return 0;
}