#include <iostream>
#include <set>

using namespace std;

int n, k;
long long arr[100000];


int main() {
    set<long long> S;
    cin >> n >> k;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
        S.insert(arr[i]);
    }

    // Write your code here!
    auto t = S.rbegin();
    for(int i=0;i<k;++i){
        cout<<*t<<" ";
        t--;
    }

    return 0;
}