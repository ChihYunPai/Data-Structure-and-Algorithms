#include<iostream>
#include<map>
#include<set>

using namespace std;
int main()
{
    /*operator = , begin(), end(), iterator*/
    map<char, int> first;
    map<char, int> second;
    map<char, int>::iterator it;
    map<char, int>::reverse_iterator rit;
    
    first['x']=8;
    first['y']=16;
    first['z']=32;
    
    second=first;
    //first=map<char, int>();
    
    cout<<"Size of first: "<<first.size();
    cout<<"\nSize of second: "<<second.size()<<endl;
    
    cout<<"iterator():\n";
    for(it=first.begin();it!=first.end();it++)
       cout<<(*it).first<<" => "<<(*it).second<<endl;
    
    cout<<"reverse_iterator():\n";
    for(rit=first.rbegin();rit!=first.rend();rit++)
       cout<< rit->first <<" => "<< rit->second <<endl;
    
    cout<<endl;
    /*empty*/
    while(!first.empty())
    {
                         cout<<first.begin()->first<<" => ";
                         cout<<first.begin()->second<<endl;
                         first.erase(first.begin());
                         }
    
    /*size*/
    cout<<"the size of the first map is: "<<first.size()<<endl;
    
    cout<<endl;
    /*max_size*/
    int i;
      map<int,int> mymap;
    
      if (mymap.max_size()>1000)
      {
        for (i=0; i<1000; i++) mymap[i]=0;
        cout << "The map contains 1000 elements.\n";
      }
      else cout << "The map could not hold 1000 elements.\n";
    
    
    /*operator []*/
     
     map<char,string> mymap1;
  
     
  mymap1['a']="an element";
  mymap1['b']="another element";
  mymap1['c']=mymap1['b'];

  cout << "mymap1['a'] is " << mymap1['a'] << endl;
  cout << "mymap1['b'] is " << mymap1['b'] << endl;
  cout << "mymap1['c'] is " << mymap1['c'] << endl;
  cout << "mymap1['d'] is " << mymap1['d'] << endl;
  
    system("pause");
    return 0;
    
    
    
}
                    
