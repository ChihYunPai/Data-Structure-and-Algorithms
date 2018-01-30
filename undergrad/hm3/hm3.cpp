#include<iostream>
#include<string>
#include<vector>
#include<fstream>
#include<algorithm>
using namespace std;

class score
{
      public:
             score(string ID, string Name, double Point) {id=ID,name=Name,point=Point;};
             friend bool operator==(const score& s1,const score& s2); 
             friend bool operator<(const score& s1,const score& s2);
             friend ostream& operator<<(ostream& os, const score& s);
             double getpoint() {return point;};
             //~score();
      private:
             string id;
             string name;
             double point;
};
bool operator==(const score& s1,const score& s2)
{return s1.id==s2.id;};
bool operator<(const score& s1,const score& s2)
{return s1.point<s2.point;};
ostream& operator<<(ostream& os, const score& s)
{os<<s.id<<s.name<<s.point;
return os ;};
int main()
{
vector<score> v;
ifstream is("hm3_data.txt");

while (1)
{
string id;
string name;
double point;
is>>id>>name>>point;
if (is) v.push_back(score(id,name,point));
else break;
};

cout<<"The total is "<<v.size()<<" items"<<endl;
for (vector<score>::iterator i=v.begin(); i!=v.end();i++) cout<<*i<<endl;
sort(v.begin(),v.end());
cout<<"After sorting according to point"<<endl;
for (vector<score>::iterator i=v.begin(); i!=v.end();i++) cout<<*i<<endl;


string str;
cin>>str;
vector<score>::iterator
p=find(v.begin(),v.end(),score(str,str,0));
if(p!=v.end()) cout<<"Found "<<str<<" , the point is "<<p->getpoint()<<endl;
else cout<<"Not found"<<endl;
system("pause");
return 0;
}
