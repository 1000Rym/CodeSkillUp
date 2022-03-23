/*
    Coding exercise
    - constructor 
        - default constructor 
        - copy constructor
        - initialize list : (constructor_name) : var1(arg1), var2(arg2) {}
    - deconstructor
    - static member variable: The variable share value with other objectes that been created with the class. 
    - The function that return reference 
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
    static int player_count; // static member variable. 

    public: 
        // Player() = default; // default constructor.
        Player(const Player&  player); 
        Player(); 
        Player(const char* name); 
        Player(const char* name, int hp);
        Player(const char* name, int hp, int coord_x, int coord_y);
        ~Player(); //  deconstructor
 
        static void show_player_count(); // declare static function.
        int& get_hp(); // the reference return variable.
        
        void set_hp(int hp);
        void be_attacked(int attacked_damage);
        void set_posision(int coord_x, int coord_y); 
        void show_status();
};

// initialize the static member variable.
int Player::player_count = 0;

// Copy Constructor
Player::Player(const Player& player):hp(player.hp), coord_x(player.coord_x), coord_y(player.coord_y),is_alive(player.is_alive){
    name = new char[strlen(player.name)+1];
    strcpy(name, player.name);
}

// initializer list(1)
Player::Player() : hp(50), coord_x(0), coord_y(0), is_alive(true){ 
    this->name = new char[strlen("Unknown")+1];
    std::strcpy(this->name, "Unknown");
    player_count ++;
}

// initializer list(2)
Player::Player(const char* name) : hp(50), coord_x(0), coord_y(0), is_alive(true){
    this->name = new char[strlen(name) +1];
    std::strcpy(this->name, name);
    player_count ++;
}

// initializer list(3)
Player::Player(const char* name, int hp) : hp(hp), coord_x(0), coord_y(0), is_alive(true){
    this->name = new char[strlen(name) +1];
    std::strcpy(this->name, name);
    player_count ++;
}

// initializer list(4)
Player::Player(const char* name, int hp, int coord_x, int coord_y) : hp(hp), coord_x(coord_x), coord_y(0), is_alive(true){
    this->name = new char[strlen(name) +1];
    std::strcpy(this->name, name);
    player_count ++;
}


Player::~Player(){
    cout << "Player " << this->name << " is destroyed." << endl;
    if (name != NULL){
        delete[] this->name;
    }
    player_count --;
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

int& Player::get_hp(){
    return this->hp;
}

void Player::show_player_count(){
    cout << "Now we have " << Player::player_count << " player(s) remained." << endl;
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
    
    // Static Function
    Player::show_player_count(); // static function should be callded with class.
    
    // The Function that return reference.
    int hp = player2.get_hp();
    hp = 70; // change the hp
    player2.show_status(); // Ben has 50 pos:20,30 -> member variable dosen't changed.
    // > Ben has 80 pos:20,30 -> member variable been changed.
    
    int& ref_hp = player2.get_hp();
    ref_hp = 80;
    player2.show_status();
    
    // > Ben has 75 pos:20,30
    player2.get_hp() = 75; // directly change the value.
    player2.show_status();


    // Copy Constructor type1
    Player player4(player2);
    cout << "player4: ";
    player4.show_status();

    // Copy Constructor type2
    Player player5 = player2;
    cout << "player5: ";
    player5.show_status();
}