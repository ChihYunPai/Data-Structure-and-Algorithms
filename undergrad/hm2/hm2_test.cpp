#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;

class point 
{
    public:
           point(){x=0;y=0;}
           point(double X ,double Y){x=X,y=Y;}
           friend istream& operator >> (istream& is, point &p){is >> p.x >> p.y; return is;}
           friend ostream& operator << (ostream& os, point &p){os << p.x << p.y; return os;}
    private:
          double x, y;
};
class polygon
{
    public:
            polygon(){size=0;}
            polygon(int n){size=n;}// initialized an n point polygon
            polygon(const polygon& v); // copy constructor
            polygon& operator=(const polygon& v);//assign operator
            //bool operator==(const vec& v);//equality operator
            const double& operator[](int n) const; // constant operator[]
            double& operator[](int n);// not const operator[]
            double area();// The area of the polygon
            int getsize() const;// The number of points of the polygon
            //~vec(); // destructor
    private:
            int size; // The number of points of the polygon
            point *p; // The point array to hold the points
} ;

int main()
{
      polygon p;
      int n;
      char filename[50];
      cout <<"Input the number of points and Enter the file name: \n";
      cin >> n ;/*filename;
      ifstream read(filename);
      if(read)cout<<"success\n";
      else cout<<"fail\n";*/
      ifstream is("hm2_data.txt");
      
      
      
      
      system("pause");
      return 0;
}
