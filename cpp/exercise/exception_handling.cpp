/*
    In this code, we are going to learn about exception handling. 
    - 1. throw an out of range exception. 
*/
#include <iostream>
#include <vector>

using std::cout, std::endl;
using std::vector;
using std::out_of_range;

template<typename T, unsigned int N>
class CustomizedArray{
    T* data_;

    public:
        /* copy constructor */
        CustomizedArray(const T (&container)[N]){
            data_ = new T[N];

            for (int i = 0; i < N; i ++){
                data_[i] = container[i];
            }
        }

        /* Return the element located at the target index. */
        const T& at(size_t index) const {
            if (index > N){
                throw out_of_range("Target index is out of the customized array's range.");
            }

            return data_[index];
        }

        /* Print the elements in the container. */
        void print(){
            for(T element : data_){
                cout << element << " ";
            }
            cout << endl;
        }

        /* Delete the customized array. */
        ~CustomizedArray(){
            cout << "customized array deleted!" << endl;
            delete[] data_;
        }

        
};

int main(){
    int arr_int[5] = {11,22,35,42,52};
    CustomizedArray<int, 5> mc_array(arr_int);
    cout <<  "second index of the array is " << mc_array.at(2) << endl;
    
    try {
        cout << "100 index of the array is " << mc_array.at(100) << endl;
    }catch(out_of_range e){
        // event is called immediatlly after the exception is happened.
        cout << "Out of array index error called. " << e.what() << endl;   
    }catch(...){ // Default exception(usually catch the unknown exception)
        cout << "Default exception is called!" << endl;  
    }
    cout << "end print the array." << endl;
}