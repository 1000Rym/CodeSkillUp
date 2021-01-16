//Author: Forest.1000
//Date: 2021.01.16
//This file is made for practice generic programming
//generic fuction
#include <iostream>

using namespace std;

int compareInt(int value1, int value2){
    if (value1>=value2) return value1; 
    else return value2; 
}

double compareDouble(double value1,double value2){
    if(value1>=value2) return value1; 
    else return value2; 
}

template <typename T>
T compare(T value1, T value2){
    if (value1>=value2) return value1;
    else return value2; 
}


int main(){
    int integer1 = 1 , integer2=2;
    double double1 = 1.1, double2 = 2.2;
    string string1 ="apple", string2 ="pear";
    cout << "Int: bigger one is" << compareInt (integer1, integer2)<<endl;
    cout << "Double: bigger one is" << compareDouble (double1, double2)<<endl;
    cout << "Bigger one is " << compare(integer1, integer2)<< endl;
    cout << "Bigger one is " << compare(double1, double2)<< endl;
    cout << "Bigger one is " << compare(string1, string2)<< endl;    
}
