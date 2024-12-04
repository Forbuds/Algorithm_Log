#include <stdio.h>
#include <string.h>

int main() {
    // 여기에 코드를 작성해주세요.
    char a[20],b[20];
    scanf("%s %s",a,b);
    if(strlen(a)>strlen(b)){
        printf("%s %d",a,strlen(a));
    }
    else if(strlen(a)<strlen(b)){
        printf("%s %d",b,strlen(b));
    }
    else{
        printf("same");
    }
    
    return 0;
}