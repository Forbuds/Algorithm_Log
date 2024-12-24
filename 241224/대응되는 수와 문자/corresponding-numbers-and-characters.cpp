#include <iostream>
#include <string>
#include <unordered_map>


using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n,m;

    unordered_map<int,string> mint;
    unordered_map<string,int> mstring;

    cin >> n>>m;
    string c;
    for(int i=1;i<n+1;++i){
        cin>>c;

        mstring[c] = i;
        mint[i] = c;

    }

    for(int i=0; i<m;++i)
    {
        string key;
        cin>>key;

        if('0'<=key[0] && key[0] <='9')
            cout<<mint[stoi(key)]<<endl;

        else
            cout<<mstring[key]<<endl;
    }


    return 0;
}