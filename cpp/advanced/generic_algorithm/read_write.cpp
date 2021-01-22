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

void testReplace(){
    //case 1: replace  origin_str’s pos to count  chars  to new_str.
    string str =  "Hello, I am Woody."; 
    string str2 = "forest.";
    int pos = 12, count = 6; 
    str.replace(pos, count, str2);
    cout<<str<<endl; // Hello, I am forest.

    //case 2: replace  origin_str’s first to last  to new_str.
    str =  "Hello, I am Woody."; 
    int first = 0, last = 6;
    str.replace(first, last, str2);
    cout<<str<<endl;  // forest. I am Woody.

    //case 3: replace  origin_str’s pos1 to count  chars  to new_str's pos2  count  chars.
    str =  "Hello, I am Woody."; 
    str2 = "forest.";
    int pos1 = 0,  count1 = 5, pos2 = 0, count2 = 6; 
    str.replace(pos1, count1, str2, pos2, count2); 
    cout <<str<<endl; //forest, I am Woody.

    //case 4:replace  str’s first to last  to first2 to last2.
    str =  "Hello, I am Woody."; 
    int first1 = 0, last1 = 6, first2 = 3, last2 = 5; 
    str.replace(first1, last1, first2, last2); 
    cout <<str<<endl; // I am Woody.

    //case 5:replace  str’s first to last  to first2 to last2.
    str =  "Hello, I am Woody."; 
    pos = 0, count = 6, count2 = 2; 
    str.replace(pos, count, "Mac", count2); 
    cout <<str<<endl; //Ma I am Woody.

    //case 6: replace  origin_str’s pos to count chars to cstr 's nullptr.
    str =  "Hello, I am Woody."; 
    pos = 0, count = 6; 
    str.replace(pos, count, "Mac"); 
    cout <<str<<endl; //Mac I am Woody.

    //case 7: replace  origin_str’s pos to count chars to count2 of ch.
    str =  "Hello, I am Woody."; 
    pos = 5, count = 1, count2 =3; 
    str.replace(pos, count, count2, '!'); 
    cout <<str<<endl; //Mac I am Woody.


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
    testReplace();
} 