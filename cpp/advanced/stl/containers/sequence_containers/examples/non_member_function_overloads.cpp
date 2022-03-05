#include <iostream>
#include <array>
#include <vector>
using namespace std;

template <typename T>
void print_container_elements(string_view description, const T & container){
    cout << description;
    for (auto element : container){
        cout << element << " ";
    }
    cout << endl;
}

int main(){
    array<int , 5> m_array1 = {1,2,3,4,5};
    array<int , 5> m_array2 = {1,2,3,4,5};
    array<int , 5> m_array3 = {5,4,1,2,3};
    
    // 1. get<index>(container) : Get an element from the container.
    // > get<2>(m_array): 3
    cout << "get<2>(m_array): "<< get<2> (m_array1)<<endl;

    // 2. relational operation: ==, !=, >, >=, <, <=
    // > m_array1 == m_array2: 1
    // m_array1 >= m_array2: 0
    cout <<  "m_array1 == m_array2: "<< (m_array1 == m_array2) << endl;
    cout <<  "m_array1 >= m_array2: "<< (m_array1 >= m_array3) << endl;

    // 3. swap
    // > m_vector1: 4 5 6 7 8 
    // > m_vector2: 1 2 3 4 5 
    vector<int> m_vector1 = {1,2,3,4,5};
    vector<int> m_vector2 = {4,5,6,7,8};
    swap(m_vector1, m_vector2);
    cout << "swap(m_vector1, m_vector2)"<<endl;
    print_container_elements("m_vector1: ", m_vector1);
    print_container_elements("m_vector2: ", m_vector2);

}