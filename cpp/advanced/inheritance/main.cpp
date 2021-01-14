//Author: Forest L. Qian
//Understanding how inheritance works. 
//Date 2021. 01.14(Thu)

#include <iostream>
#include <string>
#include <sstream>

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

        double getPay(){
            return pay;
        }

        string toString(){
            stringstream stm; 
            stm << this->name << ":" << this->pay;
            return stm.str(); 
        }
};


//derived class.
class Manager : public Employee{
    private : 
        bool salaried;
        void setNoPayWhenNotSalaried(bool empSalaried, double empPay =0){
            this->pay = empSalaried ?  empPay : 0; 
        }

    public :
        Manager(string empName,double empPay,bool empSalaried) : Employee(empName, empPay) {
            this->salaried = empSalaried;
            setNoPayWhenNotSalaried(empSalaried,empPay); 
        }

        void setSalaried(bool empSalaried){
            this->salaried = empSalaried;
            setNoPayWhenNotSalaried(empSalaried);
        }

        bool getSalaried(){
            return this->salaried;
        } 
    
};

class SportsMan {
    private :
        string sports;
    public :
        SportsMan(string which_sports){
            this->sports = which_sports;
        }
        string exercise(){
            stringstream stm; 
            stm<< "Like to play " << this->sports;
            return stm.str();
        }
};

class SportsLikeManager : public Manager, public SportsMan{
    public : 
        SportsLikeManager(string empName, double empPay, bool empSalaried, string which_sports) : Manager(empName, empPay, empSalaried), SportsMan(which_sports){}
};


int main ()
{
    Employee emp1("Forest", 500);
    Employee emp2; 
    emp2.setName("wood"); 
    emp2.setPay(800);
    Manager emp3("Leader", 1000, true);
    SportsLikeManager emp4("CEO", 2000, false, "soccer");

    cout << "Emp1 Info: " << emp1.toString()<< endl;
    cout << "Emp2 Info: " << emp2.toString()<< endl;
    cout << "Emp3 Info: " << emp3.toString()<< endl;
    cout << "Emp4 Info: " << emp4.toString()<< endl; 
    cout << "Emp4 " <<emp4.exercise()<<endl;     
}