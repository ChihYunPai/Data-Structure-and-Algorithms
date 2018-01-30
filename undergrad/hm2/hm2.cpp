#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;

class point
{
      public:
             point(){x=0,y=0;}
             //point(double& X, double& Y)
             //point& operator = (const point &p)
             friend istream& operator >> (istream& is, point &p){is >> p.x >> p.y; return is;};
             double x, y;
};

class polygon
{
      public:
              polygon(){n=0;count=0;}
              polygon(const int& N){
                                    count=0;
                                    n=N;
                                    p = new point[n];
                            
                                        }
              void input(const point& pin){
                                           p[count]=pin;
                                           count++;
                                           }
              double area(){
                            double A=0;
                            for(int i=0; i<n; i++)
                            {
                                    A=A+(p[i+1].x+p[i].x)*(p[i+1].y-p[i].y);
                                    cout<<A<<endl;
                                    }
                            cout<<A<<endl;
                            return 0.5*abs(A);
                            }
              int getsize() const{return n;}
              ~polygon(){delete [] p;}
      private:
              int n, count;
              point* p;
};
              
int main()
{
    
    int n;
    cout <<"Input the  number of points"<<endl;
    cin>> n;
    polygon poly_1(n);
    /*
    cout <<"Enter the file name : "<<endl;
    char filename[50];
    cin >> filename;
    */
    ifstream is("hm2_data.txt");
    if(is)cout<<"read success."<<endl;
    point pget;
    double dx,dy;
    while(1)
    {
            is>>dx>>dy;
            pget.x=dx;
            pget.y=dy;
            
            if(is)
            {
            poly_1.input(pget);
            }
            else break;
    }
    cout<<"The Area of "<<n<<"-sided polygon is : "<<poly_1.area()<<endl;
    system("pause");
    return 0;
}
