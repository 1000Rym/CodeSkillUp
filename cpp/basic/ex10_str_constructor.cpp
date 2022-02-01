#include <string>
#include <iostream>
using namespace std;

int main(){
    // empty string constructor
    string str_empty; 
    str_empty = "first string"; //-> first string

    // copy constructor
    string str_cpy(str_empty); //-> first string
    
    // substring constructor
    string str_sub(str_empty, 6, 3); //-> str
      
    // fill constructor
    string str_fill(4, '$');

    // from c string 
    const char *chars1 = "My Chars!"; //-> str
    string str_cstr (chars1);

    // from buffer
    string str_buffer(chars1, 2);

    // range constructor
    string str_range(str_empty.begin(),str_empty.begin()+5);


    cout << str_empty << endl;
    cout << str_cpy << endl;
    cout << str_sub << endl;
    cout << str_fill << endl;
    cout << str_cstr << endl; 
    cout << str_buffer << endl; 
    cout << str_range << endl;

    return 0;
}