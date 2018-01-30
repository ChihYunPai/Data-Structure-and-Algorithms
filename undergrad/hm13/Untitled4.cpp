// map::find
#include <iostream>
#include <map>
using namespace std;

int main ()
{
  map<char,int> mymap;
  map<char,int>::iterator it;

  mymap['a']=50;
  mymap['b']=100;
  mymap['c']=150;
  mymap['d']=200;
  
  it=mymap.find('e');
  cout<<it->second<<endl;
  mymap.erase (it);
  mymap.erase (mymap.find('d'));

  // print content:
  cout << "elements in mymap:" << endl;
  cout << "a => " << mymap.find('a')->second << endl;
  cout << "c => " << mymap.find('c')->second << endl;
  
  /*
  // map::key_comp
  
  map<char,int> mymap;
  map<char,int>::key_compare mycomp;
  map<char,int>::iterator it;
  char highest;

  mycomp = mymap.key_comp();

  mymap['a']=100;
  mymap['b']=200;
  mymap['c']=300;
  mymap['d']=400;

  cout << "mymap contains:\n";
  cout<<mycomp('d','c');
  highest=mymap.rbegin()->first;     // key value of last element

  it=mymap.begin();
  do {
    cout << (*it).first << " => " << (*it).second << endl;
  } while ( mycomp((*it++).first, highest) );

  cout << endl;
*/




  system("pause");
  return 0;
}
