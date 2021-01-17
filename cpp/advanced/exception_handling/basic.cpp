#include <iostream>
using namespace std;

const int DivideByZeroExcption = 1; 
int main(){
    int number = 5, denom = 0; 
    
    try {
        if (denom == 0) throw DivideByZeroExcption;
        else cout << number/denom <<endl; 
    } /*catch(int e){
        if (e==DivideByZeroExcption) cout << "Divide By 0  is illegal";
    }*/ catch(...){
        cout << "An unidentified exception caught."<<endl;
    }
}