#include <iostream>
#include <cmath> 
using namespace std;
class vec 
{
public:
    vec() {len=0;p=0;};
    vec(int n) 
    {
        len=n; p=new double[len];
        cout<<"vec("<<n<<") is called. p is "<<p<<endl;
    };
    vec(const vec& v) // copy constructor 
    {
        len=v.len;
        p=new double[len];
        for (int i=0; i<len; i++) p[i]=v.p[i];
    };/*
    vec& operator=(const vec& v)
    {
        delete p;
        len=v.len;
        p=new double[len];
        for (int i=0; i<len; i++) p[i]=v.p[i];            
    };
    bool operator==(const vec& v)
    {
        for (int i=0; i<len; i++)
        {
            if (p[i]!=v.p[i]) return false;
        };
        return true;                     
    };
    const double& operator[](int n) const
    {
        return p[n];
    };
    double& operator[](int n)
    {
        return p[n];
    };*/
    ~vec() 
    {
        delete p;
        cout<<"~vec() is called. p is "<<p<<endl;        
    };
    double getlen()const {return len;};
    
private:    
    int len;
    double *p;
} ;


int main()
{
    {
        int size;
        cout<<"Enter the size of the vector: ";
        cin>>size;
        vec v(size);
    };
    system("pause");
}
    

