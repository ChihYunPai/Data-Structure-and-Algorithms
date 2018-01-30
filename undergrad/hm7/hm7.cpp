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
                           
             bool empty() {return index==0;}
                          
             int size()   {return index;}
             
             T top()      {return p[index-1];}
                          
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
             T all()       {
                                 for(int i=index-1;i>=0;i--)
                                    {
                                     cout<<"x["<<i<<"]="<<p[i]<<endl;
                                     }
                                                                          }
                                     
                                
             //ostream &operator<<(ostream&, const Stack&)
      private:
              T* p;
              int n;
              int index;
};

int pre(char c) //pre=precedence
{
    if(c=='*'||c=='/'){return 2;}
    else if(c=='+'||c=='-'){return 1;}
    else if(c=='('){return 0;}
}

int main()
{
    cout<<"Please input the infix: ";
    string infix, postfix;
    char buf[256];
    cin.getline(buf,256);//read in one line.
    istringstream is(buf);//convert to a stream.
    stack<char> x(30);
    
    while (1)
    {
          
          is>>infix;
          cout<<"infix "<<infix<<endl;
          if (is)
          {
             if (infix[0]>='0' && infix[0]<='9')
                {postfix+=' ';postfix+=infix;}
             else if(infix[0]=='('){x.push(infix[0]);}
             else if(infix[0]==')'){
                                    while(x.top()!='(')
                                    {
                                     postfix+=' ';
                                     postfix+=(x.pop());   }
                                                                
                                    x.pop();}
             else /*(infix[0]=='+'||infix[0]=='-'||infix[0]=='*'||infix[0]=='/')*/{
                                                   if(!x.empty() && pre(infix[0])>pre(x.top()) ) x.push(infix[0]);
                                                   else {
                                                         while(!x.empty() && pre(infix[0])<=pre(x.top()) ) 
                                                         {postfix+=' ';
                                                          postfix+=(x.pop());}
                                                         x.push(infix[0]);
                                                         }
                                                   }
             //else cout<<"error: wrong operator.\n";
          }
          else break;
              cout<<"The postfix is : "<< postfix << endl;
              x.all();
    
    }
    cout<<postfix<<endl;
    while(!x.empty()){
                    postfix+=' ';
                    postfix+=(x.pop());          
                              }
    cout<<postfix<<endl;

    
    stack<double> y(10);//read in one line.
    istringstream is2(postfix);//convert to a stream.
    double right=0 , left=0 ;
    while (1)
    {
          string str;
          is2>>str;
          if (is2)
          {
             if (str[0]>='0' && str[0]<='9')
                {double number=atof(str.c_str());
                y.push(number);} 
             else
             {
                 right=y.pop(); 
                 left=y.pop() ; 
                 switch(str[0])
                       {
                               case '+' : {y.push(left+right);}    break;                                    
                               case '-' : {y.push(left-right);}    break;
                               case '*' : {y.push(left*right);}    break;
                               case '/' : {y.push(left/right);}    break;
                       }
             }
          }
          else break;
    } 
    cout<<"The result is: "<<y.top()<<endl;
    cout<<postfix;
    system("pause");
    return (0);
}


