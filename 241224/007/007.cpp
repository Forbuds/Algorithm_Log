#include <iostream>
#include <string>
using namespace std;
class PRI{
    public:
    int time;
    string code,p;

    PRI(string code,string p,int time){
        this->code = code;
        this->p = p;
        this->time=time;
    }
};

int main() {
    // 여기에 코드를 작성해주세요.
    string code,p;
    int time;

    cin>>code>>p>>time;
    PRI pri = PRI(code,p,time);
    cout<<"secret code : "<<pri.code<<endl;
    cout<<"meeting point : "<<pri.p<<endl;
    cout<<"time : "<<pri.time<<endl;

    
    return 0;
}