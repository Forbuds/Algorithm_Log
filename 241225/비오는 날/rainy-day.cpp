#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

struct DATA{
    public:
        string cal, day, weather;

        DATA(string cal, string day, string weather){
            this->cal = cal;
            this->day = day;
            this->weather = weather;
        };

        DATA() {};
};

int cmp(DATA a, DATA b){
    return a.cal<b.cal;
};
int main() {
    // 여기에 코드를 작성해주세요.

    string cal, day, weather;
    int n;
    cin>>n;
    DATA arr[n];
    
    for(int i=0;i<n;++i){
        cin>>cal>>day>>weather;

        if(weather!="Rain") cal = "2100-12-12";
        arr[i] = DATA(cal, day, weather);
    }

    sort(arr, arr+n, cmp);

    cout<<arr[0].cal<<" "<<arr[0].day<<" "<<arr[0].weather;

    return 0;
}