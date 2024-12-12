#include <iostream>
#include <queue>
#include <vector>
#include <climits> 

using namespace std;


int n,m;

typedef pair<int,int> pii;
priority_queue<pii, vector<pii>, greater<pii>> q;
vector<pii> G[100];

struct Node{
    int v;
    int cost;

};

void dijkstra(vector<vector<pii>> &g, int source)
{
    q.push({0,1});
    int dist[n+1];
    for (int i=1; i<n+1; i++)
    {
        dist[i] = INT_MAX;
    }
    dist[1] = 0;

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

    if (dist[source] == INT_MAX)
        cout << "INF "<<endl;
    else
        cout << dist[source] << endl;
        
}

int main() {
    // 여기에 코드를 작성해주세요.
    int s,e,c;

    cin>>n>>m;

    vector<vector<pii>> G(n + 1);
    
    for(int i=0;i<m;i++)
    {
        cin>>s>>e>>c;
        G[s].push_back({e,c});
    }
    
    for(int i=2;i<n+1;i++)
    {
        dijkstra(G,i);
        
    }
    return 0;
}