//This file is made for the learning
// read write generic algorithm
#include <iostream>
#include <vector>
#include <deque>
#include <string>
#include <algorithm> // To use transform. 

using namespace std;

// Insert function should be working with back_inserter or front inserter.
void testCopy(){
    int loopCount = 5;
    vector<int> intVector1;
    deque<int> intDeque2;

    for (int i = 1 ; i <= loopCount; i++) intVector1.push_back(i); //1~5
    for (int i = 11 ; i <= 11+loopCount; i++) intDeque2.push_back(i); //11~15

    // copy intVector2 to intVector1 from the back.
    copy(intDeque2.begin(), intDeque2.end(), back_inserter(intVector1));

    //1 2 3 4 5 11 12 13 14 15 16 
    for (auto iter = intVector1.begin(); iter!=intVector1.end(); iter++){
        cout << *iter << " "; 
    }
    cout << endl;

    // copy intVector1 (1 2 3 4 5 11 12 13 14 15 16 )
    // to infront of intDeque2 (11 12 13 14 15 16).
    copy(intVector1.begin(), intVector1.end(), front_inserter(intDeque2));

     //17 16 15 14 13 12 6 5 4 3 2 12 13 14 15 16 17 
    for (auto iter = intDeque2.begin(); iter!=intDeque2.end(); iter++){
        cout << *iter << " "; 
    }
    cout << endl;
}

void testSwap(){
    int loopCount = 5;
    vector<int> intVector1, intVector2;
    for (int i = 1 ; i <= loopCount; i++) intVector1.push_back(i); //1~5
    for (int i = 11 ; i <= 11+loopCount; i++) intVector2.push_back(i); //11~15

    //Vector1: 1 2 3 4 5 
    //Vector2: 11 12 13 14 15 16 
    
    cout << "Vector1: "; 
    for (auto iter = intVector1.begin(); iter!=intVector1.end(); iter++){
        cout << *iter << " "; 
    }
    cout << endl;

    cout << "Vector2: "; 
    for (auto iter = intVector2.begin(); iter!=intVector2.end(); iter++){
        cout << *iter << " "; 
    }
    cout << endl;

    swap(intVector2, intVector1);

    //After swap the vectors are changed to :
    //Vector1: 11 12 13 14 15 16 
    //Vector2: 1 2 3 4 5 
    cout << "After swap the vectors are changed to :" << endl;
    cout << "Vector1: "; 
    for (auto iter = intVector1.begin(); iter!=intVector1.end(); iter++){
        cout << *iter << " "; 
    }
    cout << endl;

    cout << "Vector2: "; 
    for (auto iter = intVector2.begin(); iter!=intVector2.end(); iter++){
        cout << *iter << " "; 
    }
    cout << endl;
}

void testFill(){
    vector<int> vectInt (10); //Let's make size 10 vect.
    // 1 1 1 0 0 0 0 0 0 0 
    fill(vectInt.begin(), vectInt.begin()+3, 1); 
    for (auto iter = vectInt.begin(); iter!=vectInt.end(); iter++){
        cout << *iter << " "; 
    }
    cout << endl;

    //1 1 1 2 2 2 2 2 2 2 
    fill(vectInt.begin()+3, vectInt.end(), 2);
    for (auto iter = vectInt.begin(); iter!=vectInt.end(); iter++){
        cout << *iter << " "; 
    }
    cout << endl;
}

void testTransform(){
    vector<int> vectInt = {1,2,3,4,5};
    string text = "Hello my name is forest!";

    transform(vectInt.begin(), vectInt.end(), vectInt.begin(), 
    [](int value)-> int {
        return value+10;
    });

    //11 12 13 14 15
    for(auto iter = vectInt.begin(); iter!=vectInt.end(); iter++ ){
        cout << *iter << " ";
    }
    cout <<endl;
    
    //HELLO MY NAME IS FOREST!
    transform(text.begin(), text.end(), text.begin(), ::toupper);
    cout<<text<<endl;
}

int main(){
    cout << "Read Write"<<endl;
    //testCopy();
    //testSwap();
    //testTransform();
    testFill();
} 