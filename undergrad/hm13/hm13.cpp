#include<iostream>
#include<fstream>
#include<stdlib.h>
#include<string>
#include<set>
#include<map>
#include<list>
#include<queue>
#include<limits>
using namespace std;
class graph
{
      public:
            struct edge
                {
                   edge(){;}
                   edge(const string& s1,const string &s2)
                   {
                              v1=s1;
                              v2=s2;
                              
                              }
                   string v1,v2; 
                   double w;
                   friend ostream& operator << (ostream& os, const edge& e)
                   {
                            os<<"v1: "<<e.v1<<", v2: "<<e.v2<<", w: "<<e.w<<endl;
                            return os;
                            }
                   friend bool operator == (const edge& e1, const edge& e2)
                   {
                        return(e1.v1==e2.v1 && e1.v2==e2.v2);
                        }
                };
            
            void Input(istream &is, bool directed);
            void print_edgelsit();
            void FindAllPath(string start, string dest);
            void find_all(string start, string dest,list<string>& shortestpath);
            void FindShortestPath(string start, string dest, list<string>& shortestpath);
            double ComputeDist(list<string>& path);
    private:
            int vertcnt;//¸`ÂI¼Æ 
            map< string,set<string> > adjlist; 
            list<edge> edgelist;
            list<string> visitedlist;
            double wnew,wtemp;
};

void graph:: Input(istream &is, bool directed)
{
 edge e;
       is>>vertcnt;
       while(1)
       {
               string s1,s2;
               double wtemp;
               is>>s1>>s2>>wtemp;
             if(is)
             {
                   
                   e.v1=s1;e.v2=s2;e.w=wtemp;
                   edgelist.push_back(e);
                   // inverse //
                    if(directed==false)
                    {
                                       e.v1=s2;e.v2=s1;e.w=wtemp;
                                       edgelist.push_back(e);
                                       }
             }
             else break;
       }
 

    // build adjlist //
    list<edge>::iterator it;
    map< string,set<string> >::iterator adjit;
    set<string>::iterator setit;
    
    for(it=edgelist.begin();it!=edgelist.end();it++)
    {
         adjlist[(*it).v1];
         adjit=adjlist.find( (*it).v1 );
         (*adjit).second.insert( (*it).v2 );
    }
    cout<<"The adjlist contains: "<<endl;
    for(adjit=adjlist.begin();adjit!=adjlist.end();adjit++)
    {
       cout<<(*adjit).first<<" => ";
       for(setit=(*adjit).second.begin();setit!=(*adjit).second.end();setit++)
       cout<<" "<<*setit;
       cout<<endl;
       }
}
void graph:: print_edgelsit()
{
     list<edge>::iterator it;
     cout<<"The vertcnt: "<<vertcnt<<endl;
     cout<<"The edgelist contains: "<<endl;
     for(it=edgelist.begin();it!=edgelist.end();it++)
     cout<<" "<<*it;
     cout<<endl;
}
void graph:: FindAllPath(string start, string dest)
{
     
     visitedlist.push_back(start);//push n1 to visitedlist.
     
     map< string,set<string> >::iterator adjit;
     set<string>::iterator setit;
     list<string>::iterator it;
     
     
     
     for(setit=adjlist[start].begin();setit!=adjlist[start].end();setit++)//For each node n in n1¡¦s adjacent list:
     {
          if( (*setit)==dest)//if n==n2.
          {
             visitedlist.push_back( (*setit) );//push n to visitedlist.
             for(it=visitedlist.begin();it!=visitedlist.end();it++)//one path is found, output
             {cout<<(*it)<<" ";}
             cout<<endl;
             visitedlist.remove( (*setit) );//remove n.
          }
          else if(find(visitedlist.begin(),visitedlist.end(),(*setit) )==visitedlist.end())
          {//else if n is not in visitedlist,
          {FindAllPath( (*setit), dest );}//find all paths from n to n2.
          }
     }
     visitedlist.remove(start);
}
double graph::ComputeDist(list<string>& path)
{
       string stemp;
       double wtemp=0;
       list<string>::iterator it;
       it=path.begin();
       stemp=(*it);
       it++;
       for(;it!=path.end();it++)
       {
                                
           edge e( stemp, (*it) );
           wtemp+=find(edgelist.begin(), edgelist.end(), e)->w;
           stemp=(*it);
           }
       return wtemp;
}
void graph::find_all(string start, string dest,list<string>& shortestpath)
{
       visitedlist.push_back(start);//push n1 to visitedlist.
     
     map< string,set<string> >::iterator adjit;
     set<string>::iterator setit;
     list<string>::iterator it;
     
     for(setit=adjlist[start].begin();setit!=adjlist[start].end();setit++)//For each node n in n1¡¦s adjacent list:
     {
          if( (*setit)==dest)//if n==n2.
          {
             visitedlist.push_back( (*setit) );//push n to visitedlist.
             //one path is found, compute
             
             double wnew;
             wnew=ComputeDist(visitedlist);
             if(wnew<wtemp)
             {wtemp=wnew;
             shortestpath=visitedlist;}
             
             visitedlist.remove( (*setit) );//remove n.
          }
          else if(find(visitedlist.begin(),visitedlist.end(),(*setit) )==visitedlist.end())
          {//else if n is not in visitedlist,
          {find_all( (*setit), dest, shortestpath);}//find all paths from n to n2.
          }
     }
     visitedlist.remove(start);
}
void graph::FindShortestPath(string start, string dest, list<string>& shortestpath)
{
       list<string>::iterator it;
       wtemp=numeric_limits<double>::max();
       wnew=0;
       find_all(start,dest,shortestpath);
       cout<<"The shotest path(Toatal: "<<wtemp<<" ) : ";
       for(it=shortestpath.begin();it!=shortestpath.end();it++)
       {
          cout<<" "<<(*it);
          }
          cout<<endl;
}
int main()
{
    graph graph_1, graph_2;
    list<string> shortestpath;
    // --1-- //
    ifstream is1("hm13_data1.txt");
    if(is1)cout<<"good"<<endl;
    
    graph_1.Input(is1,false);
    graph_1.print_edgelsit();
    graph_1.FindAllPath("5", "9");
    graph_1.FindShortestPath("5","9",shortestpath);
    
    // --2-- //
    ifstream is2("hm13_data2.txt");
    if(is2)cout<<"good"<<endl;
    
    graph_2.Input(is2,false);
    graph_2.print_edgelsit();
    graph_2.FindAllPath("Philadelphia", "Chicago");
    graph_2.FindShortestPath("Philadelphia","Chicago",shortestpath);
    
    system("pause");
    return 0;
}
