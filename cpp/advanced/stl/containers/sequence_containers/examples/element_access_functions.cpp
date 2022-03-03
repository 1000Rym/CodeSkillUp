#include <iostream>
#include <vector>

using namespace std;

int main(){
    
    // Initialize the elements and push 10 elements on the vector.
    vector<int> m_vector; 
    for (int i = 1; i <= 10 ; i ++){
        m_vector.emplace_back(i*10);
    }
    
    // 1. Reference Operator [n],at(n) : Returns the reference to an element at position n.
    //m_vector[2]:30
    //m_vector.at(2):30
    cout << "m_vector[2]:" << m_vector[2] << endl;
    cout << "m_vector.at(2):" << m_vector.at(2) << endl;

    // 2. front() and back() : Returns a reference to the first/last element in the container.
    // m_vector.front():10
    // m_vector.back():100
    cout << "m_vector.front():" << m_vector.front() << endl;
    cout << "m_vector.back():" << m_vector.back() << endl;

    // 3. data(): Returns a direct pointer to the memory array used internally by the container to store its owned elements.
    // *m_vector.data():10
    cout << "*m_vector.data():"<< *m_vector.data() << endl;

    return 0;
}