#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

struct STU{
    public:
        string name;
        int kor, eng, math;
        STU(string name, int kor, int eng, int math){
            this->name = name;
            this->kor = kor;
            this->eng = eng;
            this->math = math;
        }
        STU(){};
};

int cmp(const STU &a, const STU &b){
    if (a.kor == b.kor){
        if(a.eng == b.eng){
            return a.math>b.math;
        }
        return a.eng>b.eng;
    }
    return a.kor>b.kor;
}

int main() {
    // 여기에 코드를 작성해주세요.
    string name;
    int kor, eng, math,n;
    cin>>n;
    STU arr[n];

    for(int i=0;i<n;i++){
        cin>>name>>kor>>eng>>math;
        arr[i] = STU(name,kor,eng,math);
    }
    sort(arr,arr+n,cmp);
    for(int i=0;i<n;i++){
        cout<<arr[i].name<<" "<<arr[i].kor<<" "<<arr[i].eng<<" "<<arr[i].math<<endl;
    }


    return 0;
}