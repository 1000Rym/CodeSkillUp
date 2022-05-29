#include <iostream>

using std::cout;
using std::endl;
using std::string;

/*
    Normal Employee class.
*/
class Employee{ 
    protected:
        string name_;
        int rank_;

        virtual int calc_salery(){
            return 3000 + rank_ * 500;
        }


    public:
        Employee() = default;
        Employee(string name, int rank):name_(name), rank_(rank){}
        
        void print_info(){
           cout << "user name: " << name_ 
           << ", salary: " << calc_salery() << endl;  
        }

        // To avoid memory leack add virtual on deconstructor function.
        virtual ~Employee(){
            cout << "Employee is released" <<endl;
        }

};

/*
    The manager will get 2000 more than employes.
*/
class Manager : public Employee{
    protected: 
        int calc_salery(){
            return 5000 + rank_* 500;
        }

    public: 
        Manager(string name, int rank) : Employee(name, rank){}
        ~Manager(){
            cout << "Manager is released." <<endl;
        }
};

/*
    The class which handles multiple employees.
*/
class EmployeeList{
    private: 
        Employee** employees_;
        int max_num_;
        int current_count_;
        
        bool is_member_full(){
            return current_count_ >= max_num_;
        }

    public:
        /*
            Make an employee list.
        */ 
        EmployeeList(int alloc_nums){
            employees_ = new Employee* [alloc_nums];
            current_count_ = 0;
            max_num_ = alloc_nums;
        }

        /*
            Add an employee.
        */
        void add_employee(Employee* employee){
            if (!is_member_full()){
                employees_[current_count_] = employee;
                current_count_ ++;
            }
        }

        /*
            Add a manager.
        */
        void add_manager(Manager* manager){
            if (!is_member_full()){
                employees_[current_count_] = manager;
                current_count_ ++;
            }
        }

        void print_members(){
            for (int i = 0; i < current_count_ ; i ++){
                employees_[i]->print_info();
            }
        }

        ~EmployeeList(){
            delete[] employees_;
            current_count_ = 0;
        }
};

int main(){
    EmployeeList emp_list(10);
    Employee* woody = new Employee("Woody", 20);
    Manager* ben = new Manager("Ben", 20);

    // add multiple members
    emp_list.add_manager(ben);
    emp_list.add_employee(woody);
    emp_list.print_members();
    
    // Since we add virtual in front of base deconstructor function,
    // base class is also called when it start release.
    // > Manager is released.
    // > Employee is released
    delete ben;
}