#include <iostream>
#include <time.h>

using namespace std;

 //Generate number from 1~100, 10 times
void generateNumbers(int *numbers, int array_size){ 
    for (int i = 0 ; i< array_size; i++){
        numbers[i] = rand()%100 +1;
    }
}

// Display numbers.  
void displayNumbers(int *numbers, int array_size){
    for(int i=0; i< array_size; i ++){
        cout << numbers[i] << " ";
    }
    cout<< endl; 
}

void selectionSort(int *numbers, int array_size){
    for (int i =0; i < array_size; i ++){
        int smallestNumber = numbers[i];
        int position = i; 
        for(int j = i+1 ; j<array_size; j++){
            // If current number is smaller than previous smaller number, 
            // So change, smallest number and position.
            if(numbers[j] < smallestNumber) {
                position = j;
                smallestNumber = numbers[j];
             
            }
        }
        // Smallest number found in above process.
        // swap process is required. 
        if(i != position){
            numbers[position] = numbers[i];
            numbers[i] = smallestNumber;
        } 
        displayNumbers(numbers, array_size); 
    }  
}

//Insertion sort algorithm
void insertionSort(int *numbers, int array_size){
    int temp = 0; // will use extra O(1) space.
    for (int i =1 ; i  < array_size ; i++){
        // sort part. 
        for(int j = i ; j > 0 ; j--){
            //If current number is greater than previous number exchange 
            if (numbers[j] < numbers[j-1]){  
                temp = numbers[j];
                numbers[j] = numbers[j-1];
                numbers[j-1] = temp;
            }else{ // no need to exchange.
                break;  
            }
        }
    } 
}

//Bubble sort algorithm
void bubbleSort(int *numbers, int array_size){
    int temp = 0;
    for (int i = 0 ; i< array_size; i ++) {
        for (int j = 0; j< array_size; j ++){
            if(numbers[j] > numbers[j+1]){
                temp = numbers[j];
                numbers[j] = numbers[j+1];
                numbers[j+1] = temp;
            }
        }
    }
}

//void shell sort algorithm
void shellSort(int *numbers, int array_size){
    int temp = 0; // will use extra O(1) space.
    int gap = array_size;
    while(gap != 1) {
        gap /=2;  // gap sequentially reduce by half.

        for (int i = 0 ; i < array_size-gap; i++){
            // swap node and node+gap 
            if(numbers[i] > numbers[i+gap]){
                temp = numbers[i];
                numbers[i] = numbers[i+gap];
                numbers[i+gap] = temp;
            }
        }
    } 
}


int main(){
    const int array_size = 10; 
    int numbers[array_size]; 
    srand(time(NULL));
    generateNumbers(numbers, array_size);
    displayNumbers(numbers, array_size);
    //selectionSort(numbers, array_size);
    //insertionSort(numbers, array_size);
    //bubbleSort(numbers, array_size);
    shellSort(numbers, array_size);
    displayNumbers(numbers, array_size);
}