#include <iostream>
#include <algorithm>

using namespace std;

class Student {
    public:
        int kor, eng, math;
        string name;
        Student(string name, int kor, int eng, int math) {
            this->name = name;
            this->kor = kor;
            this->eng = eng;
            this->math = math;
        }
        Student(){};
};

bool cmp(const Student &a, const Student &b) { // 총 점수 기준 오름차순 정렬
    return a.kor + a.eng + a.math < b.kor + b.eng + b.math; 
}

int main() {
    int kor, eng, math,n;
    string name;
    cin>>n;
    Student students[n];

    for(int i=0;i<n;++i){
        cin>>name>>kor>>eng>>math;
        students[i] = Student(name,kor,eng,math);
    }

    sort(students, students + n, cmp); // 국어 점수 기준 오름차순 정렬

    for(int i = 0; i < n; i++)
        cout <<students[i].name<<" "<<students[i].kor << " " << students[i].eng << " " << students[i].math << endl;

    return 0;
}
