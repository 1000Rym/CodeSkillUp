#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector <int> m_vector1, m_vector2;
    
    // assign(): fill
    // assign usecase1: assign n, values.
    m_vector1.assign(10, 100);
    for (const auto value : m_vector1){
        cout << value << " ";
    }
    cout << endl;

    // assign(): range
    // assign usecase2: assign from iterators range
    m_vector2.assign(m_vector1.begin()+1, m_vector1.end()-1);
    for (const auto value : m_vector2){
        cout << value << " ";
    }
    cout << endl;
    
    //push_back, pop_back
    for (int i = 1; i <=5; i ++){
        m_vector2.push_back(i * 10);
    }
    while (!m_vector2.empty())
    {
        cout << m_vector2[m_vector2.size()-1] << " ";
        m_vector2.pop_back();
    }
    cout << endl;

    // Insert 10 at the second position
    m_vector1.insert(m_vector1.begin()+1, 10);
    for (const auto value: m_vector1){
        cout << value << " ";
    }
    cout << endl;

    // Erase the thrid to last item.
    m_vector1.erase(m_vector1.begin()+2, m_vector1.end());
    for (const auto value: m_vector1){
        cout << value << " ";
    }
    cout << endl;

    
    // emplace, emplace_back, swap.
    m_vector2.emplace_back(30);
    m_vector2.emplace(m_vector2.begin()+1, 20);
    m_vector1.swap(m_vector2);

    cout << "vector1:";
    for (const auto val : m_vector1){
        cout << val << " ";
    }
    cout << endl;

    cout << "vector2:";
    for (const auto val : m_vector2){
        cout << val << " ";
    }
    cout << endl;

    //clear the vector
    m_vector1.clear();
    m_vector2.clear();

    cout <<"after clear vector size change to " << m_vector1.size() << endl;

}
