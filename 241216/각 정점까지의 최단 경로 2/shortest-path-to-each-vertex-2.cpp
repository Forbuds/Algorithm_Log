#include <iostream>
#include <climits>
#include <vector>

using namespace std;

typedef pair<int,int> pii;

int main() {
    // 여기에 코드를 작성해주세요.
    int n,m;
    int s,e,c;
    vector<vector<int>> dist(101,vector<int>(101, (int)1e9));


    
    cin>>n>>m;

    for(int i=1;i<n+1;i++){
        dist[i][i] = 0;
    }
    for(int i=0;i<m;i++)
    {
        cin>>s>>e>>c;
        dist[s][e] = min(dist[s][e], c);
    }

    for(int k = 1; k <= n; k++) // 확실하게 거쳐갈 정점을 1번부터 N번까지 순서대로 정의합니다.
        for(int i = 1; i <= n; i++) // 고정된 k에 대해 모든 쌍 (i, j)를 살펴봅니다.
            for(int j = 1; j <= n; j++)
                // i에서 j로 가는 거리가 k를 경유해 가는 것이 더 좋다면
                // dist[i][j]값을 갱신해줍니다.
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);

    for(int i = 1; i <= n; i++) {
        for(int j = 1; j <= n; j++) {
            // 불가능한 경우에는 -1을 출력합니다.
            if(dist[i][j] ==  (int)1e9)
                cout << -1 << " ";
            else
                cout << dist[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}