#include <iostream>
#include <vector>
using namespace std;

void print_vector(const vector<int>& vars){
    for (auto var : vars){
        cout << var << " ";
    }
    cout << endl;
}

int main(){
    // Fill Constructor
    // 5 10 vars 
    vector<int> vector_fill(5,10);
    print_vector(vector_fill);

    // Range Constructor
    vector<int> vector_range(vector_fill.begin(), vector_fill.end());
    print_vector(vector_range);

    // Copy Constructor
    vector<int> vector_cp(vector_fill);
    print_vector(vector_cp);

    return 0;
}