#include<iostream>
#include<fstream>
#include<vector>
#include<cmath>
#include<string>
#include<cfloat>
using namespace std;
typedef int index;
typedef int keytype;
vector<keytype> Key;
vector<string>  Key_contain;
vector<vector<index> > R;
template <class T>
int length(T number)
{
    int digits = 0;
    if (number<=0) digits = 1;
    while(number>0) {
        number /= 10;
        digits++;
    }
    return digits;
}
struct Node
{
	Node(){left=NULL;right=NULL;}
	keytype key;
	Node* left;
	Node* right;
};
void optsearchtree(int n, const float p[], float& minavg)
{
   index i, j, k, diagonal;
   float A[n+2][n+1];
   
   for(i=1;i<=n;i++)
   {
	  A[i][i-1]= 0;
	  A[i][i]  = p[i];
	  R[i][i]  = i;
	  R[i][i-1]= 0;
	  
   }
   A[n+1][n] = 0;
   R[n+1][n] = 0;
   
   for(diagonal=1;diagonal<=n-1;diagonal++)
   {
	   for(i=1;i<=n-diagonal;i++)
	   {
		   j=i+diagonal;
		   float temp=FLT_MAX, sum_p=0;
		   index temp_k;
		   for(k=i;k<=j;k++)
		   {
			   if( ( A[i][k-1] + A[k+1][j] )< temp )
			   {
				   temp=A[i][k-1] + A[k+1][j];
				   temp_k = k;
			   }
		   }
		   for(index m=i;m<=j;m++)sum_p+=p[m];
		   A[i][j] = temp + sum_p;
		   R[i][j] = temp_k;
	   }
    }
   minavg = A[1][n];     
}

void R_resize(int n)
{
    R.resize(n+3);
    for (int i = 0; i < n+3; i++)
    { 
        R[i].resize(n);
    } 
} 
Node* tree(index i, index j)
{
	index k;
	Node* p;
	
	k = R[i][j];
	if(k==0)return NULL;
	else
	{
	   p = new Node;
	   p-> key  = Key[k];
	   p-> left = tree(i,k-1);
	   p-> right= tree(k+1,j);
	   return p;
	}
}
void input_data(int n, float p[])
{
    Key.resize(n+2);Key_contain.resize(n+2);
    for(int count=1; count<=n; count++)
    {
         cout<<endl;
         string key_temp;
         float p_temp;
         Key[count]=count;
         cout<<"Input Key["<<count<<"]: ";
         cin>>key_temp;
         Key_contain[count]=key_temp;
         cout<<"Input P["<<count<<"]: ";
         cin>>p_temp;
         p[count]=p_temp;
         cout<<endl;
    } 
}
int d(Node* p)
{
	if(p==NULL)return 0;
	else
	{
	 if(d(p->left)>d(p->right))return d(p->left)+1;
	 else return d(p->right)+1;
	}
}
int even(int n)
{
	if(n%2!=0)return n-1;
	else return n;
}

void put_widechar(char c[],char c2[]){c[0]=c2[0];c[1]=c2[1];}
void Display0(int width, int offset, vector<char> *line, int dep, Node *node)
{
	if (node==NULL) return;
	else
	{
        string str_temp=Key_contain[node->key];
		for (int i=0; i<str_temp.length(); i++)
		line[dep][offset-str_temp.length()/2+i]=str_temp[i];
		int left=even(offset-width/4);
		int right=even(offset+width/4);
		if (node->left!=NULL || node->right!=NULL)
		{
			put_widechar(&line[dep+1][left],"┌");/* put_widechar copy a two bytes character string to memory */
			for (int i=left+2;i<offset; i+=2) put_widechar(&line[dep+1][i],"─");
			put_widechar(&line[dep+1][offset],"┴");  
			for (int i=offset+2;i<right; i+=2)
			put_widechar(&line[dep+1][i],"─");
			put_widechar(&line[dep+1][right],"┐");
		};
	Display0(width/2, left, line, dep+2, node->left);
	Display0(width/2, right, line, dep+2, node->right);
	};
};
void Display(ostream &os, int width, Node* root, int depth)
{
	int row=2*depth-1;
	vector<char> *line=new vector<char>[row];
	for (int i=0; i<row; i++) line[i].resize(width,' ');
	Display0(width, even(width/2), line, 0, root); // even function change a number to even if it is odd 
	for (int i=0; i<row; i++)
	{
	for (int j=0; j<width; j++) os<<line[i][j];
	os<<endl;
	};
	delete [] line;
};
int main()
{
    cout<<"/**** Project#2_2: Optimal Binary Search Tree   ****/"<<endl;
    cout<<"/****             作者: B9827115白植允          ****/"<<endl;
    cout<<"/****   輸入:n, key[], p[]  輸出:OptBSTree      ****/"<<endl<<endl;
    
    int n, depth;
    cout<<"Input n: ";
    cin>>n;
    float minavg, p[n+2];
    R_resize(n);
    input_data(n,p);
    optsearchtree( n, p, minavg);
    Node* root = tree(1,n);
    depth = d(root);
    Display(cout, 80, root, depth);
    
    system("pause");
    return 0;
}
