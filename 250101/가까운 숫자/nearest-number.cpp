#include <iostream>
#include <set>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n,k,r,l;
    set<int> s;
    set<int> p;
    p.insert(0);
    cin>>n;
    int ans = 1e9;

    for(int i=0;i<n;++i){
        cin>>k;
        auto it = p.upper_bound(k);

        if(it!=p.end()) {
            ans = min(ans, *it -k);
            }
        it--;
        ans = min(ans,k-*it);
        p.insert(k);
        

        cout<<ans<<endl;
    }
    return 0;
}