//istream test
#include<iostream>
#include<fstream>
#include<map>
using namespace std;
struct edge
{
       string v1, v2;
       double w;
};


int main()
{
    map<string,edge> edgemap;
    map<string,edge>::iterator it;
    int vertcnt;
    map<string,edge> mymap;
    edge e;
    ifstream is("hm13_data.txt");
    if(is)cout<<"good"<<endl;
    
    is>>vertcnt;
    while(1)
    {
            if(is)
            {
                  is>>e.v1>>e.v2>>e.w;
                  mymap.insert ( pair<string,edge>("a",e) );
                  //mymap.insert ("a",e);
                  }
            else break;
    }
    
    system("pause");
    return 0;
    
}
    
    
