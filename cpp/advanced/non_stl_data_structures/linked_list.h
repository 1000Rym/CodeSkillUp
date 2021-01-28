#include <iostream>
using namespace std; 

struct Node{
    public: 
        string data;
        Node* next;
    Node(string data){
        this->data = data;
        Node* next = nullptr; 
    }
};

class LinkedList{
    private:
        Node* headptr;
        void insertData(Node* node, string data);
        bool searchData(Node* node, string data);
    public :
        LinkedList();
        void insertData(string data);
        bool searchData(string data);
        bool removeData(string data);
        void listData();
};
