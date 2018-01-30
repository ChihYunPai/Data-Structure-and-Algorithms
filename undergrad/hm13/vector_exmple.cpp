#include<iostream>
#include<vector>
using namespace std;
int main()
{
    vector<int> vec(6);
    vector<int>::iterator it;
    vector<int>::reverse_iterator rit;
    for(it=vec.begin();it!=vec.end();it++)
    cout<<*it<<endl;
    
    vec.clear();
    
    for(int i=0;i<5;i++) vec.push_back(i);
    cout<<"vec reverse_iterator:";
    for(rit=vec.rbegin();rit<vec.rend();rit++)cout<<" "<<*rit;
    cout<<endl<<endl;
    
    vector<int> myvec;
    
    for(int i=0; i<100; i++) myvec.push_back(i);
    
    cout<<"size: "<<myvec.size()<<endl;
    cout<<"capacity: "<<myvec.capacity()<<endl;
    cout<<"max_size: "<<myvec.max_size()<<endl;
    
    
    
    system("pause");
    return 0;
    
}
                    
