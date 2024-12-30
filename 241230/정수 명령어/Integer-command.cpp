#include <iostream>
#include <set>

using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.

    int T, k, n;
    string code;
    set<int> q;

    cin>>T;
    for(int i=0;i<T;++i){
        cin>> k;
        for(int j=0;j<k;++j){
            cin>>code;
            cin>>n;
            if(code=="I"){
                q.insert(n);
            }
            else if(code=="D"){
                if(q.size() == 0) continue;
                else{
                    if(n==1){
                        q.erase(*q.rbegin());
                    }
                    else{
                        q.erase(*q.begin());
                    }
                }
                
            }
        }
        if(q.size() == 0) cout<<"EMPTY"<<endl;
        else cout<<*q.rbegin()<<" "<<*q.begin()<<endl;
    }
    return 0;
}

