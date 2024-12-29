#include <iostream>
#include <set>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    set<int> s;
    string c;
    cin>>n;

    for(int i=0;i<n;++i){
        int num;
        cin>>c;
        if(c == "add"){
            cin>>num;
            s.insert(num);
        }
        else if(c == "remove"){
            cin>>num;
            s.erase(num);
        }
        else if(c == "find"){
            cin>>num;
            if(s.find(num) != s.end()){cout<<"true"<<endl;}
            else{cout<<"false"<<endl;}
        }
        else if(c == "lower_bound"){
            cin>>num;
            if(s.lower_bound(num) != s.end()){cout<<*s.lower_bound(num)<<endl;}
            else{cout<<"None"<<endl;}
        }
        else if(c == "upper_bound"){
            cin>>num;
            if(s.upper_bound(num) != s.end()){cout<<*s.upper_bound(num)<<endl;}
            else{cout<<"None"<<endl;}
        }
        else if(c == "largest"){
            if(s.rbegin() != s.rend()){cout<<*s.rbegin()<<endl;}
            else{cout<<"None"<<endl;}
        }
        else if(c == "smallest"){
            cout<<*s.begin()<<endl;
        }


    }
    return 0;
}