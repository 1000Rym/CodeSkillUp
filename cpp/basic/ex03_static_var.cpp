#include <iostream>
using namespace std;

void callStaticFunc(){
    // The static variable can be initilzed once, exists until the program ends.
    static int value = 0;
    value ++;

    cout << "The value is now" <<value<<endl;
}


int main(){
    callStaticFunc();
    callStaticFunc();
    return 0;
}