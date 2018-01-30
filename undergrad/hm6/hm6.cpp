#include<iostream>
#include<string>
#include<sstream>
using namespace std;


template< class T >
class stack
{
      
      public:
             stack(int N){ n=N; 
                           p=new T[n];
                           index=0;
                           };
             bool empty()
                          {return index==0;}
             int size()   {return index;}
             T top()
                          {return p[index-1];}
             void push(const T& item)       
                          {if(index==n)cout<<"the stack is full.\n";
                           else{
                                p[index]=item;
                                index++;
                                }
                                                                   }
                           
             T pop()      {if(empty())cout<<"the stack is empty.\n";
                           else {
                                T temp = p[index-1];
                                index--;        
                                return temp;  }
                                                                    }
                                
             //ostream &operator<<(ostream&, const Stack&)
      private:
              T* p;
              int n;
              int index;
};


int main()
{
    cout<<"Please input the postfix: "<<endl;
    
    char buf[256];
    cin.getline(buf,256);//read in one line.
    istringstream is(buf);//convert to a stream.
    stack<double> x(10);
    double right=0 , left=0 ;
    while (1)
    {
          string str;
          is>>str;
          if (is)
          {
             if (str[0]>='0' && str[0]<='9')
                {double number=atof(str.c_str());
                x.push(number);} 
             else
             {
                 right=x.pop(); 
                 left=x.pop() ; 
                 switch(str[0])
                       {
                               case '+' : {x.push(left+right);}    break;                                    
                               case '-' : {x.push(left-right);}    break;
                               case '*' : {x.push(left*right);}    break;
                               case '/' : {x.push(left/right);}    break;
                       }
             }
          }
          else break;
    } 
    cout<<"The result is: "<<x.top()<<endl;

    
    system("pause");
    return (0);
}
 

