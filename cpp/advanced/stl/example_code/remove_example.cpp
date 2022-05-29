/*
    In this code, we are going to learn sorting algorithm in c++ stl erase and remove.
*/

#include <algorithm> // To support remove and erase algorithm.
#include <iostream>
#include <string_view>
#include <vector>
#include <random> // To generate random number

using std::cout, std::endl;
using std::vector;
using std::random_device;
using std::string_view;
using std::remove_if;

/* Print the container elements*/
template <typename ITER> 
void print_container_elements(ITER begin, ITER end, string_view description= ""){
    cout << description << "";
    while (begin != end){
        cout << *begin << " ";
        begin ++; 
    }
    cout << endl;
}

template<typename T>
struct IsOdd{
    bool operator()(const T& num) const { return !(num % 2); }
};

int main(){
    // initilize the random generator.
    random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<int> dis(1, 100); // generate number via 1 to 100
    vector<int> vec;

    // push the random generated number to vector.
    for (int i = 0; i < 10; i ++){
        vec.emplace_back(dis(gen));
    }
    print_container_elements(vec.begin(), vec.end(), "Original Elements:");
    
    // remove_if: remove the container if fit condition, return the removed iterator.
    vec.erase(remove_if(vec.begin(), vec.end(), IsOdd<int>()), vec.end());
    print_container_elements(vec.begin(), vec.end(), "Removed Odd Elements:");
}