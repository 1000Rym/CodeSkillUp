#include <iostream>
#include <vector>

using namespace std;

int main(){
    vector<int> m_vector; 
    
    for (int i = 1; i <= 10 ; i ++){
        m_vector.emplace_back(i*10);
    }
    
    cout << "m_vector[2]:" << m_vector[2] << endl;
    cout << "m_vector.at(2):" << m_vector.at(2) << endl;
    cout << "m_vector.front():" << m_vector.front() << endl;
    cout << "m_vector.back():" << m_vector.back() << endl;
    cout << "*m_vector.data():"<< *m_vector.data() << endl;


    return 0;
}