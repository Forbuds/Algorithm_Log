#include <iostream>
#include <string.h>
#include <stack>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    char s[50];
    cin>>s;
    stack<char> stk;

    for(int i=0;i<strlen(s);i++)
    {
        if(s[i]=='(')
        {
            stk.push(s[i]);

        }
        else
        {
            if(stk.empty())
            {
                printf("No");
                return 0;
            }
            stk.pop();
            
        }
    }
    if(stk.empty()){
        printf("Yes");
    }
    else{
        printf("No");
    }

    return 0;
}