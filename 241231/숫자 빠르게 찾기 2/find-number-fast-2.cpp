#include <iostream>
#include <set>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    set<int> s;
    int n,m,k;

    cin>>n>>m;
    for(int i=0;i<n;++i){
        cin>>k;
        s.insert(k);
    }
    for(int i=0;i<m;++i){
        cin>>k;
        if(s.lower_bound(k) == s.end())
            cout<<-1<<endl;
        else
            cout<< *s.lower_bound(k)<<endl;
    }



    return 0;
}