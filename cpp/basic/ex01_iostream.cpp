#include <iostream>
using namespace std;

int main(){
    // use cin with extraction op(>>), use cout with insertion op(<<).
    int age;
    cout << "Please input your age:";
    cin >> age;
    cout << "Your age is " << age << endl;
    cerr << "cerr is using for displaying errors."<<endl;
    clog << "clog is also used for displaying erros, also storing in to the stream buffer." <<endl;
}