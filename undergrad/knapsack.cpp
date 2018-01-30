#include<iostream>
using namespace std;
#include<stdio.h>
void knapsack(int n,int W);
int n,i,w,W;
int weight[50],v[50];
int C[50][50];
int main()
{
 cout<<"Enter number of items";
 cin>>n;
 cout<<"Enter Capacity";
 cin>>W;
 cout<<"Enter weights";
 for(i=0;i<n;i++)
 {
  cin>>weight[i];
 }
 cout<<"Enter values";
	for(i=0;i<n;i++)
 {
  cin>>v[i];
 }
knapsack(n,W);
	 system("pause");
}

void knapsack(int n,int W)
{

/*for(int c = 0; c <= W; c++){
	C[0][c] = 0;
  }*/
for(i = 1; i <= n; i++){
	C[i][0] = 0;
 //cout<<C[i][0];
  }
for(i=1;i<=n;i++)
{
	  for(w=0;w<=W;w++)
		  if(weight[i]<=w)						   //item can be put in knapsack
			 if(v[i]+C[i-1][w-weight[i]]>C[i-1][w])
		  C[i][w]=v[i]+C[i-1][w-weight[i]];
	else
		  C[i][w]=C[i-1][w];
		 else
			 C[i][w]=C[i-1][w];			 // w[i]>w
}
cout<<C[i][w];
//return C[i][w];
} 
 
