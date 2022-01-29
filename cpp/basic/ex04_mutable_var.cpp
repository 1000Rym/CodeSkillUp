#include <iostream>
using namespace std;

class Test{
    public:
        int x; 
        mutable int y;

    Test(int x, int y){
      this->x = x;
      this->y = y;
    }

};


int main(){
    const Test test(10, 20);
    test.y = 40;
    cout << test.x << "," << test.y << endl;

    return 0;
}