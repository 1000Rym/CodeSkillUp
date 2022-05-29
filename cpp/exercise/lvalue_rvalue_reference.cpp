/*
    The code is made for understanding the l-value and r-value references.
*/
#include <iostream>
using std::cout, std::endl;

int main(){
    int a = 10;
    
    // Declareing lvalue reference
    int& lref = a; 
    // Declaring rvalue reference
    int&& rref = 20;


    auto print_ref = [&](){
        cout << "lref= " << lref << endl;
        cout << "rref= " << rref << endl;
    };

    print_ref();

    // Change the value
    cout << "== after change the value(30,40) == " << endl;
    lref = 30;
    rref = 40;
    print_ref();
}