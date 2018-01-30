#include<iostream>
#include<fstream>
#include<string>
using namespace std;

             
main()
{
      double* px = new double;
      *px = 5.1234;
      double* py = new double[10];
      py[0] = 5.1234;
      py[9]=10;
      cout<<"px: "<<px<<endl;
      cout<<"*px: "<<*px<<endl;
      
      for(int i=0; i<11; i++)
      {
              cout<<"py["<<i<<"]: "<<py[i]<<endl;
//              cout<<"*py["<<i<<"]: "<<*py[i]<<endl;
              }
      delete px;
      delete [] py;
      cout<<"px: "<<px<<endl;
      cout<<"*px: "<<*px<<endl;
      /*
      for(int i=0; i<11; i++)
      {
              cout<<"py["<<i<<"]: "<<py[i]<<endl;
//              cout<<"*py["<<i<<"]: "<<*py[i]<<endl;
              }*/
              
      ifstream is("hm2_data.txt");
      double dd;
      string ss;
      while(1)
      {
              is>>dd;
              
              if(is)
              {
                    cout<<"dd"<<dd<<endl;
                    
              }
              else break;
      }
      
      system("pause");
      
      return 0;
} 
