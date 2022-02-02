// Description: Example code for the c++ oop abstraction

#include <iostream>
using namespace std;

class ImplementAbstraction{
    private:
        int member_var1, member_var2;
    
    public:
        void setData(int var1, int var2)
        {
            this->member_var1 = var1; 
            this->member_var2 = var2;
        }
        void printData(){
            cout<< "This class have member variables "
                << member_var1 << "," << member_var2
                << endl;
        }
};

int main(){
    ImplementAbstraction instance; 
    instance.setData(10, 20);
    instance.printData();
    return 0;
}