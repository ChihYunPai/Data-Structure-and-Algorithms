#include<iostream>
#include<string>
#include<sstream>
using namespace std;

class Random {
        public:
            Random() {
                     std::srand(std::time(0));
                     }
            Random(int seed) {
                     std::srand(seed);
                     }
            int next_int(int n) {
                    return int(next_double() * n);
                    }
            double next_double() {
                    return double(std::rand()) / RAND_MAX;
                    }
};
Random my_random; /* declared globally such that all classes use the same one */
double p=my_random.next_double(); /* get a number equally distributed between 0 and 1 */
int n=my_random.next_int(10) ;/* get an integer equally distributed between 0 and 9 */

int main()
{
    Random x;
    //cout<<"Random(): " <<x.Random()<<endl;
    //cout<<"Random(int seed): "<<x.Random(3)<<endl;
    cout<<"p:"<<p<<endl;
    cout<<"n:"<<n<<endl;
    cout<<"RAND_MAX:"<<RAND_MAX<<endl;
    cout<<"next_int(int n): "<<x.next_int(10) <<endl;
    cout<<"next_double(): "<<x.next_double()<<endl;
    system("pause");
    return 0;
}
