#include <iostream>
#include <set>

using namespace std;

int n, k;
int arr[100000];

struct cmp{
    bool operator()(int* a, int*b ){
        return *a > *b ;
    }
};

int main() {
    set<int> S;
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
