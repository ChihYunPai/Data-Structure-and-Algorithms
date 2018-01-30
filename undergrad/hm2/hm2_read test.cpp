#include<iostream>
#include<fstream>
using namespace std;

int main()
{
cout <<"Enter the file name : ";
char filename[50];
cin >> filename;
ifstream is(filename);
if(is)cout<<"success. \n";
while(1)
{
        double x,y;
        is>>x>>y;
        if(is)cout<<x<<" "<<y<<endl;
        
        else break;
}

  system("pause");
    return (0);
}
