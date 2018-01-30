#include<iostream>
#include<fstream>
#include<cmath>
#include<sstream>
#include<string>
using namespace std;

string itos(int &i)
{
       string s;
       stringstream ss(s);
       ss<<i;
       return ss.str();
}

string creat_ID(int const len, int const number)
{
    int n, i, count, temp;
    char const z='0';
    n=len;
    i=number;
    
    count=0;
    temp=i;
    if(temp>9){
                while(temp>9){temp/=10;count++;}
                }
    else temp=0;
    string s;
    if(i>0){
            for(int j=1; j<(n-count); j++){s+=z;}
            s+=itos(i);
           }
            
    else for(int j=0; j<n; j++){s+=z;}
    return s;
    
}

int main()
{
    cout<<creat_ID(10,149);
    system("pause");
}
