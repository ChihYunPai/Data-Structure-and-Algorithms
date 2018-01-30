#include<iostream>
#include<string>
#include<list>
#include<algorithm>
#include<functional>
using namespace std;
class term
{
 public:
      term(double a, int n){pa=a, pn=n;};  //a=«Y¼Æ¡An=¦¸¼Æ 
      friend list<term> operator+(const list<term>& p1,const list<term>& p2 );
      friend istream& operator>>(istream& is, const list<term>& p);
      friend ostream& operator<<(ostream& os, const list<term>& p);
      double pa;
      int pn;
};
list<term> operator+(const list<term>& p1,const list<term>& p2 )
{
       list<term> p3,a;
       list<term>::const_iterator i1=p1.begin();
       list<term>::const_iterator i2=p2.begin();
       while(i1!=p1.end()&&i2!=p2.end())
       {
           if((*i1).pn>(*i2).pn)
           {p3.push_back(*i1);i1++;}
           else if((*i1).pn<(*i2).pn)
           {p3.push_back(*i2);i2++;}
           else if((*i1).pn==(*i2).pn)
           {    
                term t((*i1).pa+(*i2).pa,(*i1).pn);
                
                p3.push_back(t)
           ;i1++;i2++;}
       }
       if(i1==p1.end())
       {
           while(i2!=p2.end())
           {
               p3.push_back(*i2);
               i2++;
           }
       }
       else if(i2==p2.end())
       {
            while(i1!=p1.end())
           {
               p3.push_back(*i1);
               i1++;
           }
       }
       return p3;
};




istream& operator>>(istream& is,  term& p)
{       
         is>>p.pa>>p.pn;
         return is ;
};
ostream& operator<<(ostream& os,  list<term>& p)
{
         for(list<term>::iterator i=p.begin();i!=p.end();i++)
         {
          os<<"+("<<(*i).pa<<")10^"<<(*i).pn;
         }
         return os;
};


int main()
{
    list<term> p1, p2 ,p3;
    term p(0.0,0);
    int i,n,j;
    
    cout<<"please input the number and order of p1.\n";
    while(1)
    {
    cin>>p;
    p1.push_back(p);
    if(p.pn==0) break;
    }
    cout<<"p1= "<<p1<<endl;
    cout<<"please input the number and order of p2.\n";
    while(1)
    {
    cin>>p.pa>>p.pn;
    p2.push_back(p);
    if(p.pn==0)break;
    }
    cout<<"p2= "<<p2<<endl;
    
    p3=p1+p2;
    
        cout<<"p3= "<<p3<<endl;

    

system("pause");
return(0);
} 
