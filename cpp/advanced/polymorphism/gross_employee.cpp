//Author: Forest L. Qian
//Example Code1: Understanding how polymorphism works. 
//Date 2021. 01.15(Fri)

#include <iostream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

//base class 
class Employee {
    private: 
        string name; 

    //pay should be protected, since this value might be changed in derrived class.
    protected:
        double pay; 
    
    public : 
        Employee () {
            this->name = ""; 
            this->pay = 0;
        }

        Employee(string empName, double empPay){
            this->name = empName; 
            this->pay = empPay; 
        }

        void setName(string empName){
            this->name  = empName;
        }

        string getName(){
            return name; 
        }

        void setPay(double empPay){
            this->pay = empPay;
        }

        virtual double getGrossPay(int hour){
            return pay * hour;
        }
};


//derived class.
class Manager : public Employee{
    public :
        Manager(string empName,double empPay) : Employee(empName, empPay) {}
        double getGrossPay(int hour){
            return this->pay; 
        }
};



int main ()
{
    Employee emp1("Worker", 50);
    Manager man1("Manager", 1000);
    cout<< emp1.getName() << "," << emp1.getGrossPay(10) <<endl; 
    cout<< man1.getName() << "," << man1.getGrossPay(10) <<endl; 

    vector <Employee*> empList;
    empList.push_back(&emp1);
    empList.push_back(&man1);

    for (int i = 0 ; i<empList.size(); i++) {
        cout<< empList[i]->getName() << "," << empList[i]->getGrossPay(10) <<endl; 
    }  

}