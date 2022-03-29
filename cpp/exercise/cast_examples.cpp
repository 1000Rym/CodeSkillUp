/*
 In this code we are going to learn cast related to c++ cast.
 About cast: 
 - static cast: converts between types using a combination of implicit and user-defined conversions.
 - const_cast: change the constant value of any object(remove `const` nature of any object.)
 - dynamic_cast: using for the downcasting.
    - downcasting: casting a base class pointer(or reference) to derived class pointer(or reference)
    - upcasting: casting a derived class pointer(or reference) to base class pointer(or reference) 
 - reinterpret_cast: do cast via unrelated pointers(dangerous behavior)
*/
#include <iostream>

using std::cout;
using std::endl;

class BaseClass{
    public: 
    void print(){
        cout << "This is the base class." << endl;
    }
};

class DerivedClass: public BaseClass{
    public: 
    void print(){
        cout << "This is the derived class1." << endl;
    }
};


int main(){
    // 1. static cast
    // > variable after change float_origin_var:5
    // > variable after change float_static_cast_var:5    
    int int_variable = 5; 
    auto float_origin_var = (float)int_variable; // Original C type explicit-cast.
    auto float_static_cast_var = static_cast <float> (int_variable); // C++ static cast.
    cout << "variable after change float_origin_var:" << float_origin_var << endl;
    cout << "variable after change float_static_cast_var:"<< float_static_cast_var << endl;

    // 2.const_cast
    const int const_variable = 10;
    const int* const_variable_ptr = &const_variable;
    cout << "const variable before changed: " << *const_variable_ptr << endl;
    int* const_cast_variable = const_cast<int *>(const_variable_ptr);
    *const_cast_variable = 20;
    cout << "const variable ptr value after changed: " << *const_variable_ptr << endl;
    cout << "const variable ptr value after changed: " << const_variable << endl;

    // 3. dynamic cast 
    DerivedClass derived;
    // > This is the derived class1.
    derived.print();
    // > This is the base class.
    BaseClass* dynamic_casted_obj = dynamic_cast<BaseClass*>(&derived);
    dynamic_casted_obj->print();

    // 4. reinterpret_cast
    BaseClass base;
    // > This is the base class.  
    base.print();
    DerivedClass* reinterpret_casted_obj = reinterpret_cast<DerivedClass*>(&base);
    // > This is the derived class1.
    reinterpret_casted_obj->print();

}