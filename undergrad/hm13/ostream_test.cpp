#include<iostream>
#include<ostream>
using namespace std;

class test
{
      public:
             test(){;}
             ostream& operator << (ostream& os, const test& t)
             {
                      os<<t.v1<<" "<<t.v2<<" "<<t.w;
                      cout<<endl;
                      return os;
                      }
             
      private:
              string v1,v2;
              double w;
};
