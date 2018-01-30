#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    
    double x[7]={4,4,7,7,9,7,4}, y[7]={0,7.5,7.5,3,0,0,0};
    /*for(int i=0;i<7;i++){cout<<x[i]<<" ";}
    cout<<endl;
    for(int i=0;i<7;i++){cout<<y[i]<<" ";}
    cout<<endl;*/
    
    double A=0;
    for(int n=0;n<6;n++)
    {
            A=A+(x[n+1]+x[n])*(y[n+1]-y[n]);
            }
    A=0.5*abs(A);
    cout<<"The area is: "<<A<<endl ;
    system("pause");
    return (0);
}
