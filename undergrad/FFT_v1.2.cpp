#include<stdio.h>
#include<iostream>
#include<fstream>
#include <iomanip>
#include<ctime>
#include<complex>
#include<vector>
#include<valarray>

#define pi 3.14159265358979323846
#define file "input_data.txt"
#define result_1 "output_1.txt"
#define result_2 "output_2.txt"
#define result_3 "output_3.txt"

using namespace std;
typedef complex<double> Complex;
typedef valarray<Complex> CArray;

void write_x(Complex x[],int N)
{
  ofstream myfile;
  myfile.open (result_3);
  for(int i=0;i<N;i++)
  {
          //int temp = x[N].real();
          myfile << x[i].real() <<" ";
          }
  myfile.close();
}
void write_CA(CArray input)
{
  size_t N=input.size();
  ofstream myfile;
  myfile.open (result_1);
  for(int i=0;i<N;i++)
          myfile << input[i]<<" ";
  myfile.close();
}
void write_CV(vector<Complex> input)
{
  size_t N=input.size();
  ofstream myfile;
  myfile.open (result_2);
  for(int i=0;i<N;i++)
  {
          Complex Ctemp;
          Ctemp = abs(input[i]);
          myfile << real(Ctemp)<<" ";
          }
  myfile.close();
}
void read(Complex x[])
{
  ifstream is(file);
  int N=0;
  while(1)
  {
          if(is)
          {
          int temp;
          is>>temp;
          Complex ctemp(temp,0);
          x[N]=ctemp;
          }
          else break;
  }
}
void gen_data(Complex x[], const int& N, const int& M, const int& m)
{     
     int n,m_var=0;
     
     for(n=0;n<N;n++)
     {
         if(n>m_var*N+M)m_var++;
         if(n<=m_var*N+M && n>=m_var*N-M) x[n]=1;
         else x[n]=0;
     }
 }
Complex  W(const int& N, const int& k, const int& n)
{
         if(N/2==k*n)return Complex(-1,0);
         Complex thetatemp(0,-2*pi*k*n/N);
         return exp(thetatemp);
}
vector<Complex > DTFT(const int& N, const Complex x[])
{
  int n,k;
  vector<Complex > X;
  for(k=0;k<N;k++)
  {
      complex<double> theta(0,0);
      for (n=0;n<N;n++)
      {
          theta += ( x[n] * W(N,k,n) );// = -2*pi*k*n/N
          }
      X.push_back(theta);
  }    
  return X;   
}
void FFT(CArray& x)
{
  const size_t N = x.size();
  if(N<=1)return;
  
  CArray E = x[slice(0,N/2,2)];
  CArray O = x[slice(1,N/2,2)];
  FFT(E);
  FFT(O);
  
  for(size_t k=0;k<N/2;k++)
  {
     Complex t= polar(1.0,-2*pi*k/N)*O[k];
     x[k]    =E[k]+t;
     x[k+N/2]=E[k]-t;
  }
}
int main ()
{
  cout<<"/****                  Project#1:     FFT                    ****/"<<endl;
  cout<<"/****輸入N(必須是2的整數次方)、M(大於1正整數)、m(大於1正整數)****/"<<endl;
  cout<<"/****輸入N(題目給定:32768)、M(題目給定:10000)、m(1)          ****/"<<endl<<endl;
  clock_t start_time, end_time;
  int n,k,N,M,m;
  cout<<"Input N: ";
  cin>>N;cout<<endl;
  cout<<"Input M: ";
  cin>>M;cout<<endl;
  /* 
  cout<<"Input m( >=1 ): ";
  cin>>m;cout<<endl;
  */
  m=1;
  cout<<"計算中..."<<endl<<endl;
  Complex x[N];
  gen_data(x,N,M,m);
  write_x(x,N);
  CArray X_2(x,N);
  
  //直接計算
  /*-----------begin-----------*/
  start_time = clock();
  vector<Complex > X_1=DTFT(N,x);
  end_time = clock();
  /*------------end------------*/
  cout << "直接計算DTFT的時間: "<<setprecision(20)<<(float)(end_time - start_time)/CLOCKS_PER_SEC<<" s."<<endl;
  write_CV(X_1);
  
  cout<<endl;
  //使用FFT計算 
  /*-----------begin-----------*/
  start_time = clock();
  FFT(X_2);
  end_time = clock();
  /*------------end------------*/
  cout << "使用FFT計算的時間: "<<setprecision(20)<<(float)(end_time - start_time)/CLOCKS_PER_SEC<<" s."<<endl;
  write_CA(abs(X_2));
  
  
  
  cout<<endl;
  system("plot.exe");
  cout<<endl;
  system("pause");
  return 0;
}
