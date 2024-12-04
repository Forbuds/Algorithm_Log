#include <iostream>
#include <string.h>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    char tmp[100];
    while(1)
    {
        if (scanf("%s",tmp)==1)
        {
            for(int i=0;i<strlen(tmp);i++){
                printf("%c",tmp[i]);
            }
            
        }
        else{break;}
    }
    return 0;
}