#include <iostream>
#include <unordered_map>

using namespace std;
#define MAX_N = 100000;

int main() {
    // 여기에 코드를 작성해주세요.
    unordered_map<int,int> map;
    int n,m,k,q;

    cin>>n>>m;


    for(int i=0;i<n;++i){
        cin>>k;
        if(map.find(k) !=map.end())
        {
            map[k] +=1;
        }
        else{
            map[k] = 1;
        }
    }

    for(int i=0;i<m;++i){
        cin>>q;
        printf("%d ",map[q]);
    }



    return 0;
}