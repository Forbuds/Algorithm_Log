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

    for(int i=0;i<n;++i){
        cin>>k;
        p.insert(k);
        auto it = p.upper_bound(k);

        if(it!=p.end()) {
            //cout<<*it<<' ';
            r = *it;
            it--;
            //cout<<*it<<' ';
            l = *it;
        }
        

        
        if(r!=k) s.insert(r-k);
        if(l!=k) s.insert(k-l);

        cout<<*s.begin()<<endl;
    }
    return 0;
}