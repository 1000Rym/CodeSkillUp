/*
    Practice Lambda Expression.
    We can capture external variables from enclosing scope by 3 ways.
    - Capture by reference
    - Capture by value(copy)
    - Capture by mixed value

    Reference: geeksforgeeks.org/lambda-expression-in-c
*/
#include <iostream>
#include <vector>
#include <string_view>
#include <string>

using std::cout, std::endl;
using std::string_view, std::string;
using std::vector;

template<typename T>
void print_containers(const T &container, string_view description= ""){
    cout << description;
    for (auto element : container){
        cout << element << " ";
    }
    cout << endl;
}

int main(){
    
    vector<int> v1= {1,11,54,23,12};

    // Capture by reference[&]
    auto push_into_vecotrs = [&](int m){
        // Access v1, v2 by reference
        v1.emplace_back(m);
    };
    push_into_vecotrs(20);

    // Caputre by copied object
    auto print_v1 = [v1](){
        // copy v1 object.
        cout << "v1 :";
        for (auto element : v1){
            cout << element << " ";
        }
        cout << endl;
    };
    print_v1();

    int target_number = 20; 

    // = means can access all elements
    int bigger_nums = count_if(v1.begin(), v1.end(), [=](int element){
        return element > target_number;
    });
    cout << "count:" << bigger_nums << endl;

    string description = "v1_description:";
    // mixed access
    auto print_v1_with_description = [&v1, description](){
        // access reference v1 with copied description.
        cout << description; 
        for (auto element : v1){
            cout << element << " ";
        }
        cout << endl;
    };
    print_v1_with_description();
}