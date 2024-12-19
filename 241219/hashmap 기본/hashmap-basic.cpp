#include <iostream>
#include <unordered_map>

using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n,a,b;
    string order;

    cin>>n;

    unordered_map<int,int> m;

    for(int i=0;i<n;++i)
    {
        cin>>order;
        if(order== "add"){
            cin>>a>>b;
            m[a] = b;
        }
        else if(order == "find"){
            cin>>a;
            if(m.find(a) !=m.end()){
                cout<<m[a]<<endl;
            }
            else{
                cout<<"None"<<endl;
            }
        }
        else if(order == "remove"){
            cin>>a;
            m.erase(a);
        }
    }

    return 0;
}