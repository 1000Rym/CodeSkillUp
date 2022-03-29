/*
 This code will show example case of const function and mutable member variable.
*/
#include <iostream>

using std::cout; 
using std::endl;

class ConstClass{
    mutable int mutable_data_;
    int const_data_;

    public:
        ConstClass(int const_data, int mutable_data): const_data_(const_data), mutable_data_(mutable_data){
            cout << "const_data: " << const_data_;
            cout << " mutable_data: " << mutable_data_ << endl;
        }
        void set_data(int const_data, int mutable_data) const{
            // const_data_ = const_data;  The member variable in const function can not be changed.
            mutable_data_ = mutable_data; // however, variable declared with mutable can be changed in const function.
            cout << "const_data: " << const_data_;
            cout << " mutable_data: " << mutable_data_ << endl;
        }
};

int main(){
    ConstClass const_obj(2,3);
    const_obj.set_data(4,6);
}