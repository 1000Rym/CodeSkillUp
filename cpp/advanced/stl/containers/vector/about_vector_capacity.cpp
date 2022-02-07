#include <iostream>
#include <vector>
using namespace std;

int main(){
    vector<int> m_vector; 

    for (int i = 1 ; i <=10 ; i++){
        m_vector.emplace_back(i);
    }

    // About Size
    cout << "size: " << m_vector.size() << endl;
    cout << "capacity: " << m_vector.capacity() << endl;
    cout << "max_size: " << m_vector.max_size() << endl;
    cout << "empty: " << m_vector.empty() << endl;
    
    // About Size Control
    m_vector.resize(5);
    cout << "after resize(5) size is changed to: " << m_vector.size() << endl;
    cout << "And the value saved in consist memory is as the following:" << endl;
    
    auto iter = m_vector.cbegin();
    for (int  i = 0; i <10; i ++){
        cout << *iter ++ << " ";
    }
    cout << endl;

    cout << "after shink_to_fit() the value saved in consist memory is as the following:" << endl;
    m_vector.shrink_to_fit();
    auto iter2 = m_vector.cbegin();
    for (int  i = 0; i <10; i ++){
        cout << *iter2 ++ << " ";
    }
    cout << endl;
    cout << "capacity() is changed to:" << m_vector.capacity() << endl;

    m_vector.reserve(10);
    cout << "After reserve(10) capacity chnged to: " << m_vector.capacity() <<endl; 


    return 0; 
}