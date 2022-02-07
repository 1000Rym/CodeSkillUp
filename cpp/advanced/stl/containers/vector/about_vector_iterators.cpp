#include <iostream>
#include <vector>

using namespace std;

int main(){
    // Instantiate an empty vector.
    vector<int> m_vector;
    
    for(int i = 1; i <=10 ; i ++){

        // Rather to use emplace_back, since it dosen't create template object memory.
        m_vector.emplace_back(i);
    }

    // begin() : start pointer of the iterator.
    for(auto itor = m_vector.begin(); itor !=  m_vector.end(); itor ++){ //: last pointer of the iterator.
        
        cout << ++(*itor) << " ";
    }
    cout << endl;

    // begin() : start pointer of the iterator.
    for(auto itor = m_vector.cbegin(); itor !=  m_vector.cend(); itor ++){ //: last pointer of the iterator.
        
        cout << *itor << " ";
    }
    cout << endl;

    //rbegin: reverse iterator ptrs last element.
    for(auto itor= m_vector.rbegin(); itor != m_vector.rend(); itor ++){
        cout << (*itor)-- << " ";
    }
    cout << endl;

    //crbegin: const reverse iterator, could not change the value iterator pointing at
    //crend: const reverse iterator ptrs last element.
    for(auto itor= m_vector.crbegin(); itor != m_vector.crend(); itor ++){
        cout << *itor << " ";
    }
    cout << endl;
    return 0;

}