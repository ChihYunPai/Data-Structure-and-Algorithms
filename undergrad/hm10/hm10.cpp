#include<iostream>
#include<fstream>
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
                Node *find(const T& key)
                {return f(key,root);}/* find the node containing the key. If not found, return NULL */
                int depth(){d(root);} /* the depth of the tree */
                ~Binary_Tree(){remove(root);}
                void remove(Node *node){
                                       if(node->left!=NULL)remove(node->left);
                                       if(node->right!=NULL)remove(node->right);
                                       delete node;
                                       }
                                
        private:
                Node *f(const T &key, Node *p){
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

int main()
{
      cout<<"HM10 : Binarey_Tree\n"<<endl;
      Binary_Tree<string> bt;
      ifstream is("hm10_data.txt");
      bt.input(is);
      bt.output(cout);
      cout<<"depth is : "<<bt.depth()<<endl;
      system("pause");
      return 0;
}
