#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    char s[100], c;
    int cnt=0,i=0;
    scanf("%[^\n]", s);
    getchar();
    scanf("%c",&c);

    // printf("%c\n",c);
    while(1)
    {
        // printf("%c",s[i]);
        if(s[i] == c){
            cnt+=1;
        }
        if(s[i] == '\0'){
            break;
        }
        i++;
    }
    printf("%d",cnt);
    return 0;
}