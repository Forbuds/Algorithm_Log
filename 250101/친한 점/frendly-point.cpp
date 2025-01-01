/*
#include <iostream>
#include <set>


using namespace std;

struct Human{
    int height, weight;

    Human(int height, int weight){
        this->height = height;
        this->weight = weight;
    }

    Human(){};

};

struct cmp{
    bool operator()(const Human &a, const Human &b){
        return a.height == b.height ? a.weight<b.weight : a.height<b.height;
    }
};

int main() {
    // 여기에 코드를 작성해주세요.
    set<Human, cmp> s;

    int h=165,w=50;
    s.insert( Human(170, 60));
    s.insert( Human(160, 55));
    s.insert( Human(180, 82));
    s.insert( Human(185, 77));
    s.insert( Human(170, 30));
    cout<<s.lower_bound(Human(h,w))->height<<" "<<s.lower_bound(Human(h,w))->weight<<endl;


    return 0;
}

*/
/*
#include <iostream>
#include <set>


using namespace std;

struct Human{
    int height, weight;

    Human(int height, int weight){
        this->height = height;
        this->weight = weight;
    }

    Human(){};

};

struct cmp{
    // bool operator()(const Human &a, const Human &b){
    //     return a.height == b.height ? a.weight<b.weight : a.height<b.height;
    // }
    bool operator()( Human* a,  Human* b){
        return a->height == b->height ? a->weight<b->weight : a->height<b->height;
    }

};

int main() {
    // 여기에 코드를 작성해주세요.
    set<Human*, cmp> s;

    int h=165,w=50;
    
    s.insert(new Human(170, 60));
    s.insert(new Human(160, 55));
    s.insert(new Human(180, 82));
    s.insert(new Human(185, 77));
    s.insert(new Human(170, 30));

    Human* query = new Human(h, w);
    auto it = s.lower_bound(query);

    if (it != s.end()) {
        cout << (*it)->height << " " << (*it)->weight << endl;
    } else {
        cout << "No suitable element found." << endl;
    }

    
    return 0;
}
*/


/*
#include <iostream>
#include <set>

using namespace std;

struct Human{
    int height, weight;
} H[10];

struct cmp{

    bool operator()( Human* a,  Human* b){
        return a->height == b->height ? a->weight<b->weight : a->height<b->height;
    }

};

int main() {
    // 여기에 코드를 작성해주세요.
    set<Human*, cmp> s;

    int h=165,w=50;
    H[0] = {h,w};
    
    int cnt = 1;
    H[cnt++] = {170, 60};
    H[cnt++] = {160, 55};
    H[cnt++] = {180, 82};
    H[cnt++] = {185, 77};
    H[cnt++] = {170, 30};
    cout<<cnt<<endl;
    cout<<H[0].height<<endl;
    cout<<H[1].height<<endl;

    for(int i=1;i<cnt;++i){
        s.insert(&H[i]);
    }

    cout<<s.size()<<endl;
    cout<<(*s.lower_bound(&H[0]))->height<<" "<<(*s.lower_bound(&H[0]))->weight<<endl;
    
    return 0;
}

*/
#include <iostream>
#include <set>

#define MAX_ 100000

using namespace std;

struct Point{
    int x,y;
} p[MAX_+2];

struct cmp{
    bool operator()(Point* a, Point* b){
        return a->x == b->x ? a->y<b->y : a->x<b->x;
    }
};

int main() {
    // 여기에 코드를 작성해주세요.
    int n,m;
    set<Point*, cmp> s;
    cin>>n>>m;
    for(int i=1;i<n+1;++i){
        int x,y;

        cin>>x>>y;
        p[i] = {x,y};
        s.insert(&p[i]);
    }
    for(int i=0;i<m;++i){
        int x,y;
        cin>>x>>y;
        p[0] = {x,y};
        auto it = s.lower_bound(&p[0]);
        if (it == s.end()) cout<<-1<<" "<<-1<<endl;
        else cout<<(*it)->x<<" "<<(*it)->y<<endl;
    }
}