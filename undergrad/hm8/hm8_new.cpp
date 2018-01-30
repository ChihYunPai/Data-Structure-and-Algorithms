#include<iostream>
#include<string>
#include<sstream>
using namespace std;

    int FF_R_max=5;                   //Maximum number of FF served between regular passengers: 5.
    int passenger_remain;           //passenger remained in the queue
    int max_processed_time;         //max_processed_time
    int max_simulation_time;        //max_simulation_time
    double FF_rate;                 //FF passenger arrival rate: 0.25/minute.
    double Reg_rate;                //Reg. passenger arrival rate: 0.5/minute.
    double agent_idle_time;         //agent idle time
    double passenger_served_number; //number of passenger served
    double av_waiting_time;         //average passenger waiting time
    
template<class T> class queue
{
        public:
               queue(){max=100;}
               queue (int n){
                             max=n;
                             p= new T[max];
                             count=0;
                             rear_index=0;
                             front_index=0;
                             }
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
               T& top()                 {return p[front_index];}
                                        
               
                                        
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
int n=my_random.next_int(max_processed_time) ;/* get an integer equally distributed between 1 and 4 */


class passenger
{
      public:
             passenger(){;}
             passenger(int AT, int PROCESSED_TIME)
             {
                           at=AT;
                           process_time=PROCESSED_TIME;
                           }
             //bool process(){process_time--;return process_time==0;}
             int process_time;
             //bool finish(){return process_time==0;}
             
             
      private:
              int at;
};

class passenger_queue
{
      public:
             passenger_queue(const double& RATE, const int& MAX_PROCESSED_TIME)
             {
                                   rate=RATE;
                                   max_processed_time=MAX_PROCESSED_TIME;
                                   waiting=0;
                                   
             } 
             void update(int TICK)
             {
                  
                  waiting+=line.size();
                  /*cout<<waiting<<endl;
                  cout<<my_random.next_int(max_processed_time)<<endl;
                  system("pause");*/
                  if(my_random.next_double()<=rate)
                  {
                                                   
                             count++;
                             line.push(passenger(TICK,my_random.next_int(max_processed_time+1)));
                  
                  }
                  
                  
             }
             void bookkeeping(int TICK){;}
             
             int get_process_time(){return line.top().process_time;}
             
             int get_size(){return line.size();}
             
             int get_waiting(){return waiting;}
                  
             bool empty(){return line.empty()==1;}
             
             
      private:
              double rate;
              queue<passenger> line;
              int count,max_processed_time,waiting;
};
/*declare FFqueue, REGqueue, */
passenger_queue   FFqueue(FF_rate,max_processed_time);
passenger_queue  REGqueue(Reg_rate,max_processed_time);


class agent
{
      public:
             
             agent(const int& FF_R_MAX){
                                 idle_time=0;
                                 combo=0;
                                 process_time=0;
                                 passenger_served_number=0;
                                 FF_R_max=FF_R_MAX;
                                 cout<<combo<<process_time<<passenger_served_number<<FF_R_max<<endl;
                                 }
             void update(int TICK)
             {
                  
                   if(process_time==0)
                   {
                          if(combo<FF_R_max){
                                             
                                                 if(FFqueue.empty()!=1)
                                                 {
                                                     process_time=FFqueue.get_process_time()-1;
                                                     passenger_served_number++;
                                                     combo++;
                                                     cout<<combo<<endl;
                                                     }
                                             
                                                 
                                                 else if(REGqueue.empty()!=1)
                                                 {
                                                     process_time=REGqueue.get_process_time()-1;
                                                     passenger_served_number;
                                                     cout<<combo<<endl;
                                                     }
                                                 else 
                                                 {
                                                      idle_time++;
                                                      }
                                             }
                          else {
                                             system("pause");
                                     if(REGqueue.empty()!=1)
                                     {
                                          process_time=REGqueue.get_process_time()-1;
                                          passenger_served_number;
                                          combo=0;
                                          cout<<combo<<endl;
                                          }
                                     else if(FFqueue.empty()!=1)
                                     {
                                          process_time=FFqueue.get_process_time()-1;
                                          passenger_served_number;
                                          combo++;
                                          cout<<combo<<endl;
                                          }
                                     else 
                                     {
                                          idle_time++;
                                          }
                               }
                   }
                   else/*process_time!=0*/
                   {process_time--;}
             }
             int get_idle(){return idle_time;}
             int get_served_number(){return passenger_served_number;}
                                          
             void bookkeeping(int TICK){;}
             
      private:
              int idle_time, combo, FF_R_max,process_time,passenger_served_number;
};

/*declare agent*/
agent agent_1(FF_R_max);

class checkin_sim
{
      public:
             checkin_sim(const int& MAX_SIMULATION_TIME, const int& FF_R_MAX, const double& FF_RATE, const double& REG_RATE )
           {
               max_simulation_time=MAX_SIMULATION_TIME;
               FF_R_max=FF_R_MAX;
               FF_rate=FF_RATE;
               REG_rate=REG_RATE;
               
               for (int tick=0; tick<max_simulation_time;tick++)
               {
               agent_1.update(tick);
               FFqueue.update(tick);
               REGqueue.update(tick);
               /* do the work */
               agent_1.bookkeeping(tick);
               FFqueue.bookkeeping(tick);
               REGqueue.bookkeeping(tick);
               }
           }
           int remain(){return FFqueue.get_size()+REGqueue.get_size();}
           int get_agent_idle(){return agent_1.get_idle();}
           int get_psn(){return agent_1.get_served_number();}
           int get_av_waiting()
           {
               if(get_psn()==0) return 119;
               else return (FFqueue.get_waiting()+REGqueue.get_waiting())/get_psn() ;
               }           
           /*int sim(){return max_simulation_time;}
           int FR(){return FF_R_max;}
           double FF(){return FF_rate;}
           double REG(){return REG_rate;}*/
           
      private:
              
              int max_simulation_time,FF_R_max;
              double FF_rate,REG_rate;
};
         


int main()
{

    queue<int> q(100);
    cout<<"***The Airline Check-In Simulation***"<<endl;
    /*cout<<"How many FF passengers are coming in one hours: \n";
    cin>>FF_rate; FF_rate/=60;
    cout<<"How many Reg. passengers are coming in one hours: \n";
    cin>>Reg_rate; Reg_rate/=60;
    cout<<"Input the max processed time: \n";
    cin>>max_processed_time;
    cout<<"Input the Maximum number of FF served between regular passengers: \n";
    cin>>FF_R_max;
    cout<<"Input the total simulation times(hours):  \n";
    cin>>simulation_time; simulation_time*=3600;
    */
    FF_rate=0.25;
    Reg_rate=0.5;
    max_processed_time=4;
    FF_R_max=5;
    max_simulation_time=480;
    cout<<"max_simulation_time: "<<max_simulation_time<<"\n"<<"FF_R_max: "<<FF_R_max<<"\n";
    cout<<"max_processed_time: "<<max_processed_time<<"\n"<<"Reg_rate: "<<Reg_rate<<"\n"<<"FF_rate: "<<FF_rate<<endl;    
    /*declare checkin_sim*/
    checkin_sim simulation(max_simulation_time,FF_R_max,FF_rate,Reg_rate);
    //cout<<simulation.sim()<<" "<<simulation.FR()<<" "<<simulation.FF()<<" "<<simulation.REG()<<endl;
    
    
    cout<<"/*** THE SIMULATION RESULT ***/"<<endl;
    cout<<"The agent_idle_time: "<<simulation.get_agent_idle()<<" (minutes) \n";
    cout<<"The passenger_served_number: "<<simulation.get_psn()<<" (persons) \n";
    cout<<" The passenger_remain:"<<simulation.remain()<<" (persons) \n";
    cout<<"The av_waiting_time: "<<simulation.get_av_waiting()<<" (minutes) \n";
    


    system("pause");
    return 0;
}
