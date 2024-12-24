#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

class Agent{
    public:
        string code; int n;

        Agent(string code, int n){
            this->code = code;
            this->n = n;
        }

        Agent() {};


};

int cmp(Agent a,Agent b){
    return a.n < b.n;
}

int main() {
    // 여기에 코드를 작성해주세요.
    string code;
    int n;
    Agent arr[5];
    for(int i=0;i<5;++i){
        cin>>code>>n;
        arr[i] = Agent(code,n);
    }


    sort(arr,arr+5,cmp);

    cout<<arr[0].code<<" "<< arr[0].n;
    return 0;
}