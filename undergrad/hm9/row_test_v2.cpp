#include<iostream>
#include<stdlib.h>
using namespace std;
int main()
{
    int row[8]={0,1,2,3,4,5,6,7};
    int n=8,c=0;
    /*cout<<row[0]<<endl;
    cout<<row[7];;
    system("pause");*/
    for(int i=n-1;i>=0;i--)
    {
            if(i==n-1)
            {
            c=n+1;
            while(1)
               {
                if(c>1&&c!=n+1)cout<<"�s�w";
                else if(c==n+1)cout<<"�z�w";
                else   {cout<<"�{";break;}
                c--;
               }
            cout<<endl;  
            }
            
            for(int j=0;j<n;j++)
            {
                    if(row[j]!=i){
                                  if(j<n-1)cout<<"�x# ";
                                  else     cout<<"�x# �x";
                                  }
                    else         {
                                  if(j<n-1)cout<<"�xQ ";
                                  else     cout<<"�xQ �x";
                                  }
                                  
            }
            
                            c=n+1;
                            cout<<endl;
                            while(1)
                                   {
                                    if(c>1&&c!=n+1)cout<<"�r�w";
                                    else if(c==n+1)cout<<"�|�w";
                                    else   {cout<<"�}";break;}
                                    c--;
                                   }
                    cout<<endl;
    }
    
    system("pause");
                    
}
