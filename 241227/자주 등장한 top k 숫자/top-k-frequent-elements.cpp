#include <iostream>
#include <unordered_map>
#include <algorithm>
#include <vector>

using namespace std;

int n,k;
int arr[100000];
unordered_map<int,int> freq;
vector<pair<int,int>> v;


int main() {
    // 여기에 코드를 작성해주세요

    cin>>n>>k;
    int arr[n];

    for (int i=0;i<n;++i){
        cin>>arr[i];
        freq[arr[i]]++;
    }

    for(unordered_map<int,int>::iterator it = freq.begin(); // 형식의 이터레이터 it=처음
        it != freq.end(); // it=끝이 아닐때까지
        it++){
        v.push_back({it->second,it->first});    // 동적 할당이 필요하기 때문에 vector
    }

    sort(v.begin(),v.end());

    for(int i=(int)v.size()-1;i>=(int)v.size() - k; i--)
        cout<< v[i].second << " ";

    return 0;
}