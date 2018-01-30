#include<iostream>
#include<fstream>
#include<stdlib.h>
#include<map>
#include<queue>
using namespace std;
template <class T> class Binary_Tree
{
         public:
                class Node
                {
                    public:
                           Node(){left=NULL;right=NULL;}
                           friend bool operator < (const Node& a,const Node& b){return a.data<b.data;}
                           //friend bool operator > (const Node& a,const Node& b){return a.data>b.data;}
                           T data;
                           Node *left, *right;
                };
                Binary_Tree(){root=NULL;}
                void input(istream &is);
                void output(ostream &os){o(os, root);}
                void Display(ostream &os, int width);
                void Display0(int width, int offset, vector<char> *line, int dep, Node *node);
                Node *find(const T& key)
                {return f(key,root);}/* find the node containing the key. If not found, return NULL */
                int depth(){d(root);} /* the depth of the tree */
                ~Binary_Tree(){remove(root);}
                void put_widechar(char c[],char c2[]){c[0]=c2[0];c[1]=c2[1];}
                int even(int n){
                                   if(n%2!=0)return n-1;
                                   else return n;
                                   }
                void remove(Node *node){
                                       if(node->left!=NULL)remove(node->left);
                                       if(node->right!=NULL)remove(node->right);
                                       delete node;
                                       }
                                
        protected:
                Node *f(const T& key, Node *p){
                                               if(p->data==key)return p;
                                               else{
                                                   if(p->left!=NULL){
                                                                     if(f(key,p->left)!=NULL)return f(key,p->left);
                                                                     }
                                                   if(p->left!=NULL)
                                                   {
                                                   if(f(key,p->right)!=NULL)return f(key,p->right);
                                                   }
                                                   return NULL;
                                                   }
                                               }
                void o(ostream &os, Node *p) const{
                                            
                                                if(p!=NULL){
                                                            if(p->left!=NULL){o(os,p->left);}
                                                            //else {cout<<"NULL";}
                                                            if(p->right!=NULL){o(os,p->right);}
                                                            //else{cout<<"NULL";}
                                                            if(p->left==NULL&&p->right==NULL)cout<<p->data<<endl;
                                                            }
                                                            /*
                                                if(p->left!=NULL){o(os, p->left);}
                                                
                                                if(p->right!=NULL){o(os, p->right);}
                                                */
                                             }
                int d(Node *p){
                               if(p==NULL)return 0;
                               else        {
                                           if(d(p->left)>d(p->right))return d(p->left)+1;
                                           else return d(p->right)+1;
                                           }
                               }
                
                          Node *root;
                
};
template <class T>
void Binary_Tree<T>::Display(ostream &os, int width)
{
    int row=2*depth()-1;
    vector<char> *line=new vector<char>[row];
    for (int i=0; i<row; i++) line[i].resize(width,' ');
    Display0(width, even(width/2), line, 0, root); /* even function change a number to even if it is odd */
    for (int i=0; i<row; i++)
    {
    for (int j=0; j<width; j++) os<<line[i][j];
    os<<endl;
    };
    delete [] line;
};
template<class T>
void Binary_Tree<T>::Display0(int width, int offset, vector<char> *line, int dep, Node *node)
{
    if (node==NULL) return;
    else
    {
        for (int i=0; i<node->data.length(); i++)
        line[dep][offset-node->data.length()/2+i]=node->data[i];
        int left=even(offset-width/4);
        int right=even(offset+width/4);
        if (node->left!=NULL || node->right!=NULL)
        {
            put_widechar(&line[dep+1][left],"¢z");/* put_widechar copy a two bytes character string to memory */
            for (int i=left+2;i<offset; i+=2) put_widechar(&line[dep+1][i],"¢w");
            put_widechar(&line[dep+1][offset],"¢r");  
            for (int i=offset+2;i<right; i+=2)
            put_widechar(&line[dep+1][i],"¢w");
            put_widechar(&line[dep+1][right],"¢{");
        };
    Display0(width/2, left, line, dep+2, node->left);
    Display0(width/2, right, line, dep+2, node->right);
    };
};

class huffman_node
{
      public:
             huffman_node(){freq=0;}
             huffman_node&  operator = (const huffman_node& a){c=a.c;freq=a.freq;}
             //friend bool operator > (const huffman_node& a,const huffman_node& b){return a.freq<b.freq;}
             friend bool operator < (const huffman_node& a,const huffman_node& b){return a.freq>b.freq;}
             friend ostream& operator<<(ostream& os, const huffman_node& a){os<<a.c<<" : "<<a.freq; return os;}
             char c; // the character
             int freq; // its frequency};
            
};

class Huffman_Tree: public Binary_Tree<huffman_node>
{
      public:
             void build_freq(istream &is){
                                          char a;
                                          is>>a;
                                          if(is) ft[a]=ft[a]+1;
                                          }
             void build_tree(){
                                   map<char, int>::iterator it;
                                   for ( it=ft.begin() ; it != ft.end(); it++ )
                                   {
                                       Node temp;
                                       temp.data.c=(*it).first;
                                       temp.data.freq=(*it).second;
                                       pq.push(temp);
                                   }
                                       
                                   for ( it=ft.begin() ; it != ft.end(); it++ )cout<<(*it).first<<" : "<<(*it).second<<endl;
                                   Node  *at, *bt;
                                   while(pq.size()>1)
                                   {
                                                   
                                                   at = new Node;
                                                   *at=pq.top();
                                                   pq.pop();
                                                   
                                                   bt = new Node;
                                                   *bt=pq.top();
                                                   pq.pop();
                                                   
                                                   Node m;
                                                   m.left=at;
                                                   m.right=bt;
                                                   m.data.freq=(at->data.freq)+(bt->data.freq);
                                                   
                                                   pq.push(m);
                                   }
                                   root = new Node;
                                   *root=pq.top();
                              }
             void build_code(){string ctemp;bt(root,ctemp);}
             void output_tree(ostream &os){o(os,root);}
             void output(ostream &os){
                                      map<char, string>::iterator it;
                                      for ( it=ct.begin() ; it != ct.end(); it++ )cout<<(*it).first<<" => "<<(*it).second<<endl;
                                     }
       
     
              map<char, int>    ft;//freq
              map<char, string> ct;//code
              priority_queue<Node> pq;
              void bt(Node *p, string ctemp)
              {
                   
                   cout<<p->data<<"  code:  "<<ctemp<<endl;
                   if(p!=NULL)
                   {
                              if(p->left!=NULL)
                              {
                                          bt(p->left,ctemp+"0");
                              }
                              if(p->right!=NULL)
                              {
                                          bt(p->right,ctemp+"1");
                              }
                              if(p->left==NULL&&p->right==NULL)ct[p->data.c]=ctemp;
                   }
                   else
                   {
                       cout<<"ERROR"<<endl;
                   }
              }
};
int main()
{
    
    char c;
    Huffman_Tree ht;
    ifstream is("hm10_data.txt");
    while(1)
    {
            
            if(is)
            {
                  
                  ht.build_freq(is);
                  }
            else break;
    }
    ht.build_tree();
    ht.build_code();
    ht.output(cout);
    ht.output_tree(cout);
    //ht.Display(cout,80);
    system("pause");
    return 0;
}
