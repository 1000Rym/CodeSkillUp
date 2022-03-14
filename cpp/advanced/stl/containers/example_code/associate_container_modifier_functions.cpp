/*
    This code is made for learning associate container's modifier functions. 
    The content of the features are following below:
    1. insert
    2. swap
    4. clear
    5. emplace
    6. emplace_hint
*/

#include <iostream>
#include <set>
#include <unordered_set>
using namespace std;

/*
Print the container elements with the description.
*/
template <typename T>
void print_container_elements(string_view description, T container){
    cout << description << ": {";
    for (auto element : container)
    {
        cout << " " <<element;
    }
    cout << " }" << endl;
}

int main(){
    set<int> my_set1, my_set2;

    // 1. insert: Insert the elements.
    // > my_set1: { 1 2 3 4 5 6 7 8 9 }
    for (int i = 1; i < 10; i ++){
        // 1.1 insert elements one by one.
        my_set1.insert(i);
    }
    
    // 1.2 Insert multi elements.
    // > my_set2: { 11 12 13 }
    int my_ints[] = {11,12,13,14};
    my_set2.insert(my_ints, my_ints+3);
    print_container_elements("my_set1", my_set1);
    print_container_elements("my_set2", my_set2);

    // 2. erase: Erase the elements.
    // 2.1 Erase a single element.  
    my_set1.erase(8);
    my_set1.erase(11); // Delete unexist element does envoke error.
    // >  my_set1: { 1 2 3 4 5 6 7 9 }
    print_container_elements("my_set1", my_set1); 

    // 2.2 Erase element by using iterator.
    auto it = my_set2.end();
    it--;
    my_set2.erase(it);
    // > my_set2: { 11 12 }
    print_container_elements("my_set2", my_set2); 

    // 2.4 Erase multiple elements.
    auto start = my_set1.find(5);
    auto last = my_set1.find(7);
    my_set1.erase(start, last);
    // my_set1: { 1 2 3 4 7 9 }
    print_container_elements("my_set1", my_set1);

    // 3. Swap the content of the container.
    // > my_set1: { 11 12 }
    // > my_set2: { 1 2 3 4 7 9 }
    my_set1.swap(my_set2);
    print_container_elements("my_set1", my_set1);
    print_container_elements("my_set2", my_set2);

    // 4. clear: Clear the content of the container.
    my_set1.clear(); 
    print_container_elements("my_set1", my_set1);

    // 5. emplace: Insert the element to the container. 
    // my_set2: { 1 2 3 4 7 9 100 }
    my_set2.emplace(1); // If the value is already exist, nothing happened to the container.
    my_set2.emplace(100);
    print_container_elements("my_set2", my_set2);

    /* 6. emplace_hint(position, args) :
        - position: Hint for the position where the element can be inserted.
        - args: The element which needs to be inserted.
    > my_set3: { 80 50 40 }
    */
    unordered_set<int> my_set3;     
    my_set3.emplace_hint(my_set3.cbegin(), 80); 
    my_set3.emplace_hint(my_set3.cend(), 50); 
    my_set3.emplace_hint(my_set3.cend(), 40); 
    print_container_elements("my_set3",my_set3);

}   