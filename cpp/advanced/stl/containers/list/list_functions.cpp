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

template <typename T> void insert_vars_to_posotion(list <int> & iterator, list<T> vars, int position){
    auto it = iterator.begin();
    for (int i = 0; i < position; i ++)
    {
        it ++;
    }
    //insert iterators range.
    iterator.insert(it, vars.begin(), vars.end());
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
    cout << "after push_front(11) and push_back(21):";
    display_list(my_list);

    my_list.pop_back();
    my_list.pop_front();
    cout << "after pop_front() and pop_back():";
    display_list(my_list);
    cout << "const display:"; 
    cdisply_list(my_list);

    cout << "reverse display:";
    rdisplay_list(my_list);
    cout << "const revse display:";
    crdisplay_list(my_list);

    insert_var_to_posotion(my_list, 15, 6);
    cout << "after insert 15 to position 6 of the mylist :";
    display_list(my_list);

    list<int> my_list1;
    my_list1.push_back(11);
    my_list1.push_back(22);
    insert_vars_to_posotion(my_list, my_list1, 2);
    cout << "after insert list(11,22) to position 6 of the mylist :";
    display_list(my_list);

    return 0;
}
