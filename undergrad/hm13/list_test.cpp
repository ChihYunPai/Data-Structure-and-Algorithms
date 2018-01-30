#include<iostream>
#include<functional>
#include<list>
using namespace std;

class edge
{
      public:
             edge(){;}
             ostream& operator << (ostream& os, const edge& e)
             {     
                os<<"test123"<<endl;
                return os;
                }
      private:
              string v1,v2;
              double w;
       
};
int main()
{
    
    list<edge> edgelist;
    list<int> list_1;
    list<int>::iterator it;
    for(int i=0;i<5;i++)list_1.push_back(i);
    cout<<"The list contains: ";
    for(it=list_1.begin();it!=list_1.end();it++)
    cout<<" "<<*it;
    
    cout<<endl;
    
    edge e1;
    cout<<"e1:";
    
    system("pause");
    return 0;
    
}
