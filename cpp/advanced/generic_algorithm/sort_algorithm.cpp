//Author: forest.1000
//Date: Jan.23th  2021
//This code is made for leanrning sort algorithm. 

#include <iostream>
#include <vector>
#include <algorithm>  //use sort algorithm.

using namespace std;

struct myAssending{
    bool operator() (int i, int j) { return i<j ; }
} assendingObject;

void printVector(vector<int> myIntVector){
    cout << "Sorted vector is now changed to :" << endl;
    for (auto iterator = myIntVector.begin(); iterator < myIntVector.end(); iterator ++){
        cout << *iterator <<" ";
    }
    cout <<endl;
}

void testStableSort(){
    vector <pair<int, int>> myPairVector;
    pair <int, int> p1 (1, 1);
    pair <int, int> p2 (1, 0);
    pair <int, int> p3 (2, 3);
    pair <int, int> p4 (2, 2);

    myPairVector.push_back(p1);
    myPairVector.push_back(p2);
    myPairVector.push_back(p3);
    myPairVector.push_back(p3);

    stable_sort (myPairVector.begin(), myPairVector.end(), 
    [](pair<int, int> first, pair<int, int> second)-> bool{
        if(first.first > second.first){
            return true; 
        }else if (first.first == second.first){
            return first.second > second.second; 
        }
        return false;
    });

    cout << "Sorted vector is now changed to :" << endl;
    for (auto iterator = myPairVector.begin(); iterator < myPairVector.end(); iterator ++){
        cout << iterator->first <<" "<< iterator->second << endl;
    }

}

int main(){
    cout<< "This class is made for learning sort."<<endl;
    vector<int> myIntVector = {12, 32, 11, 8, 9 , 16, 33, 21};
    int count  = 4; 
    //Case1 Partial: Sort Infront 4 vectors only.
    sort(myIntVector.begin(), myIntVector.begin()+count);  //Partial Sort
    printVector(myIntVector); //(8 11 12 32) 9 16 33 21

    //Case2 greater<type>: Desending sort by using greate
    sort(myIntVector.begin(), myIntVector.end(),greater<int>()); //33 32 21 16 12 11 9 8 
    printVector(myIntVector);

    //Case3 less<type>:  Ascending sort by using less (default)
    sort(myIntVector.begin(), myIntVector.end(),less<int>()); //8 9 11 12 16 21 32 33 
    printVector(myIntVector);

     //Case4 use function:  Dessending sort by using less (default)
    sort(myIntVector.begin(), myIntVector.end(),[](int first, int second)-> bool{
        return first>second;
    }); //33 32 21 16 12 11 9 8 
    printVector(myIntVector);

    // Case5 use objects operation():  ascending sort by using object. 
    sort(myIntVector.begin(), myIntVector.end(),assendingObject); //8 9 11 12 16 21 32 33 
    printVector(myIntVector);

    testStableSort();
}

