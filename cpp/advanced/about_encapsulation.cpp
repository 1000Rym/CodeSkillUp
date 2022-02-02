/* This file is made for learning the concept of encapsulations.
The process of implementing encapsulation can be sub-divided into two steps.
step1: The data members should be labeled as private using the private access specifiers.
step2: The member function which manipulate the data members should be labeld as publc using the public access specifier.
*/
#include <iostream>
using namespace std;

class ImplementEncapsulation
{
    private:
        // The data hidden from the outside world.
        int member_var; 

    public:
        void set(int var)
        {
            this->member_var = var;
        }

        int get(){
            return member_var;
        }
};

int main(){
    ImplementEncapsulation object; 
    object.set(10);
    cout << object.get() << endl;
    return 0;
}