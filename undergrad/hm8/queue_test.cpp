#include<iostream>
#include<string>
#include<sstream>
using namespace std;
template<class T> class queue
{
        public:
               queue (int n){max=n;p= new T[max];count=0;rear_index=0;front_index=0;}
               void push(const T& item){if(count==max)cout<<"queue is full.\n";
                                        else{
                                             if(rear_index==max)rear_index=0;
                                             p[rear_index]=item;
                                             rear_index++;
                                             count++;
                                             }
                                                                               }
               
               T pop()                 {
                                        if(count==0)cout<<"queue is empty.\n";
                                        else{
                                             T temp = p[front_index];
                                             front_index++;
                                             if(front_index==max)front_index=0;
                                             count--;
                                             return temp;
                                             }
                                                                              }
                                        
               bool empty()            {return count==0;}
                            
               int size()              {return count;}
               
               T front()               {return p[front_index];}
               
               int get_front_index()       {return front_index;}
               
               int get_rear_index()        {return rear_index;}
        private:
               T *p;     
               int max; //maximum size of the queue; 
               int front_index;
               int rear_index;
               int count;
               
};
int main()
{
    queue<int> q1(5);
    int b,n=6;
    for(int i=0; i<n; i++)
    {
            cout<<"input the integer number. \n";
            cin>>b;
            q1.push(b);
            cout<<"the size of q1 is: "<<q1.size()<<endl;
            cout<<"front_index: "<<q1.get_front_index()<<endl;
            cout<<"rear_index:  "<<q1.get_rear_index()<<endl;
            cout<<"the number "<<i<<" step (front) is "<<q1.front()<<endl;
            }
        for(int i=0; i<n; i++)
    {
            if(!q1.empty())cout<<"the q1.pop() is "<<q1.pop()<<endl;
            }
            
    system("pause");
}
            
