#include <iostream>
using namespace std; 

int var = 10;

int main(){
    // unlike python global variable can be accessed without declare a global keyword.
    var = 12;

    // we declare a local variable which have same name with glboal variable.
    int var = 20; 

    // the variable is appointing local variable.
    cout << var <<  endl;
    cout << ::var<< endl; //To access global variable 

    return 0; 
}