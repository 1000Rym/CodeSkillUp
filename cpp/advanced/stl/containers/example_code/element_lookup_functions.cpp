/*
This code is made for learning operational functions in sequence containers.
1. find()
2. count()
3. eqaul_range()
4. lower_bound()
5. upper_bound()
*/
#include <iostream>
#include <set>
using namespace std; 

int main(){
    // initilizer list constructor.
    multiset<int> my_set = {10,20,30,20,20,50,60,70,80,100,45,55};
        
    // 1. find() : Get the iterator to the target element.
    // > it = my_set.find() *it= 20
    set<int>::iterator it = my_set.find(20);
    cout << "it = my_set.find(20) *it= " << *it << endl;

    // 2. count(): Count elements with the target value. 
    // > my_set.count(20): 1
    cout << "my_set.count(20): " << my_set.count(20) << endl;

    // 3. equal_range: Get the range of equal elements.
    // my_range.first: eqaul start , my_range.second: not equal.
    // > remained element my_set():10 30 45 50 55 60 70 80 100 
    auto my_range = my_set.equal_range(20);
    my_set.erase(my_range.first, my_range.second);
    cout << "remained element my_set():";
    for(auto element : my_set){
        cout << element << " ";
    }
    cout << endl;
    
    // 4. lower_bound(): Return iterator to lower bound.
    // 5. uppper_bound: Return iterator to upper bound.
    // > remained element my_set():10 30 45 50 100 
    auto upper_it = my_set.upper_bound(80);
    auto lower_it = my_set.lower_bound(55);
    my_set.erase(lower_it, upper_it);
    cout << "remained element my_set():";
    for(auto element : my_set){
        cout << element << " ";
    }
    cout << endl;
}