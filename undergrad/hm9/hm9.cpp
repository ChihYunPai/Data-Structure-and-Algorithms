#include<iostream>
using namespace std;

void print(int n, int row[])
{
     int c=0;
     for(int i=n-1;i>=0;i--)
    {
            c=n+1;
            if(i==n-1)
            {
            while(1)
               {
                if(c>1&&c!=n+1)cout<<"¢s¢w";
                else if(c==n+1)cout<<"¢z¢w";
                else   {cout<<"¢{";break;}
                c--;
               }  
               cout<<endl;
            }
            
           
            for(int j=0;j<n;j++)
            {
                    if(row[j]!=i){
                                  if(j<n-1)cout<<"¢x# ";
                                  else     cout<<"¢x# ¢x";
                                  }
                    else         {
                                  if(j<n-1)cout<<"¢xQ ";
                                  else     cout<<"¢xQ ¢x";
                                  }
                                  
            }
            if(i!=0)
                   {
                    cout<<endl;
                    c=n;
                    while(1)
                       {
                        if(c>1&&c!=n)cout<<"¢w¢q";
                        else if(c==n)cout<<"¢u¢w¢q";
                        else   {cout<<"¢w¢t";break;}
                        c--;
                       }  
                    } 
                    
            if(i==0)
                    {
                            c=n+1;
                            cout<<endl;
                            while(1)
                                   {
                                    if(c>1&&c!=n+1)cout<<"¢r¢w";
                                    else if(c==n+1)cout<<"¢|¢w";
                                    else   {cout<<"¢}";break;}
                                    c--;
                                   }
                    }
                    cout<<endl;
    }
}
class Nqueen
{
      public:
             Nqueen(int N)
             {
                        count=0;
                        n=N;
                        row=new int[n];
             }         
            void PlaceQueen(int column)
            {    
                    int i;
                    int j;
                    
                    for ( i=0; i<n; i++)
                    {
                        for(j=0;j<column;j++)
                        {
                         if(i==row[j]  ||  abs(i-row[j])==abs(column-j))  break;
                         }
                        if(j==column)
                        {
                                       row[column]=i;
                                       if(column!=n-1)PlaceQueen(column+1);
                                       else {
                                            count++;
                                            cout<<count<<endl;
                                            //for(int k=0;k<n;k++)cout<<"k:"<<row[k]<<endl;
                                            print(n, row);
                                            }
                        }
                    }
            }
      private:
              int *row;
              int n,count;
};

int main()
{
    int n;
    cout<<"Input the number of Queens: ";
    cin>>n;
    Nqueen nq(n);
    nq.PlaceQueen(0);
    system("pause");
}
