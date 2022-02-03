#include <iostream>
#include <string>
#include <vector>
using namespace std; 

class Employee
{
    private:
        string name;
    
    protected:
        double pay;
    
    public: 
        Employee():name(""), pay(0){}
        Employee(string name, double pay)
        {
            this -> name= name;
            this -> pay = pay;

            cout << "New employee is created" << endl;
        }

        virtual double getGrossPay(int hour)
        {
            return hour * pay;
        }
};

class Manager: public Employee
{
    public: 
        Manager():Employee(){}
        Manager(string name, double pay) : Employee(name, pay){
            cout << "New Manager is created " << endl;
        }
        double getGrossPay(int hour){
            return pay;
        }
};


int main(){
    Manager man("Mike", 550);
    Employee emp ("Jake", 20);


    vector<Employee*> emps;
    emps.push_back(&man);
    emps.push_back(&emp);

    for(auto empl : emps)
    {
        cout << empl->getGrossPay(30) <<endl;
    }

    return 0;
}