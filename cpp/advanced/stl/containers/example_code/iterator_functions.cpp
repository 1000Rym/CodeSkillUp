#include <iostream>
#include <vector>
#include <forward_list>

using namespace std;

int main(){
    
    // Push the elements 1~10 to vector.
    vector<int> m_vector;
    for(int i = 1; i <=10 ; i ++){
        // Rather to use emplace_back, since it dosen't create template object memory.
        m_vector.emplace_back(i);
    }

    // 1. begin() / end() : Returns an iterator pointing to the first/last element.
    for(auto itor = m_vector.begin(); itor !=  m_vector.end(); itor ++){ //: last pointer of the iterator.
        
        cout << ++(*itor) << " ";
    }
    cout << endl;

    // 2. cbegin() / cend() : Returns a constant iterator pointing to the first/last element.
    for(auto itor = m_vector.cbegin(); itor !=  m_vector.cend(); itor ++){ //: last pointer of the iterator.
        
        cout << *itor << " ";
    }
    cout << endl;

    // 3. rbegin(), rend(): Returns an reverse iterator pointing to the last/first element.
    for(auto itor= m_vector.rbegin(); itor != m_vector.rend(); itor ++){
        cout << (*itor)-- << " ";
    }
    cout << endl;

    // 4. crbegin(), crend(): Returns a revsered constant iterator poing to the last/first element.
    for(auto itor= m_vector.crbegin(); itor != m_vector.crend(); itor ++){
        cout << *itor << " ";
    }
    cout << endl;

    // 5. before_begin(), cbefore_begin(): Return the (const)iterator to before beginning.
    forward_list<int> m_forward_list = {1,2,3,4,5};
    // > 0 1 2 3 4 5 
    m_forward_list.insert_after(m_forward_list.before_begin(), 0); // Insert the value after the before begin iterator. 
    for(auto itor = m_forward_list.begin(); itor !=  m_forward_list.end(); itor ++){ 
        
        cout << (*itor) ++ << " ";
    }
    cout << endl;

}