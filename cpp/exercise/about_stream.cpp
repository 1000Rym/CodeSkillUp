#include<iostream>
using std::cin;
using std::cout;
using std::endl;
using std::string;

int main(){
    string s;
    cin >> s; 
    
    // Move to next word position.
    char peek = std::cin.rdbuf()->snextc();
    if (std::cin.fail()) std::cout << "Failed!";
    cout << "second word's first character:" << peek << endl;
    cin >> s; 
    cout << "read again:" << s << endl;
}