#include <iostream>
#include <vector>
using namespace std;

int main(){
    // Initialize the elements and push 10 elements on the vector.
    vector<int> m_vector; 
    for (int i = 1 ; i <=10 ; i++){
        m_vector.emplace_back(i);
    }

    // capacity functions
    // 1. size(): Returns the number of elements in the vector.
    // size: 10
    cout << "size: " << m_vector.size() << endl; 
    
    // 2. capacity(): Returns the size of the storage space currently allocated to the vector.
    // capacity: 16
    cout << "capacity: " << m_vector.capacity() << endl;
    
    // 3. max_size() : Returns the number of elements that the vector can hold.
    // max_size: 4611686018427387903
    cout << "max_size: " << m_vector.max_size() << endl;
    cout << "empty: " << m_vector.empty() << endl;
    
    // 4. resize(): Resize the containers to hold(n) elements, But not destroy other elements.
    // resize(5) size: 5
    // But consist memory is as the following: 1 2 3 4 5 6 7 8 9 10 
    m_vector.resize(5);
    cout << "resize(5) size:  " << m_vector.size() << endl;
    cout << "Consit memory:";
    auto iter = m_vector.cbegin();
    for (int  i = 0; i <10; i ++){
        cout << *iter ++ << " ";
    }
    cout << endl;
    
    // 5. shrink_to_fit(): Returns the size of the storage space currently allocated to the vector. 
    // shrink_to_fit(): 1 2 3 4 5 6 7 8 0 0 
    // capacity(): 5
    cout << "shrink_to_fit(): ";
    m_vector.shrink_to_fit();
    auto iter2 = m_vector.cbegin();
    for (int  i = 0; i <10; i ++){
        cout << *iter2 ++ << " ";
    }
    cout << endl;
    cout << "capacity():" << m_vector.capacity() << endl;

    // 6. reserve(): Requests that the vector capacity be at least enough to contain n elements.
    // reserve(10) capacity: 10
    m_vector.reserve(10);
    cout << "reserve(10) capacity: " << m_vector.capacity() <<endl; 

    return 0; 
}