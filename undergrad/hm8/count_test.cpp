#include<iostream>
using namespace std;

class btest
{
      public:
             btest(){n=0;c=0;}
             btest(int N){n=N;c=0;}
             int count(){return c+=1;}
             int plus(){return n+=1;}
      private:
              int n, c;
};

int main()
{
    btest b,c(5);
    for(int i=0;i<=5;++i)
    {
            cout<<"b is: "<<b.count()<<endl;
            cout<<"c is: "<<c.plus()<<endl;
    }
system("pause");
return 0;
}

              
      
