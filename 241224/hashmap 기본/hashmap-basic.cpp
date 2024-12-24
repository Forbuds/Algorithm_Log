#include <iostream>
#include<string>
#include<unordered_map>

using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    /*
    m.find(K) != m.end() // 값이 있는 경우
    m.find(K) == m.end() // 값이 있는 경우, 이터레이터 반환
    */
    unordered_map<int,int> m;
    int n,a,b;
    string k;

    cin>> n;

    for(int i=0;i<n;i++)
    {
        cin>>k;
        if(k=="add")
        {
            cin>>a>>b;
            m[a] = b;

        }
        else if(k=="remove")
        {
            cin>>a;
            m.erase(a);
        }
        else if(k == "find")
        {
            cin>>a;
            if (m.find(a) == m.end())
            {
                printf("None\n");
            }
            else{
                printf("%d\n",(m.find(a))->second);
                // printf("%d\n",m[a]);
            }
        }

    }


    
    return 0;
}