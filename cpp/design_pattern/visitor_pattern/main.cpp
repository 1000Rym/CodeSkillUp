// This code is made for learning design pattern
// Visitor pattern. 
// Case: There is a shopping mall classify there customer to bronze, silver, gold.
// and giving them different benificial by each custormer level.  

#include <iostream>

using namespace std; 

class BronzeCustomer;
class SilverCustomer;
class GoldCustomer;

class Visitor{
    public : 
        virtual void visit(BronzeCustomer *e)  = 0;
        virtual void visit(SilverCustomer *e)  = 0;
        virtual void visit(GoldCustomer *e) =0;
};

class Customer{
    protected:
        string name;
    public:
        Customer(string name){
            this->name = name;
        } 
        virtual void accept(class Visitor &v) = 0; // pure virtual fucntion. 
};

class BronzeCustomer : public Customer{
    public:
        BronzeCustomer(string name) : Customer(name){} 
        string bronzeCustomer(){
            return "Bronze Customer:" +name + " got ";
        }
        
        void accept(Visitor &v)  {
            v.visit(this);
        }
};

class SilverCustomer : public Customer{
    public: 
        SilverCustomer(string name) : Customer(name){} 
        string silverCustomer(){
            return "Silver Customer:" +name + " got ";
        }

        void accept(Visitor &v)  {
            v.visit(this);
        }

};

class GoldCustomer : public Customer{
    public:
        GoldCustomer(string name) : Customer(name){} 
        string goldCustomer(){
            return "Gold Customer:" +name + " got ";
        }

        void accept(Visitor &v)  {
            v.visit(this);
        }
};



class SeasonSaleCoupon: public Visitor{
    public: 
        void visit (BronzeCustomer *e) {
            cout << e->bronzeCustomer()<< "10 % season sale coupon" << endl;
        }

        void visit (SilverCustomer *e) {
            cout << e->silverCustomer()<<"20 % season sale coupon" << endl;
        }

        void visit (GoldCustomer *e) {
            cout << e->goldCustomer()<<"30 % season sale coupon" << endl;
        }
};

class MonthlySaleCoupon: public Visitor{
    void visit (BronzeCustomer *e) {
        cout << e->bronzeCustomer() << "1 dollar coupon" << endl;
    }

    void visit (SilverCustomer *e) {
        cout << e->silverCustomer()<< "3 dollar coupon" << endl;
    }

     void visit (GoldCustomer *e) {
       cout << e->goldCustomer() << "5 dollar coupon" << endl;
    }
};

int main(){
    cout<< "Welcome to coupong shoping mall" <<endl; 

    Customer *userList[] = {
        new BronzeCustomer("Tim"),
        new BronzeCustomer("Mike"),
        new BronzeCustomer("March"),
        new SilverCustomer("Jelly"),
        new SilverCustomer("Forest"),
        new GoldCustomer("Teng")
    };

    SeasonSaleCoupon seasonCoupon;
    MonthlySaleCoupon monthCoupon; 
    
    //Bronze Customer:Mike got 10 % season sale coupon
    //Bronze Customer:Mike got 1 dollar coupon
    //Bronze Customer:March got 10 % season sale coupon
    //Bronze Customer:March got 1 dollar coupon
    //Silver Customer:Jelly got 20 % season sale coupon
    //Silver Customer:Jelly got 3 dollar coupon
    //Silver Customer:Forest got 20 % season sale coupon
    //Silver Customer:Forest got 3 dollar coupon
    //Gold Customer:Teng got 30 % season sale coupon
    //Gold Customer:Teng got 5 dolar coupon

    for (int i = 0 ; i < 6; i++){
        userList[i]->accept(seasonCoupon);
        userList[i]->accept(monthCoupon);
    }

}