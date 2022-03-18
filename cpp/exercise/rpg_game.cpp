/*
    Coding exercise
    constructor, deconstructor, default constructor, copy constructor
*/

#include <iostream>
#include <string>

using std::cout;
using std::endl;

class Player{
    int hp;
    int coord_x, coord_y;
    bool is_alive;
    char* name;

    public: 
        // Player() = default; // default constructor. 
        Player(); 
        Player(const char* name); 
        ~Player();
 
        void set_hp(int hp);
        void be_attacked(int attacked_damage);
        void set_posision(int coord_x, int coord_y); 
        void show_status();
};

// initializer list
Player::Player() : hp(50), coord_x(0), coord_y(0), is_alive(true){ 
    this->name = new char[strlen("Unknown")+1];
    std::strcpy(this->name, "Unknown");
}

Player::Player(const char* name) : hp(50), coord_x(0), coord_y(0), is_alive(true){
    this->name = new char[strlen(name) +1];
    std::strcpy(this->name, name);
}

Player::Player(const char* name, int hp) : hp(hp), coord_x(0), coord_y(0), is_alive(true){
    this->name = new char[strlen(name) +1];
    std::strcpy(this->name, name);
}

Player::Player(const char* name, int hp, int coord_x, int coord_y) : hp(hp), coord_x(coord_x), coord_y(0), is_alive(true){
    this->name = new char[strlen(name) +1];
    std::strcpy(this->name, name);
}


Player::~Player(){
    cout << "Player " << this->name << " is Destroyed." << endl;
    if (name != NULL){
        delete[] this->name;
    }
}

void Player::set_hp(int hp){
    this->hp = hp;
}

void Player::set_posision(int coord_x, int coord_y){
    this->coord_x = coord_x;
    this->coord_y = coord_y;
}

void Player::be_attacked(int attacked_damage){
    hp -= attacked_damage;
    if (hp <= 0){
        is_alive = false;
    } 
}

void Player::show_status(){
    if (is_alive){
        cout << name << " has " << hp;
        cout << " pos:" << coord_x << "," <<coord_y;
        cout << endl;
    }else{
        cout << name << "is dead." << endl;
    }
}

int main(){
    Player player1;
    Player player2("Ben");
    Player player3("Luis");
    
    player2.set_hp(100);
    player2.set_posision(20,30);
    player1.be_attacked(50);
    player2.be_attacked(50);

    player1.show_status();
    player2.show_status();
    player3.show_status();
    
}