// Forest.1000
// Date: 01.19.2021
// This code is made for leaning generic algorithm 
// read - only algorithm.
#include <iostream>
#include <vector>
using namespace std; 

void testFind(vector<int> vectInt, vector<string> vectString){
    vector<int>::iterator iterInt;
    vector<string>::iterator iterString;

    iterInt = find(vectInt.begin(), vectInt.end(),111);

    if (iterInt != vectInt.end()){
        cout << "We find the number in " << *iterInt << " vector" <<endl;
    }else {
        cout << "We could not find the target number"<<endl; 
    }

    iterString = find(vectString.begin(), vectString.end(), "This");
    if (iterString != vectString.end()){
        cout << "We find the string `" << *iterString << "` from string type vector" <<endl;
    }else {
        cout << "We could not find the target string."<< endl;
    }
}

int main(){
    
    //input 100~109
    vector<int>vectInt;
    for (int i = 0; i<10; i ++) {
        vectInt.push_back (100+i);
    }

    //input happy new year this year is 2021. welcome
    vector<string>vectString; 
    vectString.push_back("Happy");
    vectString.push_back("New");
    vectString.push_back("Year");
    vectString.push_back("This");
    vectString.push_back("Year");
    vectString.push_back("is");
    vectString.push_back("2021");
    vectString.push_back("Welcome!");

    testFind(vectInt, vectString);
}