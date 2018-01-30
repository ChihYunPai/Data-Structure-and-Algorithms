#include<iostream>
#include<set>
using namespace std;
int main()
{
    /*begin, end, rbegin, rend, iterator, riterator */
    int myints[]={ 2, 10, 7, 46, 80, 26};
    set<int> first(myints, myints+6);
    set<int> second;
    second = first;
    first=set<int>();
    
    set<int>::iterator it;
    set<int>::reverse_iterator rit;
    
    cout<<"myint contains(iterator): ";
    for(it=second.begin();it!=second.end();it++)
      cout<<" "<<*it;
    cout<<endl;
    
    cout<<"myint contains(reverse_iterator): ";
    for(rit=second.rbegin();rit!=second.rend();rit++)
      cout<<" "<<*rit;
    cout<<endl;
    
    /*size()*/
    cout<<"Size of first: "<<first.size()<<endl;
    cout<<"Size of second: "<<second.size()<<endl;
    
    /*insert()*/
    set<int> myset;
    myset.insert(20);
    myset.insert(10);
    myset.insert(30);
    
    cout<<"myset contains:";
    while(!myset.empty())
    {
       cout<<" "<<*myset.begin();
       myset.erase(myset.begin());
       }
    cout<<endl;
    
    /*swap()*/
    set<int> f1(myints,myints+3);
    set<int> f2(myints+3,myints+6);
    
    f1.swap(f2);
    
    cout<<"first.contains:";
    for(it=f1.begin();it!=f1.end();it++)cout<<" "<<*it;
    
    cout<<"\nsecond.contains:";
    for(it=f2.begin();it!=f2.end();it++)cout<<" "<<*it;
    
    cout<<endl;
    
    /*max_size()*/
    int i;
    set<int> myset2;
    if(myset2.max_size()>10000)
    {
        for(i=0; i<1002; i++)myset2.insert(i);
        cout<<"The set constains 1000 elements.\n";
        }
    else cout<<"The set could not hold 1000 elements.\n";
    
    /*clear*/
    myset.insert(100);
    myset.insert(200);
    myset.insert(300);
    
    cout<<"myset contains:";
    for(it=myset.begin();it!=myset.end();it++)
       cout<<" "<<*it;
    cout<<endl;
    myset.clear();
    myset.insert(11010);
    myset.insert(200020);
    for(it=myset.begin();it!=myset.end();it++)
       cout<<" "<<*it;
       
    cout<<endl;
    
    /*key_comp*/
    set<int> myset3;
    set<int>::key_compare mycomp;
    int highest;
    
    mycomp=myset.key_comp();
    
    for(i=0; i<5; i++)myset.insert(i);
    cout<<"myset contains:";
    highest=*myset.rbegin();
    cout<<"\nthe highest:"<<highest<<endl;
    it=myset.begin();
    do{
                     cout<<" "<<*it;
                     }
    
    while(  /*??*/mycomp(*it++,highest)  );
    
    cout<<endl;
    
    /*find()*/
    set<int> myset4;
    for(int i=1; i<=5; i++)myset4.insert(i*10);
    
    it=myset4.find(20);
    myset4.erase(it);
    myset4.erase(myset4.find(40));
    cout<<"myset contains:";
    for(it=myset4.begin();it!=myset4.end();it++)
       cout<<" "<<*it;
       
    cout<<endl;
    
    /*count*/
    for(i=1;i<=5;i++)myset.insert(i*3);
    
    for(i=0;i<=10;i++)
    {
                      cout<<i;
                      if(myset.count(i)>0)
                      cout<<" is an element of myset.\n";
                      else 
                      cout<<" is not an element of myset.\n";
     }

    system("pause");
    return 0;
    
}
                    
