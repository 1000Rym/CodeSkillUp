#include <iostream>
#include <string>
using namespace std;

int main(){
    string str_sample("Hello, sample string.");
    string str_assign; 
    
    // assign operator
    str_assign = str_sample;
    cout << "Assined String: "<< str_assign <<endl;
    
    // delete all characters from the string.
    str_assign.clear();
    cout << "The string after cleared: "<< str_assign << endl;

    // lenth of the string
    cout << "len(): " << str_sample.length() <<endl; 
    cout << "size():" << str_sample.size() << endl;
    
    // get the specific char using at.
    cout << "The 2nd index of str: "<<str_sample.at(2) <<endl;

    // get the front and end char of the string.
    cout << "front():" <<str_sample.front() << endl;
    cout << "back():" <<str_sample.back() << endl;

    // find the chars of the specific chars
    cout << "Found index:"<< str_sample.find("string") << endl;

    // substring of the specific string
    cout << "substring(2, 5) is " <<str_sample.substr(2, 6) <<endl;

    // erase the specific characters
    cout << "erase(5) is " <<str_sample.erase(5) <<endl;
    
    // replace the str
    str_sample = "Hello, sample string";
    cout << "replace the sample string:" <<str_sample.replace(7, str_sample.size() - 7,"my world.") << endl;

    return 0; 
}
