/*
    Generic Programming Exercise3- Ratio: Implement a ratio add with generic meta programming.
*/
#include <iostream>

using std::cout, std::endl;

/* Struct: Ratio <Numerator, Denominator(Default 1)> */
template <int N, int D=1>
struct Ratio{
    //typedef Ratio<N, D> type;
    using type = Ratio <N, D>;
    static const int numerator = N; 
    static const int denominator = D;
};

/* Ratio Logic: Adder*/
template <class Ratio1, class Ratio2>
struct _Ratio_adder{
    // typedef Ratio<Ratio1::numerator * Ratio2::denominator + Ratio2::numerator * Ratio1::denominator, 
    //                 Ratio1::denominator * Ratio2::denominator> type;  

   using type = Ratio<Ratio1::numerator * Ratio2::denominator + Ratio2::numerator * Ratio1::denominator, 
                    Ratio1::denominator * Ratio2::denominator> type;     
};

/* Ratio Wrapper */
template <class Ratio1, class Ratio2>
struct Ratio_Adder : _Ratio_adder<Ratio1, Ratio2>::type{};

int main(){
    typedef Ratio<2,3> ratio1; 
    typedef Ratio<3,2> ratio2; 
    // typedef Ratio_Adder<ratio1, ratio2> ratio3;  // original definition of ratio3
    using ratio3 = Ratio_Adder<ratio1, ratio2>; // keyword `using` is more suggested since C++ ver11 to increase the readability.

    cout << ratio3::numerator << "/" << ratio3::denominator << endl;
}