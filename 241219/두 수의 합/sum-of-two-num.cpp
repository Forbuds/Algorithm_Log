#include <iostream>
#include <unordered_map>
using namespace std;


int main() {
    // 여기에 코드를 작성해주세요.
    int n,k,a,cnt=0;
    cin>>n>>k;
    unordered_map<int,int> m;
    for(int i=0;i<n;i++)
    {
        cin>>a;
        m[a] = k-a;
        if(m.find(k-a) != m.end()) cnt++;
            }
    cout<<cnt;
    return 0;
}