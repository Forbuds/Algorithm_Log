// c++ 풀이! 내가 짠 코드는 이전 코드임

#include <iostream>
#include <stack>
#include <string>

using namespace std;

// 변수 선언
string str;
stack<char> s;  

int main() {
    // 입력:
    cin >> str;

    for(int i = 0; i < (int) str.size(); i++) {
        if(str[i] == '(')
            s.push('(');
        else {
            if(s.empty()) {
                cout << "No";
                return 0;
            }
            s.pop();
        }
    }

    if(s.empty())
        cout << "Yes";
    else
        cout << "No";
    return 0;
}