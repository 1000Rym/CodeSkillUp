#include <iostream>
#include <string>
using namespace std;

int main(){
    int x , y = 0;
    auto pair1 = make_pair("Bill", 18);
    auto pair2 = make_pair("Tom", 21);
    auto pair3 = make_pair(1,2);

    // Before swap function.
    cout << pair1.first <<' '<< pair1.second <<endl;
    
    // After the swap function.
    pair1.swap(pair2);
    cout << pair1.first <<' '<< pair1.second <<endl;

    // Use tie(Same with tuple.
    tie(x,y) = pair3;
    cout << pair3.first <<' '<< pair3.second<< endl;
}

