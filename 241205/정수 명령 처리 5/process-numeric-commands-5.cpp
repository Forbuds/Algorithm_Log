#include <iostream>
#include <vector>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    vector<int> v;

    int T;
    string s;
    scanf("%d",&T);

    for(int i=0;i<T;i++)
    {
        cin>>s;
        if(s=="push_back")
        {
            int n;
            cin>>n;
            v.push_back(n);
        }
        else if(s=="pop_back")
        {
            v.pop_back();
        }
        else if(s=="size")
        {
            //printf("%d\n",v.size());
            cout<<v.size()<<"\n";
        }
        else if(s=="get")
        {
            int n;
            cin>>n;
            printf("%d\n",v[n-1]);
        }
    }
    return 0;
}