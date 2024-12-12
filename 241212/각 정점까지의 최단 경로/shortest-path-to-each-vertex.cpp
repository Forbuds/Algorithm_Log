#include <iostream>
#include <queue>
#include <vector>
#include <climits> 

using namespace std;


int n,m,k;

typedef pair<int,int> pii;
priority_queue<pii, vector<pii>, greater<pii>> q;
vector<pii> G[100];

struct Node{
    int v;
    int cost;

};

void dijkstra(vector<vector<pii>> &g)
{
    q.push({0,k});
    int dist[n+1];
    for (int i=1; i<n+1; i++)
    {
        dist[i] = INT_MAX;
    }
    dist[k] = 0;

    while(!q.empty())
    {
        int c = q.top().first;
        int v = q.top().second;
        q.pop();

        if(c>dist[v]) continue;


        for (const pii& neighbor : g[v]) {
            int u = neighbor.first;  // 인접한 정점
            int weight = neighbor.second;  // 간선의 가중치

            if (dist[v] + weight < dist[u]) {
                dist[u] = dist[v] + weight;
                q.push({dist[u], u});  // 갱신된 거리로 큐에 넣기
            }
        }
    }

    for(int i=1;i<n+1;i++)
        {
            if (dist[i] == INT_MAX)
                cout << -1<<endl;
            else
                cout << dist[i] << endl;
            
            
        }
}

int main() {
    // 여기에 코드를 작성해주세요.
    int s,e,c;

    cin>>n>>m;
    cin >>k;
    vector<vector<pii>> G(n + 1);
    
    for(int i=0;i<m;i++)
    {
        cin>>s>>e>>c;
        G[s].push_back({e,c});
        G[e].push_back({s,c});
    }
    dijkstra(G);

    
    
    return 0;
}