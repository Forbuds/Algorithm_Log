#include <iostream>
#include <string>

using namespace std;

struct Bomb{

    public:
        int sec;
        string code, color;

        Bomb(string code, string color, int sec){
            this->code = code;
            this->color = color;
            this->sec = sec;
        }

        Bomb(){};

};


int main() {
    // 여기에 코드를 작성해주세요.
    int sec;
    string code, color;

    cin>>code>>color>>sec;

    Bomb b = Bomb(code, color, sec);

    cout<<"code : "<<code<<endl;
    cout<<"color : "<<color<<endl;
    cout<<"second : "<<sec<<endl;

    return 0;
}