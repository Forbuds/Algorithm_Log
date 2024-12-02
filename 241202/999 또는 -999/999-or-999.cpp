#include <iostream>
#include <climits>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int min=INT_MAX, max=INT_MIN;
    int a;
    while(1)
    {
        cin>>a;
        if(a==999 || a==-999)
        {
            cout<<max<<" "<<min;
            break;
        }
        if(a<min)
        {
            min = a;
        }
        if(max<a)
        {
            max = a;
        }
    }
    return 0;
}