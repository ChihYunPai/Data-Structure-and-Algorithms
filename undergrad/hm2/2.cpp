#include<iostream>
#include<fstream>
#include<cmath>

using namespace std;

class point
{
    public:
           point(){x=0;y=0;}
           point(double X ,double Y){x=X,y=Y;}
           friend fstream& operator >> (fstream& fs, point &p);
           friend fstream& operator << (fstream& fs, point &p);
          
    private:
          double x, y;
};

fstream& operator >> (fstream& fs, point &p)
{
         fs>>p.x>>p.y;
         return fs;
}
fstream& operator << (fstream& fs, point &p)
{
         fs<<p.x<<p.y;
         return fs;
}

class polygon
{
    public:
            polygon(){size=0;}
            polygon(int n){size=n;p=new point[size];}
            polygon(const polygon& v){
                                          size=v.size;
                                          p=new point[size];
                                          for(int i=0; i<size; i++) p[i]=v.p[i];
                                          };
            polygon& operator=(const polygon& v){
                                                     delete p;
                                                     size=v.size;
                                                     p=new point[size];
                                                     for ( int i=0; i<size; i++) p[i]=v.p[i];
                                                     }
            bool operator==(const polygon& v){
                                              for(int i=0; i<size; i++)
                                              {
                                                      if(p[i]!=v[i])return false;
                                              }
                                              return true;
                                         };     
            const double& operator[](int n) const{ return p[n];};
            double& operator[](int n){return p[n];};
            double area(){
                                double A=0;
                                for(int i=0; i<size; i++)
                                {
                                        A=A+(p[i+1]->x+p[i]->y)*(p[i+1]->y-p[i]->y);
                                        }
                                return 0.5*abs(A);
                          };
            int getsize() const{return size;};
            ~polygon(){
                      delete p;
                      };
    private:
            int size; // The number of points of the polygon
            point *p; // The point array to hold the points
} ;

int main()
{
      int n;
      char filename[50];
      cout <<"Input the number of points and Enter the file name: \n";
      cin >> n ;/*>> filename;
      ifstream read(filename);
      if(read)cout<<"success\n";
      if(!read)cout<<"fail\n";*/
      ifstream is("hm2_data.txt");
      
      system("pause");
      return 0;
}
