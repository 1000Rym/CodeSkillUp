#include <iostream>
using namespace std;

static int myFunc(){
    static int value = 0;
    value ++; 
    return value; 
}

int main(){
    int a = (myFunc(), myFunc(), myFunc());
    cout << a << endl;
}