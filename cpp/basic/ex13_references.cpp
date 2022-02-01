#include <iostream>
#include <string>
using namespace std;

struct Person{
    string name;
    string job;
    int age;
};

 /* Reference Usecase 1
 Modify the passed parameters in a function.
 */
void swap(int& first, int& second)
{
    int temp = first; 
    first = second;
    second = temp;
}

/* Reference Usecase 2
 Avoiding a copy of large structures
*/
void introduce(const Person &person)
{
    /* To avoid a new copy of large structures data created, use reference.
     Use const to avoid the data is manipulated. */
    cout << "The Persons' name is " << person.name 
    << ", working as a " << person.job << " "
    << person.age <<" years old."<<endl;
}


int main()
{
    // Create a reference
    int my_var = 10;
    int& my_ref = my_var;
    my_ref = 20;
    cout << "my_var=" << my_var << ",";
    my_var = 30;
    cout << "my_ref=" << my_ref <<endl;

    // Swaping values by using reference.
    int first = 11, second = 22;
    cout << "Before the swaping the value was:" << first <<","<<second << endl;
    swap(first, second);
    cout << "After calling the swap() the vaue changed to " << first <<"," <<second<<endl;

    // Call function which dosen't generate structure memory.
    Person mike = {"Mike", "doctor", 43};
    introduce(mike);

    /* Reference Usecase 3
    - In For Each Loops to modify all objects
    */
   int my_vars [5] = {1,2,3,4,5};
   for(int& item : my_vars){
       item ++;
   }

   /* Reference Usecase 4
   - In For Eeach Loops to avoid the copy of objects.
   */
   for (const int item : my_vars){
       cout << item << " ";
   }
    cout << endl;


    return 0;
}