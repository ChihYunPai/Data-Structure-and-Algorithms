#include<iostream>
#include<string>
#include<vector>
#include<fstream>
#include<algorithm>
#include<functional>
using namespace std;

class score
{
      public:
             score(string ID, string Name, double Point) {id=ID,name=Name,point=Point;};
             
             friend bool operator==(const score& s1,const score& s2); 
             friend bool operator<(const score& s1,const score& s2);
             friend bool operator>(const score& s1,const score& s2);
             friend double operator<=(const score& s1,double u);
             friend double operator>=(const score& s1,double u);
             ostream& operator<<(ostream& os, const score& s);
             double getpoint() {return point;};
             
  class       add_number
{
public:
add_number(double n) {value=n;};
double operator()(score &n) {n.point+=value;if(n.point>=100)n.point=100;};
private:
        double value;
};
             
      private:
             string id;
             string name;
             double point;
};
bool operator==(const score& s1,const score& s2)
{return s1.id==s2.id;};
bool operator<(const score& s1,const score& s2)
{return s1.point<s2.point;};
bool operator>(const score& s1,const score& s2)
{return s1.point>s2.point;};
double operator<=(const score& s1,double u)
{return s1.point<=u;};
double operator>=(const score& s1,double u)
{return s1.point>=u;};

ostream& operator<<(ostream& os, const score& s)
{os<<s.id<<s.name<<s.point;
return os ;
};

struct fs
{
            
            bool operator()(score x)
            {if(x>=50.0&&x<=60.0) return 1;}
};

             
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
cout<<"\nBy ID acending.\n";
for (vector<score>::iterator i=v.begin(); i!=v.end();i++) cout<<*i<<endl;

sort(v.begin(), v.end(), greater<score>());
cout<<"\nBy scores descending.\n";
for (vector<score>::iterator i=v.begin(); i!=v.end();i++) cout<<*i<<endl;


cout<<"\nStudents with score between 50 and 60.\n";
vector<score>::iterator p=v.begin();
for (vector<score>::iterator i=v.begin(); i!=v.end();i++)
{
p=find_if(p,v.end(),fs());
if (p!=v.end())
{
cout<<*p<<endl;
p++;
}
}
cout<<"\nAdd by 20 points."<<endl;
for_each(v.begin(),v.end(),score::add_number(20));
for (vector<score>::iterator i=v.begin(); i!=v.end();i++) cout<<*i<<endl;

system("pause");
return 0;
}
