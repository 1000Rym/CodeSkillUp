#include <iostream>

using namespace std; 

struct Node{
     public: 
        string data;
        Node* left; 
        Node* right;
        Node(string data){
            this->data = data;
            this->left = nullptr;
            this->right = nullptr; 
        }  
};

class BST{
    private :
        Node* root;
        void insertNode(Node* node, string data);
        bool searchNode(Node* node, string data);
        bool deleteNode(Node* node, string data);
        void printPreOrder(Node *node);
        void printReverseOrder(Node *node);
    public :
        BST();
        void insertNode(string data);
        bool searchNode(string data);
        bool deleteNode(string data);
        void printPreOrder();
        void printReverseOrder();
};