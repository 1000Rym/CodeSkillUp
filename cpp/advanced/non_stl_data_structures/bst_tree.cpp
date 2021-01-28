#include <string>
#include "bst_tree.h"

BST::BST(){
    this->root = nullptr;
}

void BST::insertNode(string data){
    if (root == nullptr) {
        root = new Node(data);
    }else{
        insertNode(root, data);
    }
}

void BST::insertNode(Node *node, string data){
    if(node->data > data){
        if (node->left == nullptr) node->left = new Node(data);
        else insertNode (node->left, data);
    }else{
        if(node->right == nullptr) node->right = new Node(data);
        else insertNode(node->right, data);
    }
}

bool BST::searchNode(Node *node, string data){
    if(node-> data == data) return true;
    else if(node->data > data) {
        if(node->left == nullptr) return false;
        else return searchNode(node->left, data); 
    } else {
        if(node->right == nullptr) return false;
        else return searchNode(node->right, data);
    }
}

bool BST::searchNode(string data){
    if(root == nullptr) return false;
    else return searchNode (root, data);
}

void BST::printPreOrder(Node* node){
    if(node->left != nullptr) printPreOrder(node->left);
    cout<<node->data<<" "; 
    if(node->right != nullptr) printPreOrder(node->right);
}

void BST::printPreOrder(){
    if(root != nullptr) printPreOrder(root);
    cout<<endl;
}

void BST::printReverseOrder(Node* node){
    if(node->right != nullptr) printReverseOrder(node->right);
    cout<<node->data<<" "; 
    if(node->left != nullptr) printReverseOrder(node->left);
}


void BST::printReverseOrder(){
    if(root != nullptr) printReverseOrder(root);
    cout <<endl;
}

int main(){
    cout << "Testing BST"<<endl; 
    BST bst = BST();

    bst.insertNode("zoo");
    bst.insertNode("car");
    bst.insertNode("ear");
    bst.insertNode("aid");
    bst.insertNode("dog");

    bst.printPreOrder();
    bst.printReverseOrder();

    cout << bst.searchNode("zoo")<<endl;
    cout << bst.searchNode("toy")<<endl;
}