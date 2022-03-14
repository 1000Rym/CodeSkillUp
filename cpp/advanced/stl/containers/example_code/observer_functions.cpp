/*
    This code is made for leearning observer function.
    1. get_allocator
    2. hash_function
    3. key_eq 
    4. key_comp
    5. value_comp
*/
#include <vector>
#include <unordered_set>
#include <map>
#include <iostream>

using namespace std;

int main(){
    vector<int> m_vector;
    unordered_set<string> m_unordered_set;
    
    // 1. get_allocator: Get an (memory) allocator for the container.
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
    cout << endl;

    // Deallocate the memory.
    m_vector.get_allocator().deallocate(p, 5);
    
    // 2. hash_function: Get an hash function.
    auto m_hash = m_unordered_set.hash_function();
    cout << "that:" << m_hash("that")<<endl;
    cout << "that:" << m_hash("that")<<endl; 
    cout << "That:" << m_hash("THAT")<<endl;

    // 3. key_eq: Returns the key equivalence comparison(Checking for the two key is eqaul or not).
    // >i s_key_equal1 : 1
    // >i s_key_equal2 : 0
    bool is_key_equal1 = m_unordered_set.key_eq()("case", "case");
    bool is_key_equal2 = m_unordered_set.key_eq()("case", "Case");
    cout << "is_key_equal1:" << is_key_equal1 << endl;
    cout << "is_key_equal2:" << is_key_equal2 << endl;
    
   
    map <char, int>  m_map;
    int value = 0;
    for (char c = 'a'; c <='g'; c++)
    {
        m_map[c] = ++ value;
    }

    /* 4. key_comp : compare the key.
        > a:1
        > b:2
        > c:3
        > d:4
        > e:5
        > f:6
        > g:7
    */
    char last_key = m_map.rbegin()->first; // last value of the key.
    auto it = m_map.begin();
    auto key_comp = m_map.key_comp();
    do {
        cout << it->first << ":" << it->second << endl;
    }while( 
        key_comp((*it++).first, last_key)
    );

    /* 5. value_comp: compare the object value.
        > a:1
        > b:2
        > c:3
        > d:4
        > e:5
        > f:6
        > g:7
    */
    it = m_map.begin();
    do{
        cout << it->first << ":" << it->second << endl;
    }while(
        m_map.value_comp()(*it++, *m_map.rbegin()) // It dosent accept any parameter.
    );


}  