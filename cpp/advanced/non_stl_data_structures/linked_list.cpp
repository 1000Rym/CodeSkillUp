#include "linked_list.h"

LinkedList::LinkedList(){
    headptr = nullptr;
}

void LinkedList::insertData(string data){
    if(headptr == nullptr) {
        headptr = new Node(data);
    }else{
        insertData(headptr, data);
    }
}

void LinkedList::insertData(Node* node, string data){
    if(node->next == nullptr){
        node->next = new Node(data);
    }else{
        insertData(node->next, data);
    }
}

bool LinkedList::searchData(Node* node, string data){
    if(node == nullptr) return false;
    else {
        if(node->data == data) {
            return true;
        }else {
            return searchData(node->next, data);
        }
    }
}

bool LinkedList::searchData(string data){
    if(headptr == nullptr) return false;
    else{
        if(headptr->data == data){
            return true;
        }else {
            return searchData(headptr->next, data);
        }
    }
}

bool LinkedList::removeData(string data){
    Node* node; 
    node = headptr;
    Node* deleteNode;
    
    if(headptr->data == data){
        deleteNode = headptr; 
        if(node->next != nullptr) {
            headptr = node->next; 
        }
        delete deleteNode;
        return true; 
    }

    while(node->next != nullptr){
        if(node->next->data == data){
            deleteNode = node->next;  
            node->next = node->next->next;
            delete deleteNode;
            return true; 
        }else{
            node = node->next;
        }
    }
    return false;
}

void LinkedList::listData(){
    Node* node;
    node = headptr;
    while(node != nullptr) {
        cout << node->data << " ";
        node = node->next; 
    }
    cout <<endl;
}


int main(){
    cout << "Linked list test." <<endl;
    LinkedList linked_list;
    linked_list.insertData("apple");
    linked_list.insertData("pie");
    linked_list.insertData("is");
    linked_list.insertData("very");
    linked_list.insertData("delicous!");
    cout<<linked_list.removeData("apple")<<endl; 
    cout<<linked_list.removeData("very")<<endl;  
    linked_list.listData();
}