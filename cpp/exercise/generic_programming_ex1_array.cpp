/*
    Generic Programming Exercise: Implment a customized array class.
*/
#include <iostream>

using std::cout;
using std::endl;

template<typename T, unsigned int N>
class Array{
    T data_[N]; // declare N size array.
    public:
        /* Construct an array with recieved array.*/
        Array(T (&arr)[N]){ // Recieve ref as the sized array.
            for (int i = 0; i < N; i ++){
                data_[i] = arr[i]; // copy the reference data to data_
            }
        }

        /* Return the array size. */
        unsigned int size(){ return N; }

        /* Return Array */
        T* get_array(){ return data_; } 

        /* Print the element in the array. */
        void print_array(){
            for (auto  element : data_){
                cout << element << " ";
            }
            cout << endl;
        }
};

int main(){
    // Test code that test array.
    int arr_int[5] = {1,2,3,4,5};
    Array<int, 5> arr_custom(arr_int);
    arr_custom.print_array(); 
}