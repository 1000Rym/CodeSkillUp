/*
    This code is made for learning forward declaration.
*/
#include <iostream>
using namespace std;

// Forward Declaration of the class to avoid compiler error.
class A;
class B;

class A{
    public:
        int value;
        void setData(int value){
            this->value = value;
        }

    friend int sum(A a, B b);
};

class B{
    public:
        int value; 
        void setData(int value){
            this->value = value;
        } 

        friend int sum(A a, B b);
};

int sum(A a, B b)
{
    int result;
    result = a.value + b.value;
    return result;
}


int main(){
    A a; 
    B b; 
    a.setData(10);
    b.setData(20);
    cout << sum(a, b) <<endl;
}