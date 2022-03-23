#include <iostream>
#include <cstring>
using std::cout;
using std::endl;

/*
Coding Exercise: Made for coding exercise, supports effective and customised string.
- constructor: char, char*, copy constructor.
- Operator:
    - friend use case: use friend to support customised effective string in &ostream operator<< 
    - Operator(=)
- supports string comparison.
*/
class EffectiveString{
    private : 
        char* str_content_;
        int str_len_;
    
    public :
        EffectiveString();
        template<typename T> EffectiveString(const T t);
        EffectiveString&  operator=(char c);
        EffectiveString&  operator=(const char* chars);
        char at(int index) const;
        char operator[](int index) const;
        
        // implement insert methods.
        template<typename T>EffectiveString& insert(int position, T contents);

        // use friend to let outputstream support effective string
        friend std::ostream& operator<< (std::ostream& os, EffectiveString& s);
};

// operator= : assign char value to the content.
EffectiveString&  EffectiveString::operator=(char c){
    str_content_ = new char[1];
    str_content_[0] = c;
    str_len_ = 1;
    return *this;
}

// operator= : assign char value to the content.
EffectiveString& EffectiveString::operator=(const char* str){
    str_content_ = new char[std::strlen(str)];
    std::strcpy(str_content_, str);
    str_len_ = std::strlen(str);
    return *this;
}

// Constructor: default
EffectiveString::EffectiveString():str_len_(0), str_content_(nullptr){}

// Constructor: Character or Charactors
template<typename T>
EffectiveString :: EffectiveString(const T t){
    this->operator=(t);
}

// Use friend to let the ostream operator supports Effective string class.
std::ostream& operator<< (std::ostream& os, EffectiveString& s){
    return (s.str_len_)>0 ? os << s.str_content_ : os;
}

char EffectiveString::at(int index) const{
    return (str_len_ > index) ? str_content_[index] : '\0';
}

char EffectiveString::operator[](int index) const{
    return at(index);
}

// insert a character to the target position.
template<typename T>
EffectiveString& EffectiveString::insert(int position, T contents){
    if (position>=0 && position < str_len_+1){ // Only work when the position is valid.
        char* str_content_pre = str_content_;
        EffectiveString temp(contents);
        int new_len = str_len_+ temp.str_len_;
        str_content_ = new char[new_len];

        for (int i = 0 ; i < new_len; i ++){
            if (i < position){
                str_content_[i] = str_content_pre[i];
            }else if (i < position + temp.str_len_){
                str_content_[i] = temp[i-position];
            }else{
                str_content_[i] = str_content_pre[i-temp.str_len_];
            }
        }

        delete[] str_content_pre;
        str_len_ = new_len;
    }
    return *this; 
}

int main(){
    EffectiveString my_str = "Hello world!";
    EffectiveString a;
    cout<< my_str << endl;
    cout << my_str[3] << endl;
    my_str.insert(3, "t3");
    cout << "The string changed after the insertion:" << my_str << endl; 
}