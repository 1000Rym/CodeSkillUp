// Forest.1000
// Created Date: 2021.01.17 
// This code is made for leaning handing exception by
// using class. 

#include <iostream>
#include <stdexcept>

using namespace std;

class DivideByZero : public runtime_error{
    public: 
        DivideByZero() : runtime_error("Divide by zero exception"){}
};

template <typename T>
T divide(T number,T denom){
    if (denom == 0) throw DivideByZero(); 
    else return number/denom; 
}

int main(){
    int number1 = 10, number2 = 0; 
    cout << divide (number1, number2) <<endl;
}