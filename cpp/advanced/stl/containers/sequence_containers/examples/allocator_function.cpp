#include <vector>
#include <iostream>
#include <forward_list>


using namespace std;

int main(){
    vector<int> m_vector;

    // use allocator allocate 5 int size memory allocation.
    int* p = m_vector.get_allocator().allocate(5);

    // use constructor to construct value.
    for (int i = 0; i < 5; i++){
        m_vector.get_allocator().construct(&p[i], i);
    }

    // print out the assigned values.
    for (int i = 0; i < 5; i ++){
        cout << p[i] << " ";
    }
    // deallocate the memory.
    m_vector.get_allocator().deallocate(p, 5);
}  