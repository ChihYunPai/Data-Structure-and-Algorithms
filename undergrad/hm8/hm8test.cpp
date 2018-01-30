#include<iostream>
#include<string>
#include<sstream>
using namespace std;
    int FF_R_max, simulation_time, passenger_remain;
    double FF_rate, Reg_rate, agent_idle_time, passenger_served_number, av_waiting_time;
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


string itos(int &i)
{
       string s;
       stringstream ss(s);
       ss<<i;
       return ss.str();
}

string creat_ID(int const len, int const number)
{
    int n, i, count, temp;
    char const z='0';
    n=len;
    i=number;
    
    count=0;
    temp=i;
    if(temp>9){
                while(temp>9){temp/=10;count++;}
                }
    else temp=0;
    string s;
    if(i>0){
            for(int j=1; j<(n-count); j++){s+=z;}
            s+=itos(i);
           }
            
    else for(int j=0; j<n; j++){s+=z;}
    return s;
    
}

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
int max_processed_time;
/*class passenger:
        ID
        at:arrival time
        pt:processed time
        st:served time
        wt:waiting time
*/
class passenger
{
      public:
             passenger(int AT, string ID){
                               at=AT;
                               id=ID;
                               pt=my_random.next_int(max_processed_time)+1;
                               }
                               
             static void set_max_process_time(int n){max_processed_time=n;}
             
             int arrival_time()  {return at;}
             
             int processed_time(){return pt;}
             
             string get_id()     {return id;}
             
             
      private:
              int at,pt,st,wt;
              string id;
};
class passenger_queue
{
      public:
             passenger_queue(double RATE, int queue_max ): x(queue_max) {rate=RATE;count=0;}
             void update(int TICK){
                                   if(p<=rate){
                                               count++;
                                               id=creat_ID(10,TICK);
                                               x.push(passenger(TICK,id));
                                               
                                               }
                                   }
             
             void bookkeeping(int TICK){;}
             
             bool empty(){return x.empty()==1;}
             //int total_number(){return count;}
                           
      private:
              double rate;
              queue<passenger> x;
              int count;
              string id;
};
//double FF_rate, Reg_rate;
passenger_queue FFqueue(FF_rate, 100), REGqueue(Reg_rate, 100);
class agent
{
      public:
             agent(int FF_R_MAX){
                                 idle_time=0;
                                 idle=1;
                                 combo=0;
                                 FF_R_max=FF_R_MAX;
                                 }
             void update(int TICK){
                                          
                                          if(combo<FF_R_max){
                                                             if(FFqueue.empty()!=1){/**/;combo++;}
                                                             else if(REGqueue.empty()!=1){/**/;combo=0;}
                                                             else {idle_time++;}
                                                             }
                                          else {
                                                 if(REGqueue.empty()!=1){/**/;combo=0;}
                                                 else if(FFqueue.empty()!=1){/**/combo++;}
                                                 else {idle_time++;}
                                                 
                                                }
                                   }
                                          
             void bookkeeping(int TICK){;}
             //bool free(){return idle==1;}
      private:
              int idle_time, idle, combo, FF_R_max;
};
agent agent_1(FF_R_max);
class chekin_sim
{
      public:
             chekin_sim(int SIMULATION_TIME, int FF_R_MAX, double FF_RATE, double REG_RATE)
                                 {
                                   simulation_time=SIMULATION_TIME;
                                   FF_R_max=FF_R_MAX;
                                   FF_rate=FF_RATE;
                                   Reg_rate=REG_RATE;
                                   }
             void run();
      private:
              int max_simulation_time, FF_R_max;
              double FF_rate, Reg_rate;
              agent agent_1;
              passenger_queue FFqueue, REGqueue;
              
              
};

void run()
{
     for(int tick=1;tick<=simulation_time;tick++)
     {
             agent_1.update(tick);
             FFqueue.update(tick);
             REGqueue.update(tick);
             /* do the work */
             agent_1.bookkeeping(tick);
             FFqueue.bookkeeping(tick);
             REGqueue.bookkeeping(tick);               }
}
int main()
{

    
    cout<<"***The Airline Check-In Simulation***"<<endl;
    cout<<"How many FF passengers are coming in one hours: \n";
    cin>>FF_rate; FF_rate/=60;
    cout<<"How many Reg. passengers are coming in one hours: \n";
    cin>>Reg_rate; Reg_rate/=60;
    cout<<"Input the max processed time: \n";
    cin>>max_processed_time;
    cout<<"Input the Maximum number of FF served between regular passengers: \n";
    cin>>FF_R_max;
    cout<<"Input the total simulation times(hours):  \n";
    cin>>simulation_time; simulation_time*=3600;
    
    cout<<"The agent idle time is: "<<agent_idle_time<<" (minutes) \n";
    cout<<"The number of passenger served by agent is: "<<passenger_served_number<<" (person) \n";
    cout<<" The number of passenger remained in the queue is:"<<passenger_remain<<" (person) \n";
    cout<<"The average passenger waiting time is: "<<av_waiting_time<<" (minutes) \n";
    


    system("pause");
    return 0;
}

