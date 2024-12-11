#include <iostream>

#define MAX_N 100000
using namespace std;

int n,m;
int uf[MAX_N +1];

int Find(int x)
{
    if (uf[x] == x) return x;
    return uf[x] = Find(uf[x]);
    //x가 루트라면 그대로 루트 반환
    // x가 아니라면 find 찿아서 (경로 압축) ㅌrk 루트로 바로 가도록
}

void Union(int x, int y)
{
    int X = Find(x);
    int Y = Find(y);
    uf[X] = Y;
}
int main() {
    // 여기에 코드를 작성해주세요.

    cin >> n >> m;

    // 초기 uf 값을 설정합니다.
    for(int i = 1; i <= n; i++)
        uf[i] = i;



    while(m--){
        int q_type,a,b;
        cin>>q_type>>a>>b;
        // 합치는 명령입니다.
        if(q_type == 0)
            Union(a, b);
        // 같은 집합에 있는지를 판단하는 명령입니다.
        else {
            // 같은 집합인 경우에는 1을 출력합니다.
            if(Find(a) == Find(b))
                cout << 1 << endl;
            else
                cout << 0 << endl;
        }

    }
    return 0;
}