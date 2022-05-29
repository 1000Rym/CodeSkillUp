/*
    GCD(Greateast Common Divisor) : Implment GCD logic with generic meta programming.
*/
#include <iostream>
using std::cout, std::endl;

template<int X, int Y>
struct GCD{
    static const int value = GCD<Y, X%Y>::value;
};

template <int X>
struct GCD<X, 0>{
    static const int value = X; // non-const static data member must be intialized out of line.
}; 


/* Implement GCD(Greatest Common Divisor) with function. */
int gcd(int a, int b){
    if (b == 0){
        return a; 
    } else {
        return gcd(b, a%b);
    }
}

int main(){
    cout << "gcd(24, 36)=" << gcd(24, 36) << endl;
    cout << "GCD(24, 36)=" << GCD<36, 24>::value << endl;
}