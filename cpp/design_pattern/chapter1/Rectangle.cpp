#include <iostream>

using namespace std; 

class Rectangle
{
    protected :
        int width, height; 
    public :
        Rectangle(const int width, const int height) : width(width), height(height){};
        const int get_width() {return width;}
        const int get_height() {return height;}

        virtual void set_width(const int width){
            this->width = width;
        }

        virtual void set_height(const int height){
            this->height = height; 
        }

        const int area() {
            return width * height;
        } 
};


class Square : public Rectangle{
    public:
        Square (const int size) : Rectangle(size, size){};
        void set_width(const int width) override {
            this->width = height = width;
        }

        void set_height(const int height) override {
            this->height = width = height;
        }  

};

int main(){
    cout << "Test my rectangle!"<<endl; 
}