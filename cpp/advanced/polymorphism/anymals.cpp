//Author: Forest L. Qian
//Example Code2: Understanding how polymorphism works. 
//Date 2021. 01.15(Fri)

#include <iostream>
#include <vector>

using namespace std; 

//The class containing pure virtual function is an abstract class.
class Animal{
    protected: 
        string animal_type; 
    public:
        Animal(string animal_type):animal_type("animal"){
            this->animal_type = animal_type; 
        } 

    // add =0 after function to delcare this function is 
    // a pure virtual fucntion.
    virtual void move() = 0; 
};

// pure virtual function must be implemented in each class.
class Human : public Animal{
    public : 
        Human(string animal_type) : Animal(animal_type){};
        void move(){
            cout << this->animal_type << " is running. " << endl; 
        }
};

class Bird : public Animal{
    public : 
        Bird(string animal_type) : Animal(animal_type){};
        void move(){
            cout << this->animal_type << " is flying. " << endl; 
        }
};

class Snake : public Animal{
    public : 
        Snake(string animal_type) : Animal(animal_type){};
        void move(){
            cout << this->animal_type << " is crowling. " << endl; 
        }
};


// To run this code g++ 11 extensions is required. 
int main(){
    Human human("human");
    Bird bird("bird");
    Snake snake("snake");

    vector<Animal*> animalList;
    animalList.push_back(&human);
    animalList.push_back(&bird);
    animalList.push_back(&snake);

    for (const auto& animal : animalList){
        animal->move();
    }
}