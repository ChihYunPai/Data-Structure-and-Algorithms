#include <iostream>
#include <algorithm>
#include <math.h>
#define threshold 3
using namespace std;
typedef unsigned long int large_integer;

template <class T>
int numDigits(T number)
{
    int digits = 0;
    if (number<=0) digits = 1;
    while(number>0) {
        number /= 10;
        digits++;
    }
    return digits;
}
template <class T>
int power(T number)
{
    int digits = 10;
    if (number==1) digits = 10;
    while(number>1) {
        number--;
        digits*=10;
    }
    return digits;
}

large_integer prod(large_integer u, large_integer v)
{
  large_integer x,y,w,z,r,p,q;
  int n,m;
  
  n = max( numDigits(u), numDigits(v) );
  if(u==0||v==0)return 0;
  else if(n<=threshold)return u*v;
  else{
       m=(n/2);
       x=u/power(m);       y=u%power(m);
       w=v/power(m);       z=v%power(m);
       r=prod(x+y,w+z);
       p=prod(x,w);
       q=prod(y,z);
       return p*power(2*m) + (r-p-q)*power(m) + q;
       }
}

int main()
{
    large_integer a,b;
    cout<<"/**** Project#2_1: Large Integer Multiplication ****/"<<endl;
    cout<<"/****             作者: B9827115白植允          ****/"<<endl;
    cout<<"/****        輸入:a, b 整數  輸出:a*b結果       ****/"<<endl;
    cout<<"/****乘積大於45億須改成更大空間的large_integer  ****/"<<endl<<endl;
    
    while(1)
    {
    cout<<"Input a: ";cin>>a;cout<<endl;
    cout<<"Input b: ";cin>>b;cout<<endl;
    cout<<"a*b = "<<prod(a,b)<<endl;
    system("pause");
    }
    
    return 0;
}
