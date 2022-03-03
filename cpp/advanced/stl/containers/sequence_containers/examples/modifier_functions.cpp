#include <iostream>
#include <array>
#include <vector>
#include <deque>

using namespace std;

template <typename T> void print_container_elements(string_view descripion,T const & elements){
    // Print the container elements with description.
    cout << descripion;
    for(auto value : elements){
        cout << value << " ";
    }
    cout << endl;
}

int main()
{
    array<int, 5> m_array1, m_array2; 
    vector <int> m_vector1, m_vector2;
    deque<int> m_deque;

    // 1. fill(): Fill the container with specific value.
    // > fill(1) m_array1: 1 1 1 1 1 
    // > fill(2) m_array2: 2 2 2 2 2 
    m_array1.fill(1);
    m_array2.fill(2);
    print_container_elements("fill(1) m_array1: ", m_array1);
    print_container_elements("fill(2) m_array2: ", m_array2);

    // 2. swap(): Swap to another list of same type and size.
    // > fill(1) m_array1: 1 1 1 1 1 
    // > fill(2) m_array2: 2 2 2 2 2 
    m_array1.swap(m_array2);
    print_container_elements("m_array1.swap(m_array2) m_array1: ", m_array1);
    print_container_elements("m_array1.swap(m_array2) m_array2: ", m_array2);
    

    // 3.1 assign() :  Assign the container content(Fill). 
    // > m_vector1.assign(10, 100) m_vector1: 100 100 100 100 100 100 100 100 100 100   
    m_vector1.assign(10, 100);
    print_container_elements("m_vector1.assign(10, 100) m_vector1: ", m_vector1);

    // 3.2 assign() : Assign the container by range.
    // > m_vector2.assign(m_array1.begin()+1, m_array1.end()-1):2 2 2 
    m_vector2.assign(m_array1.begin()+1, m_array1.end()-1);
    print_container_elements("m_vector2.assign(m_array1.begin()+1, m_array1.end()-1):", m_vector2);

    
    // 4. push_back(): Push element into a vector from back.
    // > m_vector2.push_back(100): 2 2 2 100
    m_vector2.push_back(100);
    print_container_elements("m_vector2.push_back(100): ", m_vector2);
    
    // 5. pop_back(): Pop last element from the container(void). 
    // > m_vector2.pop_back(): 2 2 2 
    m_vector2.pop_back();
    print_container_elements("m_vector2.pop_back(): ", m_vector2);

    // 6. emplace_back(): Insert a new element into the back of the container(Not create temporary object implicitly). 
    // > m_vector2.emplace_back(200): 
    m_vector2.emplace_back(200);
    print_container_elements("m_vector2.emplace_back(200): ", m_vector2);

    // 7. emplace(): Insert a new element at specific position(Not create temporary object implicitly).
    // > m_vector2.emplace(m_vector2.begin()+2, 20): 2 2 20 2 200 
    m_vector2.emplace(m_vector2.begin()+2, 20);
    print_container_elements("m_vector2.emplace(m_vector2.begin()+2, 20): ", m_vector2);
    

    // 8. insert(): Insert a new element at specific position. 
    // > m_vector2.insert(m_vector2.begin()+3, 30): 2 2 20 30 2 200 
    m_vector2.insert(m_vector2.begin()+3, 30);
    print_container_elements("m_vector2.insert(m_vector2.begin()+3, 30): ", m_vector2);


    // 9.1 erase(): Remove element from a container from specified poistion.
    // > m_vector2.erase(m_vector2.end()-1)): 2 2 20 30 2 
    m_vector2.erase(m_vector2.end()-1);
    print_container_elements("m_vector2.erase(m_vector2.end()-1)): ", m_vector2);

    // 9.2 erase(): Remove elements from a container from specified range[begin, end).
    // > m_vector2.erase(m_vector2.begin()+2, m_vector2.begin()+4): 2 2 2 
    m_vector2.erase(m_vector2.begin()+2, m_vector2.begin()+4);
    print_container_elements("m_vector2.erase(m_vector2.begin()+2, m_vector2.begin()+4): ", m_vector2);

    //10. clear(): Remove all elements from the container 
    // > m_vector2.clear() size():0
    m_vector2.clear();
    cout << "m_vector2.clear() m_vector2.size():" << m_vector2.size() << endl;

    //11. push_front():  Push the new element to the first position.
    // > m_deque:{2,1}, m_deque.push_front(3): 3 1 2 
    m_deque.push_back(1);
    m_deque.push_back(2);
    m_deque.push_front(3);
    print_container_elements("m_deque:{2,1}, m_deque.push_front(3): ", m_deque);
    
    // 12. pop_front() : Remove the first element and reduces size of the container. 
    // > m_deque.pop_front(): 1 2 
    m_deque.pop_front();
    print_container_elements("m_deque.pop_front(): ", m_deque);

    // 13. emplace_front(): Insert a new element into the front of the container(Not create temporary object implicitly).
    // > deque.pop_front(3): 3 1 2 
    m_deque.emplace_front(3);
    print_container_elements("m_deque.pop_front(3): ", m_deque);
}
