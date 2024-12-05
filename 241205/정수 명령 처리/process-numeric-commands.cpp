#include <iostream>
#include <string.h>
#include <stack>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    stack<int> s;
    
    scanf("%d",&n);
    for(int i=0;i<=n;i++)
    {
        char str[7] = {0,};
        scanf("%s", str);
        if(strcmp(str,"push")==0){
            int num;
            scanf(" %d",&num);
            s.push(num);
        }
        else if(strcmp(str,"pop")==0)
        {   
            printf("%d\n",s.top());
            s.pop();
        }
        else if(strcmp(str,"size")==0)
        {
            printf("%d\n",s.size());
        }
        else if(strcmp(str,"empty")==0)
        {
            if(s.empty()){
                printf("1\n");
            }
            else{
                printf("0\n");
            }
        }
        else if(strcmp(str,"top")==0)
        {
            printf("%d\n",s.top());
        }
       
    }
    return 0;
}

