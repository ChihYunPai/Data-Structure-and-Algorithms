// map::insert
#include <iostream>
#include <map>
using namespace std;

int main ()
{
    map<char,int> mymap;
    map<char,int>::iterator it;
    pair<  map<char,int>::iterator, bool  > ret;
    
    mymap.insert( pair<char,int>('a',100) );
    mymap.insert( pair<char,int>('z',200) );
    ret=mymap.insert( pair<char,int>('z',500) );
    if(ret.second==false)
    {
                        cout<<"element 'z' already exsited";
                        cout<<"with a value of "<<ret.first->second<<endl;
    }
    
    system("pause");
    return 0;
}
