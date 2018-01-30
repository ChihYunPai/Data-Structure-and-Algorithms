#include <iostream>
#include <cmath>
using namespace std;
class complex
{
public:
       
double r,i;
complex() {;};
complex(double r, double i) {re=r; im=i;};
double angle() const{return atan2(im,re);}
double abs() const{return sqrt(re*re+im*im);};
friend double abs(const complex &z); // the absolute value
friend complex operator +(const complex &z1, const complex &z2);
friend complex operator -(const complex &z1, const complex &z2);
friend complex operator *(const complex &z1, const complex &z2);
friend complex operator /(const complex &z1, const complex &z2);
friend istream& operator>>(istream& is , complex &z1);
friend ostream& operator<<(ostream& os , const complex &z1);
private:
double re, im;
};
double abs(const complex &z)
{
       return z.abs();
       }
complex operator +(const complex &z1, const complex &z2)
{return complex(z1.re+z2.re,z1.im+z2.im);}
complex operator -(const complex &z1, const complex &z2)
{return complex(z1.re-z2.re,  z1.im-z2.im);}
complex operator *(const complex &z1, const complex &z2)
{return complex(z1.re*z2.re-z1.im*z2.im,  z1.re*z2.im+z2.re*z1.im);}
complex operator /(const complex &z1, const complex &z2)
{return complex((z1.re*z2.re+z1.im*z2.im)/(z2.re*z2.re+z2.im*z2.im), (z1.im*z2.re-z1.re*z2.im)/(z2.re*z2.re+z2.im*z2.im));}
istream& operator>>(istream& is,  complex &z1)
{is>>z1.re>>z1.im;return is;}
ostream& operator<<(ostream& os, const complex &z1)
{os<<'('<<z1.re<<','<<z1.im<<')';return os;}
int main()
{
    complex z1,z2;
    cout<<"input first complex number z1"<<endl;
    cin>>z1;
    cout<<"input second complex number z2"<<endl;
    cin>>z2;
    cout<<"angle of z1="<<z1.angle()<<endl;
    cout<<"angle of z2="<<z2.angle()<<endl;
    cout<<"abs of z1="<<abs(z1)<<endl;
    cout<<"abs of z2="<<abs(z2)<<endl;
    cout<<"z1+z2="<<z1+z2<<endl;
    cout<<"z1-z2="<<z1-z2<<endl;
    cout<<"z1*z2="<<z1*z2<<endl;
    cout<<"z1/z2="<<z1/z2<<endl;
    system("pause");
    return 0;
}

