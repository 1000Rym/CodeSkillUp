#include <iostream>
using namespace std; 

class Circle{
    // The variable can not be acccessed by out side.
    private:
        double radius; 
    
    public: 
        Circle(double radius);
        double getArea();
        
        // Initialze parameter when it is empty.
        Circle() : radius(0){};           
};

Circle::Circle(double radius){
    this->radius = radius;
}

double Circle::getArea(){
    return 3.14 * radius * radius;
}

int main(){
    Circle *circle = new Circle(2);
    cout << circle->getArea() << endl;
    return 0;
}