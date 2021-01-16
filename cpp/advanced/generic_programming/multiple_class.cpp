//Author: Forest.1000
//Date: 2021.01.16
//This file is made for practice generic programming
//multiple template class
#include <iostream>
#include <vector>

using namespace std;
template <class T, class U>
class Company{
    private: 
        vector<T> nameVector; 
        vector<U> ageVector;  
    public: 
        void insert(T name, U age){
            nameVector.push_back(name);
            ageVector.push_back(age);
        } 

        void displayInfo(int countOfPerson){
            cout << "[Info]"<< nameVector[countOfPerson]<<":"<<ageVector[countOfPerson]<<endl; 
        }
};

int main(){
    Company<string, int> company;
    company.insert("maggie",33);
    company.insert("forest",32);
    company.insert("maria",28);
    company.insert("carl",48);
    company.displayInfo(1);
}