#include <iostream>
using namespace std;

int main(){
    // initilize the array with the array size and specifiying the values.
    int arr[10] = {1,2,3,4,5};

    // way to access built-in array: 1 
    // output: 1 2 3 4 5 0 0 0 0 0
    for(int index = 0; index < 10; index ++){
        cout << arr[index]<< " ";
    }
    cout <<endl;
    
    // way to access built-in array: 2
    for (int index = 0; index < 10; index ++){
        cout << index[arr] <<" "; 
    }
    cout <<endl; 

    // Access the firs second elements of the array.
    cout <<1[arr] <<endl;

    return 0;
}