/*
    In this code, we are going to learn sorting algorithm in c++ stl sort.
    - sort : Original sorting algorithm supported in c++. 
        - To support sort the container must support 'RandomAccessIterator'(vector, deque).
        - Default: Acending order.
    - stable_sort: keep original order when the value is equal(slower than sort).
    - paritial_sort: Do partial sort.
*/

#include <algorithm> // To support sorting algorithm.
#include <iostream>
#include <string_view>
#include <vector>
#include <random> // To generate random number

using std::cout, std::endl;
using std::vector;
using std::random_device;
using std::string_view;
using std::sort, std::stable_sort, std::partial_sort;

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
struct NUM_GREATER{
    bool operator()(const T& a, const T& b) const { return a > b; }
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
    
    // sort-1 : sort default asscending order.
    sort(vec.begin(), vec.end());
    print_container_elements(vec.begin(), vec.end(), "Sorting Elements:");

    // sort-2: sort the container with customized function(descending order). 
    sort(vec.begin(), vec.end(), NUM_GREATER<int>());
    print_container_elements(vec.begin(), vec.end(), "Sorting Elements with specific func(Descending Order):");

    // stable_sort: sort the elment with the stable_sort. 
    stable_sort(vec.begin(), vec.end(), NUM_GREATER<int>());
    print_container_elements(vec.begin(), vec.end(), "Sorting Elements with stale_sort:");
    
    // partial sort the container.
    partial_sort(vec.begin(), vec.begin()+3, vec.end());
    print_container_elements(vec.begin(), vec.end(), "Partial sort the container(start, +3, end): ");
    
}

