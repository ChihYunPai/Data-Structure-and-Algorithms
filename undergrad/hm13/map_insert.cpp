// map::insert
#include <iostream>
#include <map>
#include <set>
using namespace std;

int main ()
{
    map< string,set<string> > mpp;
    map< string,set<string> >::iterator mppit;
    set<string>::iterator setit;
    
    mpp["1"];
    mppit=mpp.find("1");
    (*mppit).second.insert("3");
    mpp["2"];
    mppit=mpp.find("1");
    (*mppit).second.insert("4");
    for(mppit=mpp.begin();mppit!=mpp.end();mppit++)
    {
       cout<<(*mppit).first<<" => ";
       for(setit=(*mppit).second.begin();setit!=(*mppit).second.end();setit++)
       cout<<" "<<*setit;
       cout<<endl;
       }
       
    
  map<char,int> mymap;
  map<char,int>::iterator it;
  pair<map<char,int>::iterator,bool> ret;

  // first insert function version (single parameter):
  mymap.insert ( pair<char,int>('a',100) );
  mymap.insert ( pair<char,int>('a',200) );
  ret=mymap.insert ( pair<char,int>('z',500) ); 
  
  if (ret.second==false)
  {
    cout << "element 'z' already existed";
    cout << " with a value of " << ret.first->second << endl;
  }

  // second insert function version (with hint position):
  it=mymap.end();
  mymap.insert (it, pair<char,int>('b',300));  // max efficiency inserting
  it++;
  mymap.insert (it, pair<char,int>('c',400));  // no max efficiency inserting

  // third insert function version (range insertion):
  map<char,int> anothermap;
  anothermap.insert(mymap.begin(),mymap.find('c'));

  // showing contents:
  cout << "mymap contains:\n";
  for ( it=mymap.begin() ; it != mymap.end(); it++ )
    cout << (*it).first << " => " << (*it).second << endl;

  cout << "anothermap contains:\n";
  for ( it=anothermap.begin() ; it != anothermap.end(); it++ )
    cout << (*it).first << " => " << (*it).second << endl;
    system("pause");
  return 0;
}
