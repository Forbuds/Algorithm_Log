#include <iostream>
#include <string>
#include <algorithm>


using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.

    string s1,s2;

    cin>>s1;
    cin>>s2;

    sort(s1.begin(),s1.end());
    sort(s2.begin(),s2.end());
    
    if(s1 == s2){
        printf("Yes");
    }
    else
        printf("No");

    return 0;
}