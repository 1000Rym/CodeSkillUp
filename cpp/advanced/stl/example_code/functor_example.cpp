/*
    A functor(or fuction objuect) is a C++ class that acts like a function.
    To create a functor, we usually create a object that overloades the operator()
*/
#include <iostream>

using std::cout;
using std::endl;

class increment{
    private: 
        int added_number;

    public: 
        increment(int number):added_number(number){}
         /*
            1. we can use operator() function to implement a functor.
            2. A const member function cannot change the value of any data member of the class
            and cannot call any member function which is not constant.
         */
        int operator () (int number){
            return added_number + number;
        }
};

int main(){
    int arr[] = {1,2,3,4,5};
    int n = sizeof(arr)/sizeof(arr[0]);

    // use the class operator() to let the class operator act as the fuction pointer.
    std::transform(arr, arr+n, arr, increment(5));
    // result: 6 7 8 9 10 
    cout << "result: ";
    for (int element : arr){
        cout << element << " ";
    }
    cout << endl; 
}

