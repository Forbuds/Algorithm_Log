#include <iostream>
#include <string>

using namespace std;

struct prod{
    public:
        string name;
        int code;

        prod(string name="codetree", int code=50 ){
            this->name = name;
            this->code = code;
        }

};

int main() {
    // 여기에 코드를 작성해주세요.
    string name;
    int code;

    cin>>name>>code;
    
    prod P = prod();
    cout<<"product "<<P.code<<" is "<<P.name<<endl;
    prod P1 = prod(name, code);
    cout<<"product "<<P1.code<<" is "<<P1.name<<endl;



    return 0;
}