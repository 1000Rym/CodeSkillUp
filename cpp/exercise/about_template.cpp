/*
    In this cpp file, we are going to learn how to use template.
*/
#include <iostream>

using std::cout;
using std::endl;
using std::string;

// Multiple template type data.
template<typename A, typename B>
A add(A a, B b){
    return a + b;    
}

// Get type and data from template.
template<typename T, int size = 1> // size: default template parameter.
void print_array(T* array){
    for (int i = 0; i < size; i ++){
        cout << array[i] << " ";
    }
    cout << endl;
}

template <typename T>
struct Compare{
    bool operator()(const T& a, const T& b) const {
        return a < b; 
    }
};

// Transfer Class Type with default template name.
template <typename T, typename Comp = Compare<T>>
T min(T a, T b){
    Comp comp; 
    if(comp(a, b)){
        return a; 
    }else{
        return b;
    }
}

/* 
    The function is called when one param is remained.
*/
template <typename T>
void print(T arg) {
  cout << arg << endl;
}

/*
    The function is called recursively until one param is remained.
*/
template <typename T, typename... Types>
void print(T arg, Types... args) {
  cout << arg << " ";
  print(args...);
}

/*
    The function use sizeof.. to print arguments size.
*/
template<typename... Types>
void print_size(Types... args){
    cout << "Size is " << sizeof...(args) << endl; //sizeof... print args size.
}

/*
    Use fold expression
*/
template<typename... Types>
double sum_all(Types... args){
    return (... + args); // Fold expression supported from c++17
}


// Fold expression use case2.
class SimpleDecorator{
    public: 
        void decorate(int x) const {
            cout << "Decorated " << x << endl; 
        } 
};

template <typename T, typename... Types>
void decorate_nums(const T& t, Types... nums){
    (t.decorate(nums), ...);
}


int main(){
    int int_var = 10;
    double  double_var = 3.25;
    cout << add(double_var, int_var) << endl;
    int* my_int = new int[5];
    char* my_chars = (char*) "hello world";
    for(int i =0 ; i < 5; i++){
        my_int[i] = 100 +i ;
    }
    
    // print array with char type or int type.
    print_array<int, 5>(my_int);
    print_array<char, 10>(my_chars);

    // Compare<int> compare;
    // cout << compare(3,5) << endl;
    
    //> min of 5 and 6 is 5
    cout << "min of 5 and 6 is " << min(5,6) <<endl;
    print(1, 3.1, "abc");
    print(1, 2, 3, 4, 5, 6, 7);
    print_size(1, 2, 3, 4, 5, 6, 7);

    // fold expression case1:  print data.
    // > 20.25
    cout << sum_all(10,2,5, 3.25) << endl;

    // fold expression case2: decorate data
    SimpleDecorator d;
    decorate_nums(d, 1,2,3,4);
}