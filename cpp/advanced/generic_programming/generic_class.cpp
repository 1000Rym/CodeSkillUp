//Author: Forest.1000
//Date: 2021.01.16
//This file is made for practice generic programming
//generic class

#include <iostream>
using namespace std; 

//stack is a first in last out stucture.
template <typename T>
class Stack{
    private: 
        T store[100];
        int top; 
    public :
        Stack () : top(-1){}

        //push value to the top 
        void push(T value) {
            ++top;
            store[top] = value;  
        }
        
        T pop(){
            T value = store[top];
            store[top] = 0;
            --top;
            return value;   
        }

        T peak(){
            return top >-1 ? store[top] : 0; 
        }
};


// using class template specialization
template <>
class Stack<string>{ // should clearly define data type.
    private: 
        string store[100];
        int top; 
    public :
        Stack () : top(-1){}

        //push value to the top 
        void push(string value) {
            ++top;
            store[top] = value;  
        }
        
        string pop(){
            string value = store[top];
            store[top] = "";
            --top;
            return value;   
        }

        string peak(){
            return top >-1 ? store[top] : ""; 
        }
};

int main(){
    Stack<int> intStore;
    intStore.push(1);
    intStore.push(2);
    cout<<intStore.peak()<<endl;

    Stack<double> doubleStore;
    doubleStore.push(1.1);
    doubleStore.push(2.2);
    cout<<doubleStore.peak()<<endl; 

    Stack<string> strStore;
    strStore.push("maggie");
    strStore.push("maria");
    strStore.push("carl");
    cout<<strStore.peak()<<endl;
} 