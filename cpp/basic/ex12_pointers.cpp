#include <iostream>
using namespace std;

int main(){
    // Declare and instantiate variables.
    int int_var = 10;
    int int_vars[3] = {10,20,30};

    // Declare int type pointers and assign address value.
    int *int_var_ptr = &int_var;
    int *int_vars_ptr = int_vars;

    // access value by dereferencing.
    cout<< "Integer value was: " << *int_var_ptr << endl;
    
    for (int i = 0; i < 3; i ++){
        cout << i << "th index value is " << *int_vars_ptr <<endl;
        // Move to the next address
        int_vars_ptr ++;
    }

    return 0;
}