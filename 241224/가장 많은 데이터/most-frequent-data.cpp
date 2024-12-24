#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.

    int n, max_n;
    unordered_map<string, int> m;

    cin>>n;

    for(int i=0;i<n;++i){
        string q;
        cin>>q;

        if(m.find(q) == m.end()){
            // 없는 경우
            m[q] = 1;
        }
        else{
            m[q] +=1;
            max_n = max(max_n, m[q]);
        }

    }
    cout<<max_n;
    return 0;
}