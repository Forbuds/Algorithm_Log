#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

struct PER{
    public:
        string name;
        int h,w;
        PER(string name, int h, int w){
            this->name = name;
            this->h = h;
            this->w = w;
        }
        PER(){};
};

int cmp(const PER &A, const PER &B){
    return A.h<B.h;
}

int main() {
    // 여기에 코드를 작성해주세요.
    string name;
    int h,w;
    int n;
    cin>>n;
    PER arr[n];


    for(int i=0;i<n;i++){
        cin>>name>>h>>w;
        arr[i] = PER(name,h,w);
    }
    sort(arr, arr+5, cmp);
    for(int i=0;i<n;i++){
        cout<<arr[i].name<<" "<<arr[i].h<<" "<<arr[i].w<<endl;;
    }
    return 0;
}