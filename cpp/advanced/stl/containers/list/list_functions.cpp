// This code file is made for learning list functions.
#include <list>
#include <iostream>
using namespace std;

void display_list(const list<int> &iter){
    // points at the iterators begin and end()
    for (auto it = iter.begin();  it != iter.end(); it ++){
        cout << *it << " ";
    }
    cout << endl;
}

void cdisply_list(list<int> &iter){
    // constant pointing the iteratror's begin and end.
    for(auto it = iter.cbegin(); it != iter.cend(); it ++){
        cout << *it << " ";
    }
    cout <<endl;
}

void crdisplay_list(list<int> &iter){
    // constant pointing the iterator's rbegin and rend
    for (auto it = iter.crbegin(); it != iter.crend(); it++){
        cout << *it << " ";
    }
    cout << endl;
}


void rdisplay_list(const list<int> &iter){
    // reversely display iterators.
    // points at iterators reverse begin to reverse end()
    for (auto it = iter.rbegin(); it != iter.rend(); it ++){
        cout << *it << " ";
    }
    cout << endl;
}

void insert_var_to_posotion(list <int> & iterator, int var, int position){
    auto it = iterator.begin();
    for (int i =0 ; i < position; i ++)
    {
        it ++; 
    }
    iterator.insert(it,var);
    
}

bool is_prime(const int& value){
    if (value %2 == 0){
        return true;
    }else{
        return false;
    }
}

template <typename T> void insert_vars_to_posotion(list <int> & iterator, list<T> vars, int position){
    auto it = iterator.begin();
    for (int i = 0; i < position; i ++)
    {
        it ++;
    }
    //insert iterators range.
    iterator.insert(it, vars.begin(), vars.end());
}

// use erase() function to delete list from target index from ... to 
void erase_list_by_index_range(list <int>& iterator, int from_index, int to_index){
    
    // check the list size is whether out of range
    if (from_index < 0 || from_index >= iterator.size()){
        return ;
    }
    if(to_index <0 || to_index >= iterator.size()){
        return ;
    }

    auto from = iterator.begin();
    for (int index = 0 ; index < from_index ; index ++){
        from ++;
    }

    auto to = iterator.begin();
    for (int index = 0; index < to_index; index ++){
        to ++;
    }

    iterator.erase(from, to);
}

void emplace_to_position(list<int> &iterator, int position, int value){
    auto it = iterator.begin();
    for(int index =0; index < position; index ++){
        it ++;
    }

    iterator.emplace(it, value);
}

bool isEven(const int& value){
    if (value % 2 == 0){
        return true;
    }else{
        return false;
    }
}

int main(){
    list<int> my_list;

    for (int i = 1; i <= 10; i ++){
        my_list.push_back(i);
    }
    
    // front, back
    cout << "myList.front():" << my_list.front() << endl;
    cout << "myList.back():" << my_list.back() << endl;

    // push_front(var), pop_front(var)  
    my_list.push_front(11);
    my_list.push_back(21);
    cout << "after push_front(11) and push_back(21): ";
    display_list(my_list);

    my_list.pop_back();
    my_list.pop_front();
    cout << "after pop_front() and pop_back(): ";
    display_list(my_list);
    cout << "const display: "; 
    cdisply_list(my_list);

    cout << "reverse display: ";
    rdisplay_list(my_list);
    cout << "const revse display: ";
    crdisplay_list(my_list);

    insert_var_to_posotion(my_list, 15, 6);
    cout << "after insert 15 to position 6 of the mylist : ";
    display_list(my_list);

    list<int> my_list1;
    my_list1.push_back(11);
    my_list1.push_back(22);
    insert_vars_to_posotion(my_list, my_list1, 2);
    cout << "insert list(11,22) to position 6 of the my_list : ";
    display_list(my_list);

    // enhance the erase function remove target range index.
    erase_list_by_index_range(my_list, 2, 5);
    cout << "erase() from index 2~5, my_list : ";
    display_list(my_list);

    // remove()
    my_list.remove(11);
    cout << "remove the element 11, my_list : ";
    display_list(my_list);
    
    // remove_if() the value is even
    my_list.remove_if(isEven);
    cout << "remove_if(isEven), my_list: ";
    display_list(my_list);

    // reverse()
    my_list.reverse();
    cout << "reverse() the list, my_list : ";
    display_list(my_list);
    
    // sort() 
    my_list.sort();
    cout << "sort(), my_list : ";
    display_list(my_list);

    // emplace_front(), emplace_back()
    my_list.emplace_front(10);
    my_list.emplace_back(20);
    cout << "emplace_front(10), emplace_back(20) my_list : ";
    display_list(my_list);

    // emplace() with specific position.
    emplace_to_position(my_list, 2, 22);
    cout << "emplace() 22 to 2nd position my_list : ";
    display_list(my_list);

    //merge() is using in sorted list.
    cout << "my_list1 : ";
    display_list(my_list1);
    my_list.sort();
    my_list1.merge(my_list);
    cout << "merge(sorted my_list), my_list1: ";
    display_list(my_list1);

    // splice(): splice(transfer) another list(all or range) to the list.
    list<int> temp_list = {10,20,30,40,50};
    my_list.emplace_front(1);
    my_list.emplace_front(2);
    my_list.emplace_front(3);
    my_list.splice(my_list.begin(), temp_list);
    cout << "splice(my_list's begin position temp_list {10,20,30,40,50}, my_list:";
    display_list(my_list);

    // clear() all the elements in the list.
    my_list.clear();
    my_list1.clear();    

    return 0;
}
