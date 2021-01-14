#include <iostream>

using namespace std; 
class Numbers{
    private:
        int number1, number2; 
   
    public:
        Numbers(int number1, int number2){
            this->number1 = number1;
            this->number2 = number2; 
        } 

        // Overload ++ when used as postfix
        void operator ++ (int){
            this->number1 ++;
            this->number2 ++; 
        }

        // Overload ++ when used as prefix
        void operator ++ (){
            ++ this->number1; 
            ++ this->number2; 
        }

        void displayNumbers(){
            cout << "Number1:" << this->number1 <<","<<this->number2<<endl;  
        }
};

int main(){
    Numbers numbers(1,2);
    numbers ++;
    numbers.displayNumbers();
    ++ numbers; 
    numbers.displayNumbers(); 
}
