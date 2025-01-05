#include <iostream>
#include <set>

using namespace std;

int n, k;
int arr[100000];
set<int> S;

int main() {
    
    cin >> n >> k;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
        S.insert(-arr[i]);
    }

    // Write your code here!
    auto t = S.begin();
    for(int i=0;i<k;++i){
        cout<<-*t<<" ";
        t++;
    }

    return 0;
}