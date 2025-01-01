#include <iostream>
#include <set>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    set<int> s;
    int n,m,k;
    cin>>n>>m;

    for(int i=1;i<m+1;++i){
        s.insert(i);
    }

    for(int i=0;i<n;++i){
        cin>>k;
        s.erase(k);
        cout<<*s.rbegin()<<endl;
    }
    return 0;
}