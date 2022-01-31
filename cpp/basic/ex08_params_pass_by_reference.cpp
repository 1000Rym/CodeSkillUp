#include <iostream>
using namespace std;

void change_var(int *variable)
{
    *variable = 30;
}

int main()
{
    int var1  = 20;
    cout << "The original value of variable was " <<var1 <<endl;
    change_var(&var1);
    cout << "After calling the function the variable changed to " << var1 <<endl; 
    return 0;
}