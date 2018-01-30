#include<iostream>
#include<fstream>
#include<string>
#include<sstream>
#include<cmath>
using namespace std;
string itos(int &i)
{
       string s;
       stringstream ss(s);
       ss<<i;
       return ss.str();
}
       
int main()
{
    int n;
    string s;
    cin>>n;
    while(1)
    {
            cin>>n;
            s=itos(n);
            cout<<s<<endl;
            
    }
    char const z='0';
    for(int i=0; i<n; i++)
    {
            s+=z;
    }
    cout<<s;
    
    system("pause");
}
