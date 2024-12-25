#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

struct PER{
    public:
        string name,id,city;

        PER(string name, string id, string city ){
            this->name = name;
            this->id = id;
            this->city = city;
        }

        PER() {};
};

int cmp(PER a, PER b){

    return a.name>b.name;
}

int main() {
    // 여기에 코드를 작성해주세요.

    int n;
    string name,id,city;
    cin>>n;

    PER arr[n];

    for(int i=0;i<n;i++){
        cin>>name>>id>>city;
        arr[i] = PER(name,id,city);

    }
    sort(arr, arr+n, cmp);

    cout<<"name "<<arr[0].name<<endl;
    cout<<"addr "<<arr[0].id<<endl;
    cout<<"city "<<arr[0].city<<endl;

    return 0;
}