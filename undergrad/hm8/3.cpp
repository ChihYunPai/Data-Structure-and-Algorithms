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
class Random {
        public:
            Random() {
                     std::srand(std::time(0));
                     }
            Random(int seed) {
                     std::srand(seed);
                     }
            int next_int(int n) {
                    return int(next_double() * n);
                    }
            double next_double() {
                    return double(std::rand()) / RAND_MAX;
                    }
};
Random my_random; /* declared globally such that all classes use the same one */
double p=my_random.next_double(); /* get a number equally distributed between 0 and 1 */
int n=my_random.next_int(10) ;/* get an integer equally distributed between 0 and 9 */
int max_processed_time=5;
class passenger
{
      public:
             passenger(){;}
             passenger(int AT/*, string ID*/){
                               at=AT;
                               //id=ID;
                               pt=my_random.next_int(max_processed_time)+1;
                               }
                               
             //static void set_max_process_time(int n){max_processed_time=n;}
             
             int arrival_time()  {return at;}
             
             int processed_time(){return pt;}
             
             //string get_id()     {return id;}
             
             
      private:
              int at,pt,st,wt;
              string id;
};
class test
{
      public:
             test(){;}
             test(int AT){;}
             int arrival_time()  {return at;}
             
             int processed_time(){return pt;}
      private:
              int at,pt,st,wt;
              string id;
};

int main()
{
    int aa;
    queue<int> q1(5);
    queue<passenger> q2(5);
    
    system("pause");
}
