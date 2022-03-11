/*
    This code is made for practicing C++ Container Adapter: stack, queue, priority_queue's 
    member functions.
*/
# include <iostream>
# include <stack>
# include <queue>

using namespace std;

int main(){
    stack<int> my_stack;
    queue<int> my_queue, my_swapped_queue;
    priority_queue<int> my_priority_queue;
    
    for (int i = 1; i <= 10; i ++){
        // Insert the element in the top most position.    
        my_stack.push(i);
        my_stack.emplace(i+10);
        
        // Insert the element at first position.
        my_queue.push(i);
        my_queue.emplace(i+10);

        // Insert the element by descending order.
        my_priority_queue.push(i);
        my_priority_queue.emplace(i+10);
    }

    // 2. size(): show the current size of the stack.
    cout << "my_stack.size():" << my_stack.size() << endl;
    cout << "my_queue.size():" << my_queue.size() << endl;

    // 3. empty(): Return whether the stack is empty.
    while(!my_stack.empty()){ // my_stack {20,10, 19, 9... 11,1}  
        //4. my_stack.top(): Return the reference of the top most element. 
        cout << "my_stack.top(): " <<my_stack.top() << endl;
        //5. my_stack.pop(): Remove the top most element.
        my_stack.pop();
    }

    // my_queue {1, 11, 2, 12, 3, 13 ... 10, 20}
    while (!my_queue.empty()){
        //6. my_stack.front(): Return the reference of the first element. 
        cout << "my_queue.front(): " <<my_queue.front() << " ";
        //7. my_stack.back(): Return the reference of the last most element. 
        cout << "my_queue.back(): " << my_queue.back() << endl;
        // 7. my_queue.pop(): Remove the first element.
        my_queue.pop();
    }

    // my_priority_queue.top: { 20, 19 .... 1}
    while ( !my_priority_queue.empty() ){
        cout << "my_priority_queue.top: " << my_priority_queue.top() << endl;
        my_priority_queue.pop();
    }

    queue<int> my_queue1, my_queue2;
    
    for (int i = 1; i <= 100; i ++){
        my_queue1.emplace(i);
    }
    
    //swap(): exchange the swap the container.
    my_queue1.swap(my_queue2);
    cout << "my_queue1.size(): "<< my_queue1.size() << " ";
    cout << "my_queue2.size(): "<< my_queue2.size() << endl;
}