#include <iostream>
#include <list>

using namespace std;

template <typename T> 
void print_container_elements(string_view description, const T  &container){
    cout << description;
    for(auto element : container){
        cout << element << " ";
    }
    cout << endl;
}

int main()
{
    list <int> m_list1, m_list2;

    // insert elements(1~10) to the list.
    for (int i = 1; i <= 10; i++)
    {
        m_list1.emplace_back(i);
        m_list1.emplace_back(i);
    }
    
    // 1. splice(): Transfer elements from one list to another. 
    // > m_list2.splice(m_list1), m_list1: 
    // > m_list2.splice(m_list1), m_list2: 1 1 2 2 3 3 4 4 5 5 6 6 7 7 8 8 9 9 10 10  
    m_list2.splice(m_list2.begin(), m_list1);
    print_container_elements("m_list2.splice(m_list1), m_list1: ", m_list1);
    print_container_elements("m_list2.splice(m_list1), m_list2: ", m_list2);

    // 2. remove(): Remove target element(s) if exist.
    // > m_list2.remove(10): 1 1 2 2 3 3 4 4 5 5 6 6 7 7 8 8 9 9  
    m_list2.remove(10);
    print_container_elements("m_list2.remove(10): ", m_list2);

    // 3. remove_if(): Remove elements that fit the condition.
    // > m_list2.remove_if(is_even): 1 1 3 3 5 5 7 7 9 9 
    m_list2.remove_if([](int number){return number %2 == 0;}); // lambda's data type: function<bool(int)>
    print_container_elements("m_list2.remove_if(is_even): ", m_list2);

    // 4. unique(): Remove duplicate values.
    // > list2.unique(): 1 3 5 7 9 
    m_list2.unique();
    print_container_elements("m_list2.unique(): ", m_list2);

    // 5. sort(): Sort the list (default:incresing order). 
    // > m_list2.sort([](int num1, int num2){return num1 > num2;}): 9 7 5 3 1 
    m_list2.sort([](int num1, int num2){return num1 > num2;}); // or use the std::greater<int>()
    print_container_elements("m_list2.sort([](int num1, int num2){return num1 > num2;}): ", m_list2);
    
    // 6. reverse(): Reverse the container.
    // > m_list2.reverse(): 1 3 5 7 9  
    m_list2.reverse();
    print_container_elements("m_list2.reverse(): ", m_list2);

}