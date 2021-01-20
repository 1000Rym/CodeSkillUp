// Forest.1000
// Date: 01.19.2021
// This code is made for leaning generic algorithm 
// read - only algorithm.
#include <iostream>
#include <vector>
#include <numeric>
#include <string> // string accumulate is implemented in string::accumuate
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

void test_foreach(vector<int> vectInt, vector<string> vectString){

    //100 101 102 103 104 105 106 107 108 109 
    //Happy New Year This Year is 2021 Welcome! 

    for_each(vectInt.begin(), vectInt.end(), [] (int number) {
        cout<<number<<" ";
    });

    cout <<endl;

    for_each(vectString.begin(), vectString.end(), [] (string text) {
        cout<<text<<" ";
    });

    cout <<endl;  
}

void test_reverse(vector<int> vectInt, vector<string> vectString){

    //100 101 102 103 104 105 106 107 108 109 
    //Happy New Year This Year is 2021 Welcome! 

    for_each(vectInt.rbegin(), vectInt.rend(), [] (int number) {
        cout<<number<<" ";
    });
    cout <<endl;

    for_each(vectString.rbegin(), vectString.rend(), [] (string text) {
        cout<<text<<" ";
    });
    cout <<endl;  
}

void test_accumulate(vector<int> vectInt, vector<string> vectString){
    int sum = accumulate(vectInt.begin(), vectInt.end(), 0);
    string concat_string;
    concat_string = accumulate(vectString.begin(), vectString.end(), concat_string);

    //sum is 1045
    //cocated string is HappyNewYearThisYearis2021Welcome!
    cout << "sum is " << sum <<endl;
    cout << "cocated string is " << concat_string << endl; 
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

    //testFind(vectInt, vectString);
    //test_foreach(vectInt, vectString);
    //test_accumulate(vectInt, vectString);
    test_reverse(vectInt, vectString);
}