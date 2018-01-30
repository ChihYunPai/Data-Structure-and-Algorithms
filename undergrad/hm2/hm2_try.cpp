#include <iostream> 
#include <fstream>
#include <vector>
#include <string>
using namespace std; 

double v(int x , string filename)
{
      vector<double> b1;
      double temp;
      string filname;
      ifstream read(filname.c_str());
      while (read>>temp){
      cout<<"sucess. \n";
      b1.push_back(temp)  ;
			}
      return b1[x];
}

int main()
{
      int n; 
      char filename[50];
      cout <<"Input the number of points and Enter the file name: \n";
      cin>> n >> filename ;   
      fstream read(filename);
      if (read){cout<<"reading sucess. \n";};
      if (!read){cout<<"error. \n";};
    
    
      system("pause");
      return 0;   
}
