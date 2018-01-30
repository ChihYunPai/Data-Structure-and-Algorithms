#include<iostream>
#include<fstream>
#include<stdlib.h>
#include<string>
#include<set>
#include<map>
#include<list>
#include<queue>
struct edge
{
       
       int v1,v2;
       double w;
       
       
};
using namespace std;
int main()
{
    
    set<string> myset;
    set<string>::iterator it;
    string s1="1";
    string s2="2";
    string s3="3";
    myset.insert(s1);
    myset.insert(s2);
    myset.insert(s3);
    /*for(it=myset.begin();it!=myset.end();it++)
    cout<<" "<<*it;*/
    
    map< string, set<string> > mymap;
    map< string, set<string> >::iterator mymapit;
    mymapit=mymap.begin();
    mymap.insert( mymapit, pair< string,set<string> >("1",myset) );
    cout<<(*mymapit).first<<endl;
    for(mymapit!=mymap.begin();mymapit!=mymap.end();mymapit++)
    {
       cout<<(*mymapit).first<<" => ";
       for(it=myset.begin();it!=myset.end();it++)
       cout<<" "<<*it;
       }
    
    

     
     system("pause");
     return 0;
     
}
