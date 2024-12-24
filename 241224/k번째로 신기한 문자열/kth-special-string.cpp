#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n,k;
    vector< string > arr;

    string T;

    cin>>n>>k>>T;

    string s;
    int m=0;

    for(int i=0;i<n;++i)
    {
        cin>>s;
        // printf("%s",s.c_str());
       

        if(s.find(T) == 0){
            arr.push_back(s);
            m ++;
        }
    }
    sort(arr.begin(),arr.end());
    cout<<arr[k-1];


    return 0;
}