//Author: Forest.1000
//Date: 2021.01.16
//This file is made for practice generic programming
//multiple template function
# include <iostream>
using namespace std;

template <typename T, typename U>
T compare(T value1, U value2){
    return (value1 >= value2) ? value1 : value2;
}

int main(){
    int value1 = 20; 
    double value2 = 30.2; 
    cout<<"max value is the " << compare(value2, value1)<<endl; //30.2
    cout<<"max value is the " << compare(value1, value2)<<endl; //30
}
