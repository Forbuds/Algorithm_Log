#include <iostream>
#include <string>


using namespace std;

class USER{
    public:
        string ID;
        int LV;

        USER(string ID="codetree", int LV=10){
            this->ID = ID;
            this->LV = LV;
        }
};

int main() {
    // 여기에 코드를 작성해주세요.

    string ID;
    int LV;

    cin>>ID>>LV;
    USER defalt = USER();
    USER modi = USER(ID,LV);

    cout<<"user "<<defalt.ID<<" lv "<<defalt.LV<<endl;
    cout<<"user "<<modi.ID<<" lv "<<modi.LV;
    
    return 0;
}