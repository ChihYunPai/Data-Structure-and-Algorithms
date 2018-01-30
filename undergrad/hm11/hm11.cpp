#include<iostream>
#include<fstream>
#include<vector>
#include<cmath>
using namespace std;

template <class T> class Binary_Tree
{
         public:
                class Node
                {
                    public:
                           Node(){left=NULL;right=NULL;}
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
                void o(ostream &os, Node *p){
                                                T m, l, r;
                                                if(p!=NULL){
                                                            m=p->data;
                                                            if(p->left!=NULL){l=p->left->data;}
                                                            else {l="NULL";}
                                                            if(p->right!=NULL){r=p->right->data;}
                                                            else{r="NULL";}
                                                            if(l!="NULL"||r!="NULL")cout<<m<<" "<<l<<" "<<r<<endl;
                                                            }
                                                if(p->left!=NULL){o(os, p->left);}
                                                
                                                if(p->right!=NULL){o(os, p->right);}
                                                
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

 template <class T> void Binary_Tree<T>::input(istream &is)
{
          
              T m, l, r;
              while(1)
              {
                       is>>m>>l>>r;
                       Node *mt, *lt, *rt;
                       if(is)
                       {
                       if(root!=NULL){
                                      mt=find(m);
                                    if(l!="NULL"){
                                                  lt=new Node;
                                                  mt->left=lt;
                                                  lt->data=l;
                                                  }
                                    if(r!="NULL"){
                                                  rt=new Node;
                                                  mt->right=rt;
                                                  rt->data=r;
                                                  }
                                   }
                       else        {
                                    mt=new Node;
                                    root=mt;
                                    root->data=m;
                                    if(l!="NULL"){
                                                  lt=new Node;
                                                  root->left=lt;
                                                  lt->data=l;
                                                  }
                                    if(r!="NULL"){
                                                  rt=new Node;
                                                  root->right=rt;
                                                  rt->data=r;
                                                  }
                                    }
                        }
                       else break;
                       
                       }

}
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

template<class T> class BST: public Binary_Tree<T>
{
               public:
                      void input(istream &is);
                      void output(ostream &os){o(os,this->root);}
                      typename Binary_Tree<T>::Node *find(const T& key){f(key,this->root);}
                      void insert(const T& data);
                      
               private:
                       void o(ostream &os,typename Binary_Tree<T>::Node *p)
                       {
                                                    if(p!=NULL)
                                                    {
                                                               if(p->left!=NULL)o(os,p->left);
                                                               cout<<p->data<<endl;;
                                                               if(p->right!=NULL)o(os,p->right);
                                                    }
                       }
                       void i(const T& data, typename Binary_Tree<T>::Node *p)
                       {
                            if(p==NULL){
                                        p->data=data;
                                        }
                            if(data<p->data)
                            {
                                        i(data,p->left);    
                            }
                            if(data>p->data)
                            {
                                 i(data,p->right);
                            }
                       }
                       typename Binary_Tree<T>::Node *f(const T& key, typename Binary_Tree<T>::Node *p)
                         {
                           if(key==p->data)return p;
                           else if(key<p->data){
                                                 if(p->left!=NULL)return f(key,p->left);
                                                 else return NULL;
                                                }
                           else{
                                if(p->right!=NULL)return f(key,p->right);
                                else return NULL;
                                }
                         }
};

template <class T> void BST<T>::insert(const T& data)
{
              T m, u;
              typename Binary_Tree<T>::Node *mt, *ut;
              m=data;
                           if(this->root!=NULL){
                                              mt=new typename Binary_Tree<T>::Node;
                                              u=this->root->data;
                                              ut=this->root;
                                              while(1)
                                              {
                                                  if(m<u)
                                                  {
                                                         if(ut->left==NULL)
                                                         {
                                                             ut->left=mt;
                                                             mt->data=m;
                                                             break;
                                                         }
                                                         else {
                                                              ut=ut->left;
                                                              u=ut->data;
                                                              }
                                                  }
                                                  else
                                                  {
                                                         if(ut->right==NULL)
                                                         {
                                                             ut->right=mt;
                                                             mt->data=m;
                                                             break;
                                                         }
                                                         else {
                                                              ut=ut->right;
                                                              u=ut->data;
                                                              }
                                                   }
                                              }
                                          }
                           else        {
                                        mt=new typename Binary_Tree<T>::Node;
                                        this->root=mt;
                                        this->root->data=m;
                                        }
}
template <class T> void BST<T>::input(istream &is)
{
              T m, u;
              typename Binary_Tree<T>::Node *mt, *ut;
              while(1)
              {
                       is>>m;
                       if(is)
                       {
                           insert(m);
                          
                        }
                       else break;
                       
               }
}

int main()
{
    Binary_Tree<string> bt;
    BST<string> bst;
    
      cout<<"HM10 : Binarey_Searh_Tree\n"<<endl;
      
      ifstream is("hm10_data.txt");
      bt.input(is);
      bt.output(cout);
      bt.Display(cout, 80);
      cout<<"depth is : "<<bt.depth()<<endl;
      
      cout<<"HM11 : Binarey_Searh_Tree\n"<<endl;
      
      ifstream is2("hm11_data.txt");
      bst.input(is2);
      bst.output(cout);
      bst.Display(cout, 80);
      
      string n;
      while(1)
      {   
          cout<<"input a word : \n";
          cin>>n;
          if(n!="esc")
          {
              bst.insert(n);
              bst.output(cout);
              bst.Display(cout, 80);
              }
          else break;
          
          }
      
      system("pause");
      return 0;
}
