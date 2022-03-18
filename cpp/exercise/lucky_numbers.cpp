/* Guessing Lucky Numbers */
#include <iostream>
#include <random>

using std::cout;
using std::cin;
using std::endl;

int main(){
    // Generate Random Device.
    std::random_device rd;
    // Generate random device generator .
    std::mt19937 gen(rd());
    
    // Use uniform int distribution.
    std::uniform_int_distribution<int> dis(0,99);

    int generated_number = dis(gen);
    int user_input;

    while (true){
        cout<<"Please input your number:";
        cin>>user_input;

        if (user_input == generated_number){
            cout << "Congratulations!" << endl;
            break;
        }else if(user_input < generated_number){
            cout << "Small number!" << std:: endl;    
        }else{
            cout << "Large number!" << std:: endl;
        }
    }

}