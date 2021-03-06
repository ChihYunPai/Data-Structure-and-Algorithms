#include<iostream>

using namespace std;
/* pair class is defined as: */
template <class T1, class T2> struct pair
{
         typedef T1 first_type;
         typedef T2 second_type;
         
         T1 first;
         T2 second;
         pair() : first(T1()), second(T2()){}
         pair(const T1& x, const T2& y) : first(x), second(y) {}
         template <class U, class V>
           pair(const pair<U,V>&p) : first(p.first), second(p.second) {}
};

int main()
{
    
    system("pause");
    return 0;
    
}
