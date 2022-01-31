#include <iostream>
using namespace std;

// When define macro we don't need add any semiclon.
# define MAXNUM 9999

// We can also define macros with the arguments.
# define AREA(a,b) (a*b)


int main(){
    cout << "Max value is " << MAXNUM << endl;
    cout << "The Area(10,20) is " << AREA(10,20) <<endl;
    return 0;
}